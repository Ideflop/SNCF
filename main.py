#!/usr/bin/python3

import requests
import json

token = 'token'
since = '20220224T000000'
until = '20220225T000000'

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
print(bef)

max_page = int(int(bef) / 25)
print(max_page)






'''
https://api.sncf.com/v1/coverage/sncf/disruptions?since=20220224T000000&start_page=0&until=20220225T000000




https://api.sncf.com/v1/coverage/sncf/vehicle_journeys?since=20220222T000000&start_page=0&until=20220223T000000
https://api.sncf.com/v1/coverage/sncf/disruptions?start_page=0&since=20220222T000000&until=20220223T000000&
https://api.sncf.com/v1/coverage/sncf/routes?since=20220222T000000&start_page=0&until=20220223T000000
https://api.sncf.com/v1/coverage/sncf/lines?since=20220222T000000&start_page=0&until=20220223T000000
https://api.sncf.com/v1/coverage/sncf/companies?since=20220222T000000&start_page=0&until=20220223T000000


https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/
https://www.avisia.fr/news/tribune-expert/tutoriel-visualiser-la-position-des-trains-de-la-sncf-en-temps-reel/

'''