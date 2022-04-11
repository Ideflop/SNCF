#! /usr/bin/python3

import mysql.connector
import datetime


mydb = mysql.connector.connect( # connect to database
    host="127.0.0.1",
    user="root",
    database="SNCF"
)

class clean:
    def __init__(self):
        self.mydb = mydb
        self.mycursor = mydb.cursor()
        
        self.today = datetime.date.today()
        #self.yesterday = self.today - datetime.timedelta(days = 1)
        self.yesterday = '2022-03-24'
        self.yesterday = str(self.yesterday).replace('-', '_')
        
        self.disruption_list = ['value', 'date', 'begin', 'end', 'id', 'message', 'severity_effect', 'severity_name', 'trip_id', 'trip_name']
        self.impacted_object_list = ['date', 'begin', 'end', 'amended_arrival_time', 'amended_departure_time', 'departure_status', 'base_arrival_time', 'base_departure_time', 'arrival_status', 'cause', 'is_detour', 'id_impacted_stop', 'label_impacted_stop', 'name_impacted_stop', 'stop_time_effect']
        self.vehicle_journey_list = ['value', 'date', 'begin', 'end', 'headsign', 'id', 'name', 'trip_id', 'trip_name']
        self.routes_list = ['date', 'embedded_type', 'id_direction', 'name_direction', 'quality', 'value', 'lat', 'lon', 'id_stop_area', 'label_stop_area', 'name_stop_area', 'direction_type', 'id', 'is_frequence', 'closing_time', 'id_commercial_mode', 'name_commercial_mode', 'id_line', 'id_name', 'opening_time', 'id_physical_modes', 'name_physical_modes', 'routes_name']
        
        self.impacted_object_list1 = ['departure_status','arrival_status', 'cause', 'is_detour', 'id_impacted_stop', 'label_impacted_stop', 'name_impacted_stop', 'stop_time_effect']
        self.impacted_object_list2 = ['lat', 'lon']
        self.impacted_object_list3 = ['amended_arrival_time', 'amended_departure_time', 'base_arrival_time', 'base_departure_time']
        self.stop_times_list = ['date', 'begin', 'end', 'arrival_time', 'departure_time', 'drop_off_allowed', 'headsign_stop', 'pickup_allowed', 'skipped_stop', 'lat', 'lon', 'id_stop_point', 'label_stop_point', 'name_stop_point', 'utc_arrival_time', 'utc_departure_time']
        self.stop_times_list1 = ['drop_off_allowed', 'headsign_stop', 'pickup_allowed', 'skipped_stop', 'id_stop_point', 'label_stop_point', 'name_stop_point']
        self.stop_times_list2 = ['lat', 'lon']
        self.stop_times_list3 = ['arrival_time', 'departure_time', 'utc_arrival_time', 'utc_departure_time']
    
    def clean_data(self):

        sql = f"UPDATE disruptions_{self.yesterday} SET message = NULL WHERE message = 'zzz'"
        self.mycursor.execute(sql)
        self.mydb.commit()

        for i in self.impacted_object_list1:
            sql = f"UPDATE impacted_object_{self.yesterday} SET {i} = NULL WHERE {i} = 'zzz'"
            self.mycursor.execute(sql)
            self.mydb.commit()

        for i in self.impacted_object_list2:
            sql = f"UPDATE impacted_object_{self.yesterday} SET {i} = NULL WHERE {i} = '0'"
            self.mycursor.execute(sql)
            self.mydb.commit()
        
        sql = f"UPDATE impacted_object_{self.yesterday} SET cause = NULL WHERE cause = ''"
        self.mycursor.execute(sql)
        self.mydb.commit()
        
        for i in self.impacted_object_list3:
            sql = f"UPDATE impacted_object_{self.yesterday} SET {i} = NULL WHERE {i} = '00:00:00'"
            self.mycursor.execute(sql)
            self.mydb.commit()
        
        for i in self.stop_times_list1:
            sql = f"UPDATE stop_times_{self.yesterday} SET {i} = NULL WHERE {i} = 'zzz'"
            self.mycursor.execute(sql)
            self.mydb.commit()

        for i in self.stop_times_list2:
            sql = f"UPDATE stop_times_{self.yesterday} SET {i} = NULL WHERE {i} = '0'"
            self.mycursor.execute(sql)
            self.mydb.commit()
        
        for i in self.stop_times_list3:
            sql = f"UPDATE stop_times_{self.yesterday} SET {i} = NULL WHERE {i} = '00:00:00'"
            self.mycursor.execute(sql)
            self.mydb.commit()

        sql = f"UPDATE stop_times_{self.yesterday} SET headsign_stop = NULL WHERE headsign_stop = '00'"
        self.mycursor.execute(sql)
        self.mydb.commit()









clean().clean_data()