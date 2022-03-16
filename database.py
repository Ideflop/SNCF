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

def main():
    global dossier
    for i in range(delta.days + 1):
        day = first_date + timedelta(days=i)
        dossier = str(day)
        if (os.path.exists(dossier)):
            remove()
            word()
        else:
            print('Error' + dossier + ' does not exist')
            
def remove(): # pour enlever tout les fichiers en trop.
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

def word():
    for p in range(0, 3):
        file, sousdossier = file_created[p], file_created[p]
        DIR = f'{dossier}/{sousdossier}'    
        numfiles = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))//25
        print(numfiles)
        for i in range(0, numfiles):
            for j in range(0, 25):
                if (os.path.exists(DIR + f'/{file}{i}-{j}.txt')):
                    with open(DIR + f'/{file}{i}-{j}.txt') as f:
                        if 'embedded_type' in f.read():
                            print("true")
                else:
                    print(DIR + f'/{file}{i}-{j}.txt does not exist')
main()