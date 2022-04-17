#! /usr/bin/python3

import mysql.connector
import datetime
import json
import os   # for writing to file

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
        self.yesterday = self.today - datetime.timedelta(days = 1)
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


class write: # just here os
    def __init__(self):
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        self.mydb = mydb
        self.mycursor = mydb.cursor()
        if not os.path.exists(f"calculus/{self.yesterday}.txt"):
            open(f'calculus/{self.yesterday}', 'w').close()
        self.yesterday = str(self.yesterday).replace('-', '_')

    def write_data(self):
        # create a dictionary of the data
        data_dict = {}
        text, result = search.general(self)
        for i in range(len(result)):
            data_dict.update({text[i]:result[i]})
        print(data_dict)

    def write_to_file(self, data): # data must be dict

        with open(f'calculus/{self.yesterday}.txt', 'a') as f:
            json.dump(data, f)
        


class search:
    def __init__(self):
        self.mydb = mydb
        self.mycursor = mydb.cursor()
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        self.yesterday = str(self.yesterday).replace('-', '_')

    def general(self):
        text = ['vehicle', 'stop_times', 'disruptions', '%_vehicle', 'impacted_stop', '%_stop_times','routes']
        result = []
        # total vehicle journey
        self.mycursor.execute(f"SELECT COUNT(*) FROM vehicle_journeys_{self.yesterday}")
        result.append(self.mycursor.fetchone()[0])
        # total stop times
        self.mycursor.execute(f"SELECT COUNT(*) FROM stop_times_{self.yesterday}")
        result.append(self.mycursor.fetchone()[0])
        # total disruption
        self.mycursor.execute(f"SELECT COUNT(*) FROM disruptions_{self.yesterday}")
        result.append(self.mycursor.fetchone()[0])
        # in % of total vehicle journey
        result.append(round(result[2] * 100 / result[0],2))
        # total impacted object
        self.mycursor.execute(f"SELECT COUNT(*) FROM impacted_object_{self.yesterday}")
        result.append(self.mycursor.fetchone()[0])
        # in % of total stop times
        result.append(round(result[4] * 100 / result[1],2))
        # total routes
        self.mycursor.execute(f"SELECT COUNT(*) FROM routes_{self.yesterday}")
        result.append(self.mycursor.fetchone()[0])

        return text,result
        
    def disruptions_message(self):
        result = []
        message = []
        # search all message and number of time it appears
        self.mycursor.execute(f"SELECT message FROM disruptions_{self.yesterday}")
        for i in self.mycursor.fetchall():
            if i[0] in message:
                index = message.index(i[0])
                result[index] += 1
            else:
                message.append(i[0])
                result.append(1)
        

        if None in message:
            index = message.index(None)
            result.pop(index)
            message.pop(index)
        
        # return the 10 most common disruptions message
        top_result = []
        top_message = []
        for i in range(10):
            vmax_result = max(result)
            imax_result = result.index(vmax_result)
            vmax_message =  message[imax_result]
            top_result.append(vmax_result)
            top_message.append(vmax_message)
            result[imax_result] = 0
        
        return top_message, top_result

    def citi_impacted(self):
        result = []
        message = []
        # search all cities and number of time it appears
        self.mycursor.execute(f"SELECT name_impacted_stop FROM impacted_object_{self.yesterday}")
        for i in self.mycursor.fetchall():
            if i[0] in message:
                index = message.index(i[0])
                result[index] += 1
            else:
                message.append(i[0])
                result.append(1)

        if None in message:
            index = message.index(None)
            result.pop(index)
            message.pop(index)
        
        # return the 10 most commen impacted city by appearance
        top_result = []
        top_message = []
        for i in range(10):
            vmax_result = max(result)
            imax_result = result.index(vmax_result)
            vmax_message =  message[imax_result]
            top_result.append(vmax_result)
            top_message.append(vmax_message)
            result[imax_result] = 0
        
        return top_message, top_result

    def citi_time_impacted(self):
        station = []
        time = []

        # select base_arrival_time and base_departure_time and name_impacted_stop where departure_time is delayed
        self.mycursor.execute(f"SELECT base_arrival_time, base_departure_time, name_impacted_stop FROM impacted_object_{self.yesterday} WHERE departure_status = 'delayed' AND base_arrival_time IS NOT NULL AND base_departure_time IS NOT NULL")
        for i in self.mycursor.fetchall():
            if i[2] in station:
                index = station.index(i[2])
                time[index] += (i[1] -i[0]).seconds
            else:
                station.append(i[2])
                time.append((i[1] -i[0]).seconds)

        tot_time_impacted = sum(time)
        tot_time_impacted = datetime.timedelta(seconds = tot_time_impacted)
        tot_time_impacted = str(tot_time_impacted)

        # return the 10 most common impacted city by time
        top_station = []
        top_time = []
        for i in range(10):
            vmax_time = max(time)
            imax_time = time.index(vmax_time)
            vmax_station =  station[imax_time]
            top_time.append(vmax_time)
            top_station.append(vmax_station)
            time[imax_time] = 0
        
        for i in range(len(top_station)):
            conversion = datetime.timedelta(seconds = top_time[i])
            top_time[i] = str(conversion)

        return top_station, top_time, tot_time_impacted

    def disruptions_severity_name(self):
        message = []
        result = []

        # count all severity_name 
        self.mycursor.execute(f"SELECT severity_name FROM disruptions_{self.yesterday}")
        for i in self.mycursor.fetchall():
            if i[0] in message:
                index = message.index(i[0])
                result[index] += 1
            else:
                message.append(i[0])
                result.append(1)

        sort_message = []
        sort_result = []

        # sort the result by descending order

        for i in range(len(result)):
            vmax = max(result)
            index = result.index(vmax)
            sort_result.append(vmax)
            sort_message.append(message[index])
            result.pop(index)
            message.pop(index)

        return sort_message, sort_result

        
#clean().clean_data()
#print(search().general())
#print(search().disruptions_message())
#print(search().citi_impacted())
#print(search().citi_time_impacted())
#print(search().disruptions_severity_name())

print(write().write_data())
