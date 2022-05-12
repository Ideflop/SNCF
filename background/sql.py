#! /usr/bin/python3


import mysql.connector 
import extract
import datetime


mydb = mysql.connector.connect( # connect to database
    host="127.0.0.1",
    user="root",
    password="1234",
    auth_plugin='mysql_native_password',
    database="SNCF"
)

print(mydb)

class Init():
    def __init__(self):
        self.mydb = mydb
        self.mycursor = mydb.cursor()
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        #self.yesterday = '2022-04-30'
        self.yesterday = str(self.yesterday).replace('-', '_')
        self.mycursor.execute("USE {}".format("SNCF"))

class Create(Init):
        
    def table(self): # create sql table if not exist 

        try:
            sql = f"CREATE TABLE disruptions_{self.yesterday} (begin TIME, end TIME, id VARCHAR(255), message TEXT, severity_name VARCHAR(255), trip_id VARCHAR(255) , trip_name VARCHAR(255), PRIMARY KEY (id))"
            self.mycursor.execute(sql)
        except:
            pass 
        try:        
            sql = f"CREATE TABLE impacted_object_{self.yesterday} (Trainid int NOT NULL AUTO_INCREMENT,amended_arrival_time TIME, amended_departure_time TIME, arrival_status VARCHAR(255), base_arrival_time TIME, base_departure_time TIME, departure_status VARCHAR(255), cause VARCHAR(255), lat FLOAT, lon FLOAT, id_impacted_stop VARCHAR(255), name_impacted_stop VARCHAR(255), trip_name VARCHAR(255),PRIMARY KEY (Trainid))"
            self.mycursor.execute(sql)
        except:
            pass
        try:                                           
            sql = f"CREATE TABLE vehicle_journeys_{self.yesterday} (begin DATE, end DATE, headsign VARCHAR(255), id VARCHAR(255), trip_id VARCHAR(255),PRIMARY KEY (id))"
            self.mycursor.execute(sql)
        except:
            pass
        try:
            sql = f"CREATE TABLE stop_times_{self.yesterday} (Trainid int NOT NULL AUTO_INCREMENT, arrival_time TIME, departure_time TIME, headsign_stop VARCHAR(255), lat FLOAT, lon FLOAT, id_stop_point VARCHAR(255), name_stop_point VARCHAR(255), utc_arrival_time TIME, utc_departure_time TIME, PRIMARY KEY (Trainid))"
            self.mycursor.execute(sql)
        except:
            pass
        try:
            sql = f"CREATE TABLE routes_{self.yesterday} (Trainid int NOT NULL AUTO_INCREMENT, id_direction VARCHAR(255), value varchar(255), id_stop_area TEXT, lat FLOAT, lon FLOAT, name_stop_area VARCHAR(255), closing_time TIME, id_commercial_mode VARCHAR(255), name_commercial_mode VARCHAR(255), opening_time TIME, id_physical_modes VARCHAR(255), name_physical_modes VARCHAR(255), routes_name VARCHAR(255),PRIMARY KEY (Trainid))"
            self.mycursor.execute(sql)
        except:
            pass

        print("Table created successfully")


class Insert(Init):

    def disruptions(self): # insert disruptions
        result = extract.Sort().how_many_files(0)
        
        for z in range(result):
            i = 0
            data = extract.Sort().which_data(z,0)
            for x in data['disruptions']:
                for y in data['disruptions'][i]['impacted_objects']:
                    j=0
                    disruption, impacted_object = extract.Sort().disruptions(z,i,j)

                    sql = f"INSERT INTO disruptions_{self.yesterday} (begin, end, id, message, severity_name, trip_id, trip_name) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    val = (disruption[0], disruption[1], disruption[2], disruption[3], disruption[4], disruption[5], disruption[6])
                    self.mycursor.execute(sql,val)
                    
                    sql = f"INSERT INTO impacted_object_{self.yesterday} (amended_arrival_time, amended_departure_time, arrival_status, base_arrival_time, base_departure_time, departure_status, cause, lat, lon, id_impacted_stop, name_impacted_stop, trip_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (impacted_object[0], impacted_object[1], impacted_object[2], impacted_object[3], impacted_object[4], impacted_object[5], impacted_object[6], impacted_object[7], impacted_object[8], impacted_object[9], impacted_object[10], impacted_object[11])
                    self.mycursor.execute(sql,val)
                    
                    try:
                        f = 1
                        for w in data['disruptions'][i]['impacted_objects'][0]['impacted_stops'][f]:
                            disruption, impacted_object = extract.Sort().disruptions(z,i,f)
                            sql = f"INSERT INTO impacted_object_{self.yesterday} (amended_arrival_time, amended_departure_time, arrival_status, base_arrival_time, base_departure_time, departure_status, cause, lat, lon, id_impacted_stop, name_impacted_stop, trip_name) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val = (impacted_object[0], impacted_object[1], impacted_object[2], impacted_object[3], impacted_object[4], impacted_object[5], impacted_object[6], impacted_object[7], impacted_object[8], impacted_object[9], impacted_object[10], impacted_object[11])
                            self.mycursor.execute(sql,val)
                            f += 1
                    except:
                        pass
                    j+=1
                i += 1
        self.mydb.commit()
        print("Disruptions and impacted_stop inserted successfully")

    def vehicle_journey(self): # insert vehicle_journey
        result = extract.Sort().how_many_files(1)

        for z in range(result):
            i=0
            j = 0
            data = extract.Sort().which_data(z,1)
            for x in data['vehicle_journeys']:
                vehicle_journey, stop_times = extract.Sort().vehicle_journey(z,i,j)

                sql = f"INSERT INTO vehicle_journeys_{self.yesterday} (begin, end, headsign, id, trip_id) VALUES (%s,%s,%s,%s,%s)"
                val = (vehicle_journey[0], vehicle_journey[1], vehicle_journey[2], vehicle_journey[3], vehicle_journey[4])
                self.mycursor.execute(sql,val)
                
                sql = f"INSERT INTO stop_times_{self.yesterday} (arrival_time, departure_time, headsign_stop, lat, lon, id_stop_point, name_stop_point, utc_arrival_time, utc_departure_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (stop_times[0], stop_times[1], stop_times[2], stop_times[3], stop_times[4], stop_times[5], stop_times[6], stop_times[7], stop_times[8])
                self.mycursor.execute(sql,val)
                
                try:
                    f=1
                    vehicle_journey, stop_times = extract.Sort().vehicle_journey(z,i,f)
                    for w in data['vehicle_journeys'][i]['stop_times']:
                        sql = f"INSERT INTO stop_times_{self.yesterday} (arrival_time, departure_time, headsign_stop, lat, lon, id_stop_point, name_stop_point, utc_arrival_time, utc_departure_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (stop_times[0], stop_times[1], stop_times[2], stop_times[3], stop_times[4], stop_times[5], stop_times[6], stop_times[7], stop_times[8])
                        self.mycursor.execute(sql,val)
                        f += 1
                        vehicle_journey, stop_times = extract.Sort().vehicle_journey(z,i,f)
                except:
                    pass
                i += 1
        self.mydb.commit()
        print("Vehicle_journey and stop_times inserted successfully")

    def routes(self): # insert routes
        result = extract.Sort().how_many_files(2)

        for z in range(result):
            i=0
            data = extract.Sort().which_data(z,2)
            for x in data['routes']:
                routes = extract.Sort().routes(z,i)
                sql = f"INSERT INTO routes_{self.yesterday} (id_direction, value, id_stop_area, lat, lon, name_stop_area, closing_time, id_commercial_mode, name_commercial_mode, opening_time, id_physical_modes, name_physical_modes, routes_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"             
                val = (routes[0], routes[1], routes[2], routes[3], routes[4], routes[5], routes[6], routes[7], routes[8], routes[9], routes[10], routes[11], routes[12])
                self.mycursor.execute(sql,val)
                i += 1
        self.mydb.commit()
        print("Routes inserted successfully")

if '__main__' == __name__:
    Create().table()
    Insert().disruptions()
    Insert().vehicle_journey()
    Insert().routes()
