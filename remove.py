import datetime
from datetime import date, timedelta
import os, os.path
import re

first_date = date(2022,2,1) #a remplacer par le premier jour enregistré dans la base de donnée
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
strdate = str(yesterday).replace("0", "")
y1, m1, d1 = strdate.split('-')
date(int(y1), int(m1), int(d1))
delta = yesterday - first_date

files = []
file_created = ['Page', 'Vehicle_journey', 'Routes']

def main(): # pour enlever tout les fichiers en trop.
    global dossier
    for i in range(delta.days + 1):
        day = first_date + timedelta(days=i)
        dossier = str(day)
        if (os.path.exists(dossier)):
            for i in range(0, 3):
                sousdossier = file_created[i]
                DIR = f'{dossier}/{sousdossier}'
                for _file in os.listdir(DIR):
                    if re.search(f'{file_created[i]}[0-9].txt', _file):
                        os.remove(DIR + '/' + _file)
                        print(_file + ' removed')
                    elif re.search(f'{file_created[i]}[0-9][0-9].txt', _file):
                        os.remove(DIR + '/' + _file)
                        print(_file + ' removed')
                    elif re.search(f'{file_created[i]}[0-9][0-9][0-9].txt', _file):
                        os.remove(DIR + '/' + _file)
                        print(_file + ' removed')
                else:
                    print('Error' + dossier + ' does not exist')
            

    
main()
