#! /usr/bin/python3

import json
import os
import datetime

class Sort():
    
    def __init__(self):
        self.today = today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        self.file_created = ['Page','Vehicle_journey','Routes']

    def how_many_files(self,i):        
        count_file = 0
        dir = f"{self.yesterday}/{self.file_created[i]}"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                count_file += 1

        return count_file

    def disruptions(self):

        result = Sort().how_many_files(0)
        for z in range(result-1):
            with open(f'{self.yesterday}/Page/Page{z}.txt') as json_file:
                data = json.load(json_file)

                i = 0
                for x in data['disruptions']:
                    j = 0
                    for y in data['disruptions'][i]['impacted_objects']:

                        date = self.yesterday
                        no, begin = str(data["disruptions"][i]['application_periods'][0]['begin']).split('T') # give just hhmmss
                        no, end = str(data["disruptions"][i]['application_periods'][0]['end']).split('T') # give just hhmmss
                        id = data["disruptions"][i]['id'] # = disruption_id disruption_uri impacteed_object

                        value = j
                        amended_arrival_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_arrival_time']
                        amended_departure_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['amended_departure_time']
                        departure_status = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['departure_status']
                        base_arrival_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_arrival_time']
                        base_departure_time = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['base_departure_time']
                        arrival_status = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['arrival_status']
                        cause = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['cause']
                        is_detour = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['is_detour']
                        lat = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lat']
                        lon = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['coord']['lon']
                        id_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['id']
                        label_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['label']
                        name_impacted_stop = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_point']['name']
                        stop_time_effect = data["disruptions"][i]['impacted_objects'][j]['impacted_stops'][0]['stop_time_effect']

                        message = data["disruptions"][i]['messages'][0]['text'] # try
                        severity_effect = data["disruptions"][i]['severity']['effect']
                        severity_name = data["disruptions"][i]['severity']['name']
                        trip_id = data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['id']
                        trip_name = data["disruptions"][i]['impacted_objects'][0]['pt_object']['trip']['name']

                        return [date, begin, end, id, message, severity_effect, severity_name, trip_id, trip_name],[ date, begin, end, value, amended_arrival_time, amended_departure_time, departure_status, base_arrival_time, base_departure_time, arrival_status, cause, is_detour, lat, lon, id_impacted_stop, label_impacted_stop, name_impacted_stop, stop_time_effect]

                        j += 1
                    i += 1


    def vehicle_journey(self):

        result = how_many_files(i)
        for z in range(result):

            with open(f'{self.yesterday}/Vehicle_journey/Vehicle_journey{z}.txt') as json_file:
                data2 = json.load(json_file)

                i = 0
                for x in data2['vehicle_journeys']:

                    j = 0
                    for y in data2['vehicle_journeys'][i]['stop_times']:

                        date = yesterday
                        begin = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['begin']
                        end = data2['vehicle_journeys'][i]['calendars'][0]['active_periods'][0]['end']
                        # week_pattern = data2['vehicle_journeys'][i]['calendars'][0]['week_pattern'] # garde just true
                        id = data2['vehicle_journeys'][i]['id']
                        name = data2['vehicle_journeys'][i]['name'] # = headsign

                        value = j
                        arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['arrival_time']
                        departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['departure_time']
                        drop_off_allowed = data2['vehicle_journeys'][i]['stop_times'][j]['drop_off_allowed']
                        headsign = data2['vehicle_journeys'][i]['stop_times'][j]['headsign']
                        pickup_allowed = data2['vehicle_journeys'][i]['stop_times'][j]['pickup_allowed']
                        skipped_stop = data2['vehicle_journeys'][i]['stop_times'][j]['skipped_stop']
                        lat = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lat']
                        lon = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['coord']['lon']
                        id_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['id']
                        label_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['label']
                        name_stop_point = data2['vehicle_journeys'][i]['stop_times'][j]['stop_point']['name']
                        utc_arrival_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_arrival_time']
                        utc_departure_time = data2['vehicle_journeys'][i]['stop_times'][j]['utc_departure_time']

                        trip_id = data2['vehicle_journeys'][i]['trip']['id']
                        trip_name = data2['vehicle_journeys'][i]['trip']['name']

                        return [date, begin, end, id, name, trip_id, trip_name],[date, begin, end, value, arrival_time, departure_time, drop_off_allowed, headsign, pickup_allowed, skipped_stop, lat, lon, id_stop_point, label_stop_point, name_stop_point, utc_arrival_time, utc_departure_time]

                        j += 1
                    i += 1


    def routes(self):

        result = how_many_files(2)
        for z in range(result):

            with open(f'{self.yesterday}/Routes/Routes{z}.txt') as json_file:
                data3 = json.load(json_file)

                i = 0
                for x in data3['routes']:

                    embedded_type = data3['routes'][i]['direction']['embedded_type']
                    id_direction = data3['routes'][i]['direction']['id']
                    name_direction = data3['routes'][i]['direction']['name']
                    quality = data3['routes'][i]['direction']['quality'] # utile ?
                    value = data3['routes'][i]['direction']['stop_area']['codes'][0]['value']
                    lat = data3['routes'][i]['direction']['stop_area']['coord']['lat']
                    lon = data3['routes'][i]['direction']['stop_area']['coord']['lon']
                    id_stop_area = data3['routes'][i]['direction']['stop_area']['id']
                    label_stop_area = data3['routes'][i]['direction']['stop_area']['label']
                    name_stop_area = data3['routes'][i]['direction']['stop_area']['name']
                    direction_type = data3['routes'][i]['direction_type']
                    id = data3['routes'][i]['id']
                    is_frequence = data3['routes'][i]['is_frequence']
                    closing_time = data3['routes'][i]['line']['closing_time']
                    id_commercial_mode = data3['routes'][i]['line']['commercial_mode']['id']
                    name_commercial_mode = data3['routes'][i]['line']['commercial_mode']['name']
                    id_line = data3['routes'][i]['line']['id']
                    id_name = data3['routes'][i]['line']['name']
                    opening_time = data3['routes'][i]['line']['opening_time']
                    id_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['id']
                    name_physical_modes = data3['routes'][i]['line']['physical_modes'][0]['name']
                    name = data3['routes'][i]['name']
                    i += 1

                    return [embedded_type, id_direction, name_direction, quality, value, lat, lon, id_stop_area, label_stop_area, name_stop_area, direction_type, id, is_frequence, closing_time, id_commercial_mode, name_commercial_mode, id_line, id_name, opening_time, id_physical_modes, name_physical_modes, name]


#Sort().disruptions()
#Sort().vehicle_journey()
#Sort().routes()

