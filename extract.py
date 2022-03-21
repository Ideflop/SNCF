#! /usr/bin/python3

import json
import os
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)

file_created = ['Page','Vehicle_journey','Routes']


def how_many_files(i):        
    count_file = 0
    dir = f"{yesterday}/{file_created[i]}"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            count_file += 1

    return count_file

def disruptions():

    result = how_many_files(0)
    for i in range(result):
        with open(f'{yesterday}/Page/Page{result}.txt') as json_file:
            data = json.load(json_file)

            i = 0
            for x in data['disruptions']:
                j = 0
                for y in data['disruptions'][i]['impacted_objects']:

                    print(data["disruptions"][i]['application_periods'][0]['begin']) # give just hhmmss
                    print(data["disruptions"][i]['application_periods'][0]['end']) # give just hhmmss
                    print(data["disruptions"][i]['id']) # = disruption_id disruption_uri impacteed_object

                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_arrival_time'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_departure_time'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['arrival_status'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_arrival_time'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_departure_time'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['cause'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['departure_status'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['is_detour'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lat'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lon'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['id'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['label'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['name'])
                    print(data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_time_effect'])
                    
                    print(data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['id'])
                    print(data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['name'])
                    print(data["disruptions"][i]['messages'][0]['text'])
                    print(data["disruptions"][i]['severity']['effect'])
                    print(data["disruptions"][i]['severity']['name'])

                    j += 1
                i += 1


def vehicle_journey():

    result = how_many_files(i)
    for i in range(result):
        
        with open(f'{yesterday}/Vehicle_journey/Vehicle_journey{result}.txt') as json_file:
            data2 = json.load(json_file)

            i = 0
            for x in data2['vehicle_journeys']:

                j = 0
                for y in data2['vehicle_journeys'][i]['stop_times']:

                    print(data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['begin'])
                    print(data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['end'])
                    print(data2['vehicle_journeys'][i]['calendars'][0]['week_pattern']) # garde just true
                    print(data2['vehicle_journeys'][i]['id'])
                    print(data2['vehicle_journeys'][i]['name']) # = headsign

                    print(data2['vehicle_journeys'][i]['stop_times'][j]['arrival_time'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['departure_time'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['drop_off_allowed'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['headsign'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['pickup_allowed'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['skipped_stop'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lat'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lon'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['id'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['label'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['name'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['utc_arrival_time'])
                    print(data2['vehicle_journeys'][i]['stop_times'][j]['utc_departure_time'])

                    print(data2['vehicle_journeys'][i]['trip']['id'])
                    print(data2['vehicle_journeys'][i]['trip']['name'])

                    j += 1
                i += 1


def routes():

    result = how_many_files(2)
    for i in range(result):

        with open(f'{yesterday}/Routes/Routes0.txt') as json_file:
            data3 = json.load(json_file)

            i = 0
            for x in data3['routes']:

                print(data3['routes'][i]['direction']['embedded_type'])
                print(data3['routes'][i]['direction']['id'])
                print(data3['routes'][i]['direction']['name'])
                print(data3['routes'][i]['direction']['quality']) # utile ? 
                print(data3['routes'][i]['direction']['stop_area']['codes'][0]['value'])
                print(data3['routes'][i]['direction']['stop_area']['coord']['lat'])
                print(data3['routes'][i]['direction']['stop_area']['coord']['lon'])
                print(data3['routes'][i]['direction']['stop_area']['id'])
                print(data3['routes'][i]['direction']['stop_area']['label'])
                print(data3['routes'][i]['direction']['stop_area']['name'])
                print(data3['routes'][i]['direction_type'])
                print(data3['routes'][i]['id'])
                print(data3['routes'][i]['is_frequence'])
                print(data3['routes'][i]['line']['closing_time'])
                print(data3['routes'][i]['line']['commercial_mode']['id'])
                print(data3['routes'][i]['line']['commercial_mode']['name'])
                print(data3['routes'][i]['line']['id'])
                print(data3['routes'][i]['line']['name'])
                print(data3['routes'][i]['line']['opening_time'])
                print(data3['routes'][i]['line']['physical_modes'][0]['id'])
                print(data3['routes'][i]['line']['physical_modes'][0]['name'])
                print(data3['routes'][i]['name'])

                i += 1

#disruptions()
#vehicle_journey()
#routes()
