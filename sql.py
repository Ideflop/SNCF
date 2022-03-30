#! /usr/bin/python3

import mysql.connector 
import extract

mydb = mysql.connector.connect( # connect to database
    host="127.0.0.1",
    user="root",
    database="SNCF"
)

print(mydb) 

class Create():

    def __init__(self):
        self.mycursor = mydb.cursor()
        
    def table(self): # create sql table if not exist 

        try:
            sql = "CREATE TABLE disruptions (date DATE, begin TIME, end TIME, id VARCHAR(255), message TEXT, severity_effect VARCHAR(255), severity_name VARCHAR(255), trip_id VARCHAR(255) , trip_name INT)"
            self.mycursor.execute(sql)
        except:
            pass 
        try:# begin et end
            sql = "CREATE TABLE impacted_object (date DATE, begin TIME, end TIME, value INT, amended_arrival_time TIME, amended_departure_time TIME, arrival_status VARCHAR(255), base_arrival_time TIME, base_departure_time TIME, departure_status VARCHAR(255), cause VARCHAR(255), is_detour VARCHAR(255), lat FLOAT, lon FLOAT, id_impacted_stop VARCHAR(255), label_impacted_stop VARCHAR(255), name_impacted_stop VARCHAR(255), stop_time_effect VARCHAR(255))"
            self.mycursor.execute(sql)
        except:
            pass
        try:# week_pattern
            sql = "CREATE TABLE vehicle_journeys (date DATE, begin TIME, end TIME, headsign INT, id VARCHAR(255), name INT, trip_id VARCHAR(255), trip_name INT)"
            self.mycursor.execute(sql)
        except:
            pass
        try:
            sql = "CREATE TABLE stop_times (date DATE, begin TIME, end TIME, value INT, arrival_time TIME, departure_time TIME, drop_off_allowed VARCHAR(255), headsign INT, pickup_allowed VARCHAR(255), skipped_stop VARCHAR(255), lat FLOAT, lon FLOAT, id VARCHAR(255), label VARCHAR(255), name VARCHAR(255), utc_arrival_time TIME, utc_departure_time TIME)"
            self.mycursor.execute(sql)
        except:
            pass

        try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            sql = "CREATE TABLE routes (date DATE, embedded_type VARCHAR(255), id_direction VARCHAR(255), name_direction VARCHAR(255), quality INT, value TEXT, id_stop_area TEXT, lat FLOAT, lon FLOAT, label_stop_area VARCHAR(255), name_stop_area VARCHAR(255), direction_type VARCHAR(255), id VARCHAR(255), is_frequence VARCHAR(255), closing_time TIME, id_commercial_mode VARCHAR(255), name_commercial_mode VARCHAR(255), id_line VARCHAR(255), id_name VARCHAR(255), opening_time TIME, id_physical_modes VARCHAR(255), name_physical_modes VARCHAR(255), routes_name VARCHAR(255))"
            self.mycursor.execute(sql)
        except:
            pass


class Insert():

    def __init__(self):
        self.mycursor = mydb.cursor()
        self.one = ['date', 'begin', 'end', 'id', 'message', 'severity_effect',' severity_name', 'trip_id', 'trip_name']
        self.two = ['date', 'begin', 'end', 'value', 'amended_arrival_time', 'amended_departure_time', 'departure_status', 'base_arrival_time', 'base_departure_time', 'arrival_status', 'cause', 'is_detour', 'lat', 'lon', 'id_impacted_stop', 'label_impacted_stop', 'name_impacted_stop', 'stop_time_effect']
        self.three = ['date', 'begin', 'end', 'id', 'name', 'trip_id', 'trip_name']
        self.four = ['date', 'begin', 'end', 'value', 'arrival_time', 'departure_time', 'drop_off_allowed', 'headsign', 'pickup_allowed', 'skipped_stop', 'lat', 'lon', 'id_stop_point', 'label_stop_point', 'name_stop_point', 'utc_arrival_time', 'utc_departure_time']


    def disruptions(self): # insert disruptions
        result = extract.Sort().how_many_files(0)
        
        for z in range(result):
            i = 0
            data = extract.Sort().which_data(z,1)
            for x in data['disruptions']:

                for y in data['disruptions'][i]['impacted_objects']:
                    j=0
                    disruption, impacted_object = extract.Sort().disruptions(z,i,j)

                    sql = "INSERT INTO disruptions (date, begin, end, id, message, severity_effect, severity_name, trip_id, trip_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (disruption[0], disruption[1], disruption[2], disruption[3], disruption[4], disruption[5], disruption[6], disruption[7], disruption[8])
                    self.mycursor.execute(sql,val)
                    mydb.commit()
                    
                    sql = "INSERT INTO impacted_object (date, begin, end, value, amended_arrival_time, amended_departure_time, departure_status, base_arrival_time, base_departure_time, arrival_status, cause, is_detour, lat, lon, id_impacted_stop, label_impacted_stop, name_impacted_stop, stop_time_effect) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (impacted_object[0], impacted_object[1], impacted_object[2], impacted_object[3], impacted_object[4], impacted_object[5], impacted_object[6], impacted_object[7], impacted_object[8], impacted_object[9], impacted_object[10], impacted_object[11], impacted_object[12], impacted_object[13], impacted_object[14], impacted_object[15], impacted_object[16], impacted_object[17])
                    self.mycursor.execute(sql,val)
                    mydb.commit()
                    try:
                        f = 1
                        for w in data['disruptions'][i]['impacted_objects'][0]['impacted_stops'][f]:
                            disruption, impacted_object = extract.Sort().disruptions(z,i,j)
                            sql = "INSERT INTO impacted_object (date, begin, end, value, amended_arrival_time, amended_departure_time, departure_status, base_arrival_time, base_departure_time, arrival_status, cause, is_detour, lat, lon, id_impacted_stop, label_impacted_stop, name_impacted_stop, stop_time_effect) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val = (impacted_object[0], impacted_object[1], impacted_object[2], impacted_object[3], impacted_object[4], impacted_object[5], impacted_object[6], impacted_object[7], impacted_object[8], impacted_object[9], impacted_object[10], impacted_object[11], impacted_object[12], impacted_object[13], impacted_object[14], impacted_object[15], impacted_object[16], impacted_object[17])
                            self.mycursor.execute(sql,val)
                            mydb.commit()
                            f += 1
                    except:
                        pass
                    j+=1
                i += 1
            #print('Page: ',z)
        
    def vehicle_journey(self): # insert vehicle_journey
        result = extract.Sort().how_many_files(1)

        for z in range(result-1):
            i=0
            data = extract.Sort().which_data(z,1)
            for x in data['vehicle_journeys']:
                j = 0
                for y in data['vehicle_journeys'][i]['calendars']:
                    vehicle_journey, stop_times = extract.Sort().vehicle_journey(z,i,j)
                    for a in range(len(self.three)):
                        if self.three[a] == 'data':
                            sql = f"INSERT INTO vehicle_journey ({self.three[a]}) VALUES (str_to_date('{vehicle_journey[a]}','%Y-%m-%d'))"
                        elif disruption[a] == 'NULL':
                            sql = f"INSERT INTO disruptions ({self.three[a]}) VALUES ({vehicle_journey[a]})"
                        else:
                            sql = f'INSERT INTO vehicle_journey ({self.three[a]}) VALUES ("{vehicle_journey[a]}")'
                        self.mycursor.execute(sql)
                        mydb.commit()
                    for b in range(len(self.four)):
                        if self.four[b] == 'data':
                            sql = f"INSERT INTO stop_times ({self.four[b]}) VALUES (str_to_date('{stop_times[b]}','%Y-%m-%d'))"
                        elif disruption[a] == 'NULL':
                            sql = f"INSERT INTO disruptions ({self.four[b]}) VALUES ({stop_times[b]})"
                        else:
                            sql = f'INSERT INTO stop_times ({self.four[b]}) VALUES ("{stop_times[b]}")'
                        self.mycursor.execute(sql)
                        mydb.commit()
                    j += 1
                i += 1

    def routes(self): # insert routes
        result = extract.Sort().how_many_files(2)

        for z in range(result):
            i=0
            data = extract.Sort().which_data(z,2)
            for x in data['routes']:
                routes = extract.Sort().routes(z,i)
                sql = "INSERT INTO routes (date, embedded_type, id_direction, name_direction, quality, value, lat, lon, id_stop_area, label_stop_area, name_stop_area, direction_type, id, is_frequence, closing_time, id_commercial_mode, name_commercial_mode, id_line, id_name, opening_time, id_physical_modes, name_physical_modes, routes_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"             
                val = (routes[0], routes[1], routes[2], routes[3], routes[4], routes[5], routes[6], routes[7], routes[8], routes[9], routes[10], routes[11], routes[12], routes[13], routes[14], routes[15], routes[16], routes[17], routes[18], routes[19], routes[20], routes[21], routes[22])
                self.mycursor.execute(sql,val)
                mydb.commit()
                i += 1

Create().table()
#Insert().disruptions()
#Insert().vehicle_journey()
Insert().routes()
