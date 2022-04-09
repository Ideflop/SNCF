#! /usr/bin/env bash

# This script is used to launch the download.py script
# Put the file in /bin and make it executable (chmod +x sncf-launch.sh)
# and the create a cronjob to launch it every time the computer is turned on

yesterday=$(date -d "yesterday" +"%Y-%m-%d")
# Path to the folder where the data will be downloaded to change for your own 
cd /home/idefux/Dokumente/School/L1/Semestre\ 2/Bases\ de\ données\ relationnelles/Test_projet 

# check if folder exists else download data
if [ -d "$yesterday" ]; then
    echo "Folder $yesterday exists"
else
    echo "Folder $yesterday does not exist"
    echo "Downloading data"
    python3 download.py
fi

cd $yesterday

# check if 3 folders exist else download data
if [ -d "Page" ] && [ -d "Routes" ] && [ -d "Vehicle_journey" ]; then
    echo "All folders exist"
else
    echo "Some folders do not exist"
    echo "Delete folder $yesterday"
    cd ..
    rm -rf $yesterday
    echo "Downloading data"
    python3 download.py
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
