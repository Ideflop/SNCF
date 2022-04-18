#! /usr/bin/python3

import json

with open('2022-04-17.txt') as json_file:
    data = json.load(json_file)
    a = data["vehicle"]
    b = data["stop_times"]
    c = data["disruptions"]
    d = data["%_vehicle"]
    e = data["impacted_stop"]
    f = data["%_stop_times"]
    g = data["routes"]
    h = data["disruptions_message"]['data0']        # loop through the data
    i = data["disruptions_message"]['value0']       # loop through the data
    j = data["citi_impacted"]['data0']              # loop through the data
    k = data["citi_impacted"]['value0']             # loop through the data
    l = data["citi_time_impacted"]['data0']         # loop through the data
    m = data["citi_time_impacted"]['value0']        # loop through the data 
    n = data["citi_time_impacted_tot"]
    o = data["disruptions_severity_name"]['data0']  # loop through the data
    p = data["disruptions_severity_name"]['value0'] # loop through the data

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
