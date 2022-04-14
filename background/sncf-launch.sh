#! /usr/bin/env bash

# This script is used to launch the download.py script
# Put the file in /bin and make it executable (chmod +x sncf-launch.sh)
# and the create a cronjob to launch it every time the computer is turned on

yesterday=$(date -d "yesterday" +"%Y-%m-%d")
yesterday2=$(date -d "yesterday" +"%Y_%m_%d")
echo "yesterday: $yesterday";
echo "yesterday2: $yesterday2";
# Path to the folder where the data will be downloaded to change for your own 
cd /home/idefux/Dokumente/School/L1/Semestre\ 2/Bases\ de\ données\ relationnelles/Test_projet/sncf_data 

# check if folder exists else download data
if [ -d "$yesterday" ]; then
    echo "Folder $yesterday exists"
    cd ..
else
    echo "Folder $yesterday does not exist"
    echo "Downloading data"
    cd ..
    python3 background/download.py
fi

cd sncf_data/$yesterday

# check if 3 folders exist else download data
if [ -d "Page" ] && [ -d "Routes" ] && [ -d "Vehicle_journey" ]; then
    echo "All folders exist"
else
    echo "Some folders do not exist"
    echo "Delete folder $yesterday"
    cd ..
    rm -rf $yesterday
    echo "Downloading data"
    cd ..
    python3 background/download.py

fi

# setup mysql server and datbase to store data
# try to start mysql server else error message


UP=$(/etc/init.d/mysql status | grep running | grep -v not | wc -l);
if [ "$UP" -ne 1 ];
then
    echo "MySQL is down.";
    echo "MySql is starting..."
    echo "Password" | sudo -S service mysql start
    echo "MySQL is up"
else
    echo "MySQL is running.";
fi

# check if SNCF database exists else create it else exit
if [ -d "/var/lib/mysql/SNCF" ]; then
    echo "Database SNCF does not exist"
    echo "Creating database SNCF"
    mysql -u root -e "CREATE DATABASE SNCF"
else
    echo "Database SNCF exists"
fi

# check if files disruptions_${yesterday} exist in sncf database else transfering data
MT=$(mysql -u root -e "select count(*) from information_schema.tables where table_schema='SNCF' and table_name='disruptions_$yesterday2';" | grep -iv "count")
if [ $MT -eq 1 ]; then
    echo "File disruptions_${yesterday2} exists"
    echo "The data might be already in the database"
else
    echo "Data from ${yesterday2} not in database SNCF"
    echo "Transferring data to database SNCF"
    cd /home/idefux/Dokumente/School/L1/Semestre\ 2/Bases\ de\ données\ relationnelles/Test_projet
    python3 background/sql.py
fi

# Shutdown mysql server if it is running
UP=$(/etc/init.d/mysql status | grep running | grep -v not | wc -l);
if [ "$UP" -eq 1 ];
then
    echo "Shutdown MySQL.";
    echo "Password" | sudo -S service mysql stop
    echo "MySQL is down.";
else
    echo "MySQL is still running.";
fi
