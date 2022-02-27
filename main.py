#!/usr/bin/python3

import secret
import requests
import json
import datetime

dt = datetime.datetime.now()

year = dt.year
month = dt.month
day = dt.day

print(year)
print(month)
print(day)

token = str(secret.token())
since = f'{year}02{day-1}T000000'
until = f'{year}02{day}T000000'


response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/disruptions?since={since}&start_page=0&until={until}',
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



with open('Page0.txt', 'w') as f: # cree fichier et mets data dedans en format json
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    f.write(text)
    print('Page0.txt created')

with open('Page0.txt', 'r') as f: # vérifie si total_result présent
    if f.read().find('total_result'):
        print('Find : totat_result' )
        print(search_string_in_file('Page0.txt', 'total_result'))
    else:
        print('No total_result in Page0.txt')

bef,aft = str(result).split(':')
bef,aft = aft.split('\'')
print('number of disruption :',bef)

max_page = int(int(bef) / 25)
print('Number of page:',max_page)

for i in range(1,max_page+1):
    response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/disruptions?since={since}&start_page={i}&until={until}',
            headers={ 'Authorization': '{}'.format(token) })
    
    with open(f'Page{i}.txt', 'w') as f: # cree fichier et mets data dedans en format json
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)
        print(f'Page{i}.txt created')
print('Finish :', i, 'pages created')




response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/vehicle_journeys?since={since}&start_page=0&until={until}',
            headers={ 'Authorization': '{}'.format(token) })


with open('vehicle_journey0.txt', 'w') as f: # cree fichier et mets data dedans en format json
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    f.write(text)
    print('vehicle_journey0.txt created')

with open('vehicle_journey0.txt', 'r') as f: # vérifie si total_result présent
    if f.read().find('total_result'):
        print('Find : totat_result' )
        print(search_string_in_file('vehicle_journey0.txt', 'total_result'))
    else:
        print('No total_result in vehicle_journey0.txt')

bef,aft = str(result).split(':')
bef,aft = aft.split('\'')
print('number of vehicle in the journey :',bef)

max_page = int(int(bef) / 25)
print('Number of page:',max_page)

for i in range(1,max_page+1):
    response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/vehicle_journeys?since={since}&start_page={i}&until={until}',
            headers={ 'Authorization': '{}'.format(token) })
    
    with open(f'Vehicle_journey{i}.txt', 'w') as f: # cree fichier et mets data dedans en format json
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)
        print(f'Vehicle_journey{i}.txt created')
print('Finish :', i, 'Vehicle_journey created')





response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/routes?since={since}&start_page=0&until={until}',
            headers={ 'Authorization': '{}'.format(token) })


with open('Routes0.txt', 'w') as f: # cree fichier et mets data dedans en format json
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    f.write(text)
    print('Routes0.txt created')

with open('Routes0.txt', 'r') as f: # vérifie si total_result présent
    if f.read().find('total_result'):
        print('Find : totat_result' )
        print(search_string_in_file('Routes0.txt', 'total_result'))
    else:
        print('No total_result in Routes0.txt')

bef,aft = str(result).split(':')
bef,aft = aft.split('\'')
print('number of Routes :',bef)

max_page = int(int(bef) / 25)
print('Number of page:',max_page)

for i in range(1,max_page+1):
    response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/routes?since={since}&start_page={i}&until={until}',
            headers={ 'Authorization': '{}'.format(token) })
    
    with open(f'Routes{i}.txt', 'w') as f: # cree fichier et mets data dedans en format json
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)
        print(f'Routes{i}.txt created')
print('Finish :', i, 'Routes created')




response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/lines?since={since}&start_page=0&until={until}',
            headers={ 'Authorization': '{}'.format(token) })


with open('Lines0.txt', 'w') as f: # cree fichier et mets data dedans en format json
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    f.write(text)
    print('Lines0.txt created')

with open('Lines0.txt', 'r') as f: # vérifie si total_result présent
    if f.read().find('total_result'):
        print('Find : totat_result' )
        print(search_string_in_file('Lines0.txt', 'total_result'))
    else:
        print('No total_result in Lines0.txt')

bef,aft = str(result).split(':')
bef,aft = aft.split('\'')
print('number of Lines :',bef)

max_page = int(int(bef) / 25)
print('Number of page:',max_page)

for i in range(1,max_page+1):
    response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/lines?since={since}&start_page={i}&until={until}',
            headers={ 'Authorization': '{}'.format(token) })
    
    with open(f'Lines{i}.txt', 'w') as f: # cree fichier et mets data dedans en format json
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        f.write(text)
        print(f'Lines{i}.txt created')
print('Finish :', i, 'Lines created')











'''
implementer month

https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/
https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/

'''
