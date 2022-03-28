#! /usr/bin/python3

import json
import os
import datetime

class Sort():
    
    def __init__(self):
        self.today = today = datetime.date.today()
        #self.yesterday = self.today - datetime.timedelta(days = 1)
        self.yesterday = '2022-03-24'
        self.file_created = ['Page','Vehicle_journey','Routes']
        self.NULL = 'NULL'

    def how_many_files(self,i):        
        count_file = 0
        dir = f"{self.yesterday}/{self.file_created[i]}"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                count_file += 1

        return count_file

    def which_data(self,z):
        with open(f'{self.yesterday}/Page/Page{z}.txt') as json_file:
            return json.load(json_file)

        
    def disruptions(self,z,i,j):

        with open(f'{self.yesterday}/Page/Page{z}.txt') as json_file:
            data = json.load(json_file)

            date = self.yesterday
            value = j
                
            try:    
                no, begin = str(data["disruptions"][i]['application_periods'][0]['begin']).split('T') # give just hhmmss
            except:
                begin = NULL
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
                severity_effect = data["disruptions"][i]['severity']['effect']
            except:
                severity_effect = self.NULL
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
                amended_arrival_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_arrival_time']
            except:
                amended_arrival_time = self.NULL
            try:
                amended_departure_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_departure_time']
            except:
                amended_departure_time = self.NULL
            try:    
                departure_status = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['departure_status']
            except:
                departure_status = self.NULL
            try:    
                base_arrival_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_arrival_time']
            except:
                base_arrival_time = self.NULL
            try:    
                base_departure_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_departure_time']
            except:
                base_departure_time = self.NULL
            try:    
                arrival_status = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['arrival_status']
            except:
                arrival_status = self.NULL
            try:    
                cause = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['cause']
            except:
                cause = self.NULL
            try:    
                is_detour = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['is_detour']
            except:
                is_detour = self.NULL
            try:    
                lat = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lat']
            except:
                lat = self.NULL
            try:    
                lon = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lon']
            except:
                lon = self.NULL
            try:    
                id_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['id']
            except:
                id_impacted_stop = self.NULL
            try:    
                label_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['label']
            except:
                label_impacted_stop = self.NULL
            try:    
                name_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['name']
            except:
                name_impacted_stop = self.NULL
            try:    
                stop_time_effect = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_time_effect']
            except:
                stop_time_effect = self.NULL

            return [date, begin, end, id, message, severity_effect, severity_name, trip_id, trip_name],[ date, begin, end, value, amended_arrival_time, amended_departure_time, departure_status, base_arrival_time, base_departure_time, arrival_status, cause, is_detour, lat, lon, id_impacted_stop, label_impacted_stop, name_impacted_stop, stop_time_effect]


    def vehicle_journey(self,z,i,j):

        with open(f'{self.yesterday}/Vehicle_journey/Vehicle_journey{z}.txt') as json_file:
            data2 = json.load(json_file)
            
            value = j
            date = self.yesterday
                        
            try:    
                begin = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['begin']
            except:
                begin = self.NULL
            try:    
                end = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['end']
            except:
                end = self.NULL
            # week_pattern = data2['vehicle_journeys'][i]['calendars'][0]['week_pattern'] # garde just true
            try:    
                id = data2['vehicle_journeys'][i]['id']
            except:
                id = self.NULL
            try:    
                name = data2['vehicle_journeys'][i]['name'] # = headsign
            except:
                name = self.NULL
            try:    
                trip_id = data2['vehicle_journeys'][i]['trip']['id']
            except:
                trip_id = self.NULL
            try:    
                trip_name = data2['vehicle_journeys'][i]['trip']['name']
            except:
                trip_name = self.NULL
            try:    
                arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['arrival_time']
            except:
                arrival_time = self.NULL
            try:    
                departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['departure_time']
            except:
                departure_time = self.NULL
            try:    
                drop_off_allowed = data2['vehicle_journeys'][i]['stop_times'][j]['drop_off_allowed']
            except:
                drop_off_allowed = self.NULL
            try:    
                headsign = data2['vehicle_journeys'][i]['stop_times'][j]['headsign']
            except:
                headsign = self.NULL
            try:    
                pickup_allowed = data2['vehicle_journeys'][i]['stop_times'][j]['pickup_allowed']
            except:
                pickup_allowed = self.NULL
            try:    
                skipped_stop = data2['vehicle_journeys'][i]['stop_times'][j]['skipped_stop']
            except:
                skipped_stop = self.NULL
            try:    
                lat = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lat']
            except:
                lat = self.NULL
            try:    
                lon = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lon']
            except:
                lon = self.NULL
            try:    
                id_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['id']
            except:
                id_stop_point = self.NULL
            try:    
                label_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['label']
            except:
                label_stop_point = self.NULL
            try:    
                name_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['name']
            except:
                name_stop_point = self.NULL
            try:    
                utc_arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_arrival_time']
            except:
                utc_arrival_time = self.NULL
            try:
                utc_departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_departure_time']
            except:
                utc_departure_time = self.NULL
                
            return [date, begin, end, id, name, trip_id, trip_name],[date, begin, end, value, arrival_time, departure_time, drop_off_allowed, headsign, pickup_allowed, skipped_stop, lat, lon, id_stop_point, label_stop_point, name_stop_point, utc_arrival_time, utc_departure_time]


    def routes(self,z,i,j):

        with open(f'{self.yesterday}/Routes/Routes{z}.txt') as json_file:
            data3 = json.load(json_file)

                                    
            date = self.yesterday

            try:
                embedded_type = data3['routes'][i]['direction']['embedded_type']
            except:
                embedded_type = self.NULL
            try:
                id_direction = data3['routes'][i]['direction']['id']
            except:
                id_direction = self.NULL
            try:
                name_direction = data3['routes'][i]['direction']['name']
            except:
                name_direction = self.NULL
            try:
                quality = data3['routes'][i]['direction']['quality'] # utile ?
            except:
                quality = self.NULL
            try:
                value = data3['routes'][i]['direction']['stop_area']['codes'][0]['value']
            except:
                value = self.NULL
            try:
                lat = data3['routes'][i]['direction']['stop_area']['coord']['lat']
            except:
                lat = self.NULL
            try:
                lon = data3['routes'][i]['direction']['stop_area']['coord']['lon']
            except:
                lon = self.NULL
            try:
                id_stop_area = data3['routes'][i]['direction']['stop_area']['id']
            except:
                id_stop_area = self.NULL
            try:
                label_stop_area = data3['routes'][i]['direction']['stop_area']['label']
            except:
                label_stop_area = self.NULL
            try:
                name_stop_area = data3['routes'][i]['direction']['stop_area']['name']
            except:
                name_stop_area = self.NULL
            try:
                direction_type = data3['routes'][i]['direction_type']
            except:
                direction_type = self.NULL
            try:
                id = data3['routes'][i]['id']
            except:
                id = self.NULL
            try:
                is_frequence = data3['routes'][i]['is_frequence']
            except:
                is_frequence = self.NULL
            try:
                closing_time = data3['routes'][i]['line']['closing_time']
            except:
                closing_time = self.NULL
            try:
                id_commercial_mode = data3['routes'][i]['line']['commercial_mode']['id']
            except:
                id_commercial_mode = self.NULL
            try:
                name_commercial_mode = data3['routes'][i]['line']['commercial_mode']['name']
            except:
                name_commercial_mode = self.NULL
            try:
                id_line = data3['routes'][i]['line']['id']
            except:
                id_line = self.NULL
            try:
                id_name = data3['routes'][i]['line']['name']
            except:
                id_name = self.NULL
            try:
                opening_time = data3['routes'][i]['line']['opening_time']
            except:
                opening_time = self.NULL
            try:
                id_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['id']
            except:
                id_physical_modes = self.NULL
            try:
                name_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['name']
            except:
                name_physical_modes = self.NULL
            try:
                name = data3['routes'][i]['name']
            except:
                name = self.NULL
                    

            return [date, embedded_type, id_direction, name_direction, quality, value, lat, lon, id_stop_area, label_stop_area, name_stop_area, direction_type, id, is_frequence, closing_time, id_commercial_mode, name_commercial_mode, id_line, id_name, opening_time, id_physical_modes, name_physical_modes, name]

#print(Sort().disruptions())
#Sort().vehicle_journey()
#Sort().routes()

