import mysql.connector 
import extract

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="SNCF"
)

print(mydb) 

class Create():

    def __init__(self):
        self.mycursor = mydb.cursor()
        
    def table(self):

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
            sql = "CREATE TABLE routes (date DATE, embedded_type VARCHAR(255), direction_id VARCHAR(255), start_name VARCHAR(255), quality INT, stop_area INT, lat FLOAT, lon FLOAT, label VARCHAR(255), name VARCHAR(255), direction_type VARCHAR(255), id VARCHAR(255), is_frequence VARCHAR(255), closing_time TIME, commercial_mode_id VARCHAR(255), commercial_mode_name VARCHAR(255), line_id VARCHAR(255), line_name VARCHAR(255), opening_time TIME, physical_modes_id VARCHAR(255), stop_name VARCHAR(255), routes_name VARCHAR(255))"
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


    def disruptions(self):
        result = extract.Sort().how_many_files(0)
        
        for z in range(result-1):
            i = 0
            data = extract.Sort().which_data(z)
            for x in data['disruptions']:
                j = 0
                for y in data['disruptions'][i]['impacted_objects']:
                    disruption, impacted_object = extract.Sort().disruptions(z,i,j)
                    for a in range(len(self.one)):
                        if self.one[a] == 'date':
                            sql = f"INSERT INTO disruptions (date) VALUES (str_to_date('{disruption[a]}','%Y-%m-%d'))"
                        elif disruption[a] == 'NULL':
                            sql = f"INSERT INTO disruptions ({self.one[a]}) VALUES ({disruption[a]})"
                        else:
                            sql = f'INSERT INTO disruptions ({self.one[a]}) VALUES ("{disruption[a]}")'
                        #print(self.one[a])
                        self.mycursor.execute(sql)
                        mydb.commit()
                    for b in range(len(self.two)):
                        if self.two[b] == 'date':
                            sql = f"INSERT INTO impacted_object ({self.two[b]}) VALUES (str_to_date('{impacted_object[b]}','%Y-%m-%d'))"
                        elif impacted_object[b] == 'NULL':
                            sql = f"INSERT INTO impacted_object ({self.two[b]}) VALUES ({impacted_object[b]})"
                        else:
                            sql = f'INSERT INTO impacted_object ({self.two[b]}) VALUES ("{impacted_object[b]}")'
                        #print(self.two[b])
                        self.mycursor.execute(sql)
                        mydb.commit()
                    j += 1
                    print(j)
                i += 1
            #print('Page: ',z)
        
    def vehicle_journey(self):
        result = extract.Sort().how_many_files(1)

        for z in range(result-1):
            i=0
            data = extract.Sort().which_data(z)
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

    def routes(self):
        result = extract.Sort().how_many_files(1)

        for z in range(result-1):
            i=0
            data = extract.Sort().which_data(z)
            for x in data['vehicle_journeys']:
                routes = extract.Sort().routes(z,i,j)
                for a in range(len(self.five)):
                    if self.five[a] == 'data':
                        sql = f"INSERT INTO routes ({self.five[a]}) VALUES (str_to_date('{routes[a]}','%Y-%m-%d'))"
                    elif disruption[a] == 'NULL':
                            sql = f"INSERT INTO disruptions ({self.five[a]}) VALUES ({routes[a]})"
                    else:
                        sql = f'INSERT INTO routes ({self.five[a]}) VALUES ("{routes[a]}")'
                    self.mycursor.execute(sql)
                    mydb.commit()
                i += 1


#Create().table()
Insert().disruptions()
#Insert().vehicle_journey()
#Insert().routes()
