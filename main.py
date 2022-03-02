#!/usr/bin/python3

import requests
import json
import datetime
import secret
import os


today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)

bef,mid,aft = str(today).split('-')
date_today = [bef, *(mid, aft)]
until = "".join(date_today)

bef,mid,aft = str(yesterday).split('-')
date_yesterday = [bef, *(mid, aft)]
since = "".join(date_yesterday)

token = str(secret.token())
since = f'{since}T000000'
until = f'{until}T000000'

print(since)
print(until)

disruptions = f'https://api.sncf.com/v1/coverage/sncf/disruptions?since={since}&start_page=0&until={until}'
vehicle_journeys = f'https://api.sncf.com/v1/coverage/sncf/vehicle_journeys?since={since}&start_page=0&until={until}'
routes = f'https://api.sncf.com/v1/coverage/sncf/routes?since={since}&start_page=0&until={until}'
lignes =  f'https://api.sncf.com/v1/coverage/sncf/lines?since={since}&start_page=0&until={until}'

name_api_request = ['disruptions', 'vehicle_journeys','routes', 'lines']
file_created = ['Page','Vehicle_journey','Routes','Lines']
api_request = [disruptions, vehicle_journeys,routes, lignes]

dossier = str(yesterday)
    
def sncf():
    for i in range(0,4):
        os.mkdir(dossier + "/" + file_created[i])
        sousdossier = file_created[i]

        response = requests.get(api_request[i],
                    headers={ 'Authorization': '{}'.format(token) }) # va api avec début + fin en stcok response


        def search_string_in_file(file_name, string_to_search): # renvoie ligne + numéro de la ligne
            line_number = 0
            global result
            result = []
            with open(file_name, 'r') as r:
                for line in r:
                    line_number += 1
                    if string_to_search in line:
                        result.append((line_number, line.rstrip()))
        
            return result


        with open(dossier + "/" + sousdossier + "/" + f'{file_created[i]}0.txt', 'w') as f: # cree fichier et mets data dedans en format json
            text = json.dumps(response.json(), sort_keys=True, indent=4)
            f.write(text)
            print(f'{file_created[i]}0.txt created')

        with open(dossier + "/" + sousdossier + "/" + f'{file_created[i]}0.txt', 'r') as f: # vérifie si total_result présent
            if f.read().find('total_result'):
                print('Find : totat_result' )
                print(search_string_in_file(dossier + "/" + sousdossier + "/" + f'{file_created[i]}0.txt', 'total_result'))
            else:
                print(f'No total_result in {file_created[i]}0.txt')

        bef,aft = str(result).split(':')
        bef,aft = aft.split('\'')
        print(f'number of {file_created[i]} :',bef)

        max_page = int(int(bef) / 25)
        print('Number of page:',max_page)

        for j in range(1,max_page+1):
            response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/{name_api_request[i]}?since={since}&start_page={j}&until={until}'.format(replace=name_api_request[i]),
                    headers={ 'Authorization': '{}'.format(token) })
            
            with open(dossier + "/" + sousdossier + "/" + f'{file_created[i]}{j}.txt', 'w') as f: # cree fichier et mets data dedans en format json
                text = json.dumps(response.json(), sort_keys=True, indent=4)
                f.write(text)
                print(f'{file_created[i]}{j}.txt created')
        print('Finish :', j, 'pages created')

try:
    os.mkdir(dossier)
    sncf()
except:
    print('Path exist')


'''

https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/
https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/

'''
