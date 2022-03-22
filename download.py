#! /usr/bin/python3

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

name_api_request = ['disruptions', 'vehicle_journeys','routes']
file_created = ['Page','Vehicle_journey','Routes']
api_request = [disruptions, vehicle_journeys,routes]

dossier = str(yesterday)


def search_string_in_file(file_name, string_to_search,just_lines=False): # return ligne number + ligne
    line_number = 0
    global result
    result = []
    if string_to_search == 'end_line': # for extract vehicle_journey & Routes
        return [line_count(file_name)]
    with open(file_name, 'r') as r:
        for line in r:
            line_number += 1
            if string_to_search in line:
                if just_lines:
                    result.append(line_number)
                else:    
                    result.append((line_number, line.rstrip()))

    return result


def sncf():
    for i in range(3):
        os.mkdir(f'{dossier}/{file_created[i]}')
        sousdossier = file_created[i]

        response = requests.get(api_request[i],
                    headers={ 'Authorization': f'{token}'}) # collect api file


        with open(f'{dossier}/{sousdossier}/' + f'{file_created[i]}0.txt', 'w') as f: # create file and store data in json format
            text = json.dumps(response.json(), sort_keys=True, indent=4)
            f.write(text)
            print(f'{file_created[i]}0.txt created')

        with open(f'{dossier}/{sousdossier}/' + f'{file_created[i]}0.txt', 'r') as f: # check if total_result exist
            if f.read().find('total_result'):
                print('Find : totat_result' )
                print(search_string_in_file(
                        f'{dossier}/{sousdossier}/'
                        + f'{file_created[i]}0.txt', 'total_result')
                    )

            else:
                print(f'No total_result in {file_created[i]}0.txt')

        bef,aft = str(result).split(':') # extract number of total_number and deduce number of page
        bef,aft = aft.split('\'')
        print(f'number of {file_created[i]} :',bef)

        max_page = int(bef) // 25
        print('Number of page:',max_page)

        for j in range(1,max_page+1): 
            response = requests.get(f'https://api.sncf.com/v1/coverage/sncf/{name_api_request[i]}?since={since}&start_page={j}&until={until}'.format(replace=name_api_request[i]),
                    headers={ 'Authorization': '{}'.format(token) })

            with open(f'{dossier}/{sousdossier}/' + f'{file_created[i]}{j}.txt', 'w') as f: #  create file and store data in json format
                text = json.dumps(response.json(), sort_keys=True, indent=4)
                f.write(text)
                print(f'{file_created[i]}{j}.txt created')
        print('Finish :', j, 'pages created')

string_begin = ['application_periods','calendars','\"direction\"']
string_end = ['feed_publishers','end_line','end_line']

def line_count(sample): # count line in file
    file = open(sample, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count

try:
    os.mkdir(dossier)
    sncf()
except:
    print('Path exist')
