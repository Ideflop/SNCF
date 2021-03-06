#! /usr/bin/python3

import json
import os
import datetime

class Sort():
    
    def __init__(self): # constructor
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        #self.yesterday = '2022-04-01'
        self.file_created = ['Page','Vehicle_journey','Routes']
        self.dir = f'scnf_data/{self.yesterday}'
        self.NULL = 'zzz'
        self.number = '00'
        try:
            os.chdir(f'sncf_data/{self.yesterday}')
        except:
            pass
        

    def how_many_files(self,i): # i = 0,1,2    
        count_file = 0
        #dir = f"{self.dir}/{self.yesterday}/{self.file_created[i]}"
        for path in os.listdir(f'{self.file_created[i]}'): # list of files in the directory
            if os.path.isfile(os.path.join(f'{self.file_created[i]}', path)):
                count_file += 1

        return count_file

    def which_data(self,z,q): # i = 0,1,2
        with open(f'{self.file_created[q]}/{self.file_created[q]}{z}.txt') as json_file:
            return json.load(json_file)

    def disruptions(self,z,i,j): 
        with open(f'Page/Page{z}.txt') as json_file:
            data = json.load(json_file)
                
            try:    
                no, begin = str(data["disruptions"][i]['application_periods'][0]['begin']).split('T') # give just hhmmss
            except:
                begin = self.number
            try:    
                no, end = str(data["disruptions"][i]['application_periods'][0]['end']).split('T') # give just hhmmss
            except:
                end = self.NULL
            try:    
                id = data["disruptions"][i]['id'] # = disruption_id disruption_uri impacteed_object
            except:
                id = self.NULL
            try:
                message = data["disruptions"][i]['messages'][0]['text'] # try
            except:
                message = self.NULL
            try:    
                severity_name = data["disruptions"][i]['severity']['name']
            except:
                severity_name = self.NULL
            try:    
                trip_id = data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['id']
            except:
                trip_id = self.NULL
            try:    
                trip_name = data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['name']
            except:
                trip_name = self.NULL
            try:
                amended_arrival_time = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['amended_arrival_time']
            except:
                amended_arrival_time = self.number
            try:
                amended_departure_time = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['amended_departure_time']
            except:
                amended_departure_time = self.number
            try:    
                departure_status = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['departure_status']
            except:
                departure_status = self.NULL
            try:    
                base_arrival_time = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['base_arrival_time']
            except:
                base_arrival_time = self.number
            try:    
                base_departure_time = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['base_departure_time']
            except:
                base_departure_time = self.number
            try:    
                arrival_status = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['arrival_status']
            except:
                arrival_status = self.NULL
            try:    
                cause = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['cause']
            except:
                cause = self.NULL
            try:    
                lat = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['stop_point']['coord']['lat']
            except:
                lat = self.number
            try:    
                lon = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['stop_point']['coord']['lon']
            except:
                lon = self.number
            try:    
                id_impacted_stop = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['stop_point']['id']
            except:
                id_impacted_stop = self.NULL
            try:    
                name_impacted_stop = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['stop_point']['name']
            except:
                name_impacted_stop = self.NULL
            try:    
                stop_time_effect = data["disruptions"][i]['impacted_objects'][0]['impacted_stops'][j]['stop_time_effect']
            except:
                stop_time_effect = self.NULL
            
            return [begin, end, id, message, severity_name, trip_id, trip_name],[amended_arrival_time, amended_departure_time, departure_status, base_arrival_time, base_departure_time, arrival_status, cause, lat, lon, id_impacted_stop, name_impacted_stop, stop_time_effect, trip_name]

    def vehicle_journey(self,z,i,j):

        with open(f'Vehicle_journey/Vehicle_journey{z}.txt') as json_file:
            data2 = json.load(json_file)
            

            try:    
                begin = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['begin']
            except:
                begin = self.number
            try:    
                end = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['end']
            except:
                end = self.number
            try:    
                headsign = data2['vehicle_journeys'][i]['headsign']
            except:
                headsign = self.number
            try:    
                id = data2['vehicle_journeys'][i]['id']
            except:
                id = self.NULL
            try:    
                trip_id = data2['vehicle_journeys'][i]['trip']['id']
            except:
                trip_id = self.NULL
            try:    
                arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['arrival_time']
            except:
                arrival_time = self.number
            try:    
                departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['departure_time']
            except:
                departure_time = self.number
            try:    
                headsign_stop = data2['vehicle_journeys'][i]['stop_times'][j]['headsign']
            except:
                headsign_stop = self.number
            try:    
                lat = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lat']
            except:
                lat = self.number
            try:    
                lon = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lon']
            except:
                lon = self.number
            try:    
                id_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['id']
            except:
                id_stop_point = self.NULL
            try:    
                name_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['name']
            except:
                name_stop_point = self.NULL
            try:    
                utc_arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_arrival_time']
            except:
                utc_arrival_time = self.number
            try:
                utc_departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_departure_time']
            except:
                utc_departure_time = self.number
                
            return [begin, end, headsign, id, trip_id ],[arrival_time, departure_time, headsign_stop, lat, lon, id_stop_point, name_stop_point, utc_arrival_time, utc_departure_time,]


    def routes(self,z,i):

        with open(f'Routes/Routes{z}.txt') as json_file:
            data3 = json.load(json_file)

            try:
                id_direction = data3['routes'][i]['direction']['id']
            except:
                id_direction = self.NULL
            try:
                value = data3['routes'][i]['direction']['stop_area']['codes'][0]['value'] # defois pas que int
            except:
                value = self.number
            try:
                lat = data3['routes'][i]['direction']['stop_area']['coord']['lat']
            except:
                lat = self.number
            try:
                lon = data3['routes'][i]['direction']['stop_area']['coord']['lon']
            except:
                lon = self.number
            try:
                id_stop_area = data3['routes'][i]['direction']['stop_area']['id']
            except:
                id_stop_area = self.NULL
            try:
                name_stop_area = data3['routes'][i]['direction']['stop_area']['name']
            except:
                name_stop_area = self.NULL
            try:
                closing_time = data3['routes'][i]['line']['closing_time']
            except:
                closing_time = self.number
            try:
                id_commercial_mode = data3['routes'][i]['line']['commercial_mode']['id']
            except:
                id_commercial_mode = self.NULL
            try:
                name_commercial_mode = data3['routes'][i]['line']['commercial_mode']['name']
            except:
                name_commercial_mode = self.NULL
            try:
                opening_time = data3['routes'][i]['line']['opening_time']
            except:
                opening_time = self.number
            try:
                id_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['id']
            except:
                id_physical_modes = self.NULL
            try:
                name_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['name']
            except:
                name_physical_modes = self.NULL
            try:
                routes_name = data3['routes'][i]['name']
            except:
                routes_name = self.NULL
        
            return [id_direction, value, id_stop_area, lat, lon, name_stop_area, closing_time, id_commercial_mode, name_commercial_mode, opening_time, id_physical_modes, name_physical_modes, routes_name]

        
#print(Sort().disruptions())
#Sort().vehicle_journey()
#Sort().routes()
