import json

with open('2022-03-13/Page/Page24.txt') as json_file:
    data = json.load(json_file)
    
print(data["disruptions"][0]['application_periods'][0]['begin'])
print(data["disruptions"][0]['application_periods'][0]['end'])
print(data["disruptions"][0]['id'])

print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['amended_arrival_time'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['amended_departure_time'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['arrival_status'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['base_arrival_time'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['base_departure_time'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['cause'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['departure_status'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['is_detour'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['stop_point']['coord']['lat'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['stop_point']['coord']['lon'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['stop_point']['id'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['stop_point']['name'])
print(data["disruptions"][0]['impacted_objects'][0]['impacted_stops'][0]['stop_time_effect'])

print(data["disruptions"][0]['impacted_objects'][0]['pt_object']['trip']['id'])
print(data["disruptions"][0]['impacted_objects'][0]['pt_object']['trip']['name'])
print(data["disruptions"][0]['messages'][0]['text'])
print(data["disruptions"][0]['severity']['effect'])
print(data["disruptions"][0]['severity']['name'])

print('')
print('-----------------------------')
'''
label ?
'''


with open('2022-03-13/Vehicle_journey/Vehicle_journey0.txt') as json_file:
    data2 = json.load(json_file)

print(data2['vehicle_journeys'][0]['calendars'][0]['active_periods'][0]['begin'])
print(data2['vehicle_journeys'][0]['calendars'][0]['active_periods'][0]['end'])
print(data2['vehicle_journeys'][0]['calendars'][0]['week_pattern']) # garde just true
print(data2['vehicle_journeys'][0]['id'])
print(data2['vehicle_journeys'][0]['name'])

print(data2['vehicle_journeys'][0]['stop_times'][0]['arrival_time'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['departure_time'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['drop_off_allowed'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['headsign'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['pickup_allowed'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['skipped_stop'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['stop_point']['coord']['lat'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['stop_point']['coord']['lon'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['stop_point']['id'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['stop_point']['name'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['utc_arrival_time'])
print(data2['vehicle_journeys'][0]['stop_times'][0]['utc_departure_time'])

print(data2['vehicle_journeys'][0]['trip']['id'])
print(data2['vehicle_journeys'][0]['trip']['name'])

print('')
print('-----------------------------')
'''
prendre quelque chose pour les codes ?
label ?
'''

with open('2022-03-13/Routes/Routes0.txt') as json_file:
    data3 = json.load(json_file)

print(data3['routes'][0]['direction']['embedded_type'])
print(data3['routes'][0]['direction']['id'])
print(data3['routes'][0]['direction']['name'])
print(data3['routes'][0]['direction']['quality']) # utile ? 
print(data3['routes'][0]['direction']['stop_area']['codes'][0]['value'])
print(data3['routes'][0]['direction']['stop_area']['coord']['lat'])
print(data3['routes'][0]['direction']['stop_area']['coord']['lon'])
print(data3['routes'][0]['direction']['stop_area']['id'])
print(data3['routes'][0]['direction']['stop_area']['name'])
print(data3['routes'][0]['direction_type'])
print(data3['routes'][0]['id'])
print(data3['routes'][0]['is_frequence'])
print(data3['routes'][0]['line']['id'])
print(data3['routes'][0]['line']['name'])
print(data3['routes'][0]['line']['opening_time'])
print(data3['routes'][0]['line']['physical_modes'][0]['id'])
print(data3['routes'][0]['line']['physical_modes'][0]['name'])
print(data3['routes'][0]['name'])


print('')
print('-----------------------------')

'''
label ?
closing time ?
'''
