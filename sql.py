import mysql.connector 
import extract

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="SNCF"
)

print(mydb) 

class Create():

    def table(self):

        mycursor = mydb.cursor()
        try:
            sql = "CREATE TABLE disruptions (date DATE, begin TIME, end TIME, id VARCHAR(255), message VARCHAR(255), severity_effect VARCHAR(255), severity_name VARCHAR(255), trip_id INT, trip_name INT)"
            mycursor.execute(sql)
        except:
            pass 
        try:# begin et end
            sql = "CREATE TABLE impacted_object (date DATE, begin TIME, end TIME, value INT, amended_arrival_time TIME, amended_departure_time TIME, arrival_status VARCHAR(255), base_arrival_time TIME, base_departure_time TIME, departure_status VARCHAR(255), cause VARCHAR(255), is_detour VARCHAR(255), lat FLOAT, lon FLOAT, id VARCHAR(255), label VARCHAR(255), name VARCHAR(255), stop_time_effect VARCHAR(255))"
            mycursor.execute(sql)
        except:
            pass
        try:# week_pattern
            sql = "CREATE TABLE vehicle_journeys (date DATE, begin DATE, end DATE, headsign INT, id VARCHAR(255), name INT, trip_id VARCHAR(255), trip_name INT)"
            mycursor.execute(sql)
        except:
            pass
        try:
            sql = "CREATE TABLE stop_times (date DATE, begin TIME, end TIME, value INT, arrival_time TIME, departure_time TIME, drop_off_allowed VARCHAR(255), headsign INT, pickup_allowed VARCHAR(255), skipped_stop VARCHAR(255), lat FLOAT, lon FLOAT, id VARCHAR(255), label VARCHAR(255), name VARCHAR(255), utc_arrival_time TIME, utc_departure_time TIME)"
            mycursor.execute(sql)
        except:
            pass

        try:
            sql = "CREATE TABLE routes (embedded_type VARCHAR(255), direction_id VARCHAR(255), start_name VARCHAR(255), quality INT, stop_area INT, lat FLOAT, lon FLOAT, label VARCHAR(255), name VARCHAR(255), direction_type VARCHAR(255), id VARCHAR(255), is_frequence VARCHAR(255), closing_time TIME, commercial_mode_id VARCHAR(255), commercial_mode_name VARCHAR(255), line_id VARCHAR(255), line_name VARCHAR(255), opening_time TIME, physical_modes_id VARCHAR(255), stop_name VARCHAR(255), routes_name VARCHAR(255))"
            mycursor.execute(sql)
        except:
            pass

class Insert():

    def disruptions(self):
        pass

    def vehicle_journey(self):
        pass

    def routes(self):
        pass

Create().table()
