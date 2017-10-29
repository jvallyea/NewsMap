import os
import csv
import urllib
import zipfile
import sys
import json

# Defines the paramters that will be user-inputed on the website
# for the year, month, day, and hour range in the form start-finish

year = "2017"
month = "09"
day = "15"
hour_range = "3-6"
hour_range = hour_range.split("-")
hour_range = range(int(hour_range[0]),int(hour_range[1]))
minute_range = ["00","15","30","45"]

# Defines the company name to be searched
company = "Microsoft"

# Creates empty latitude and longitude arrays
latitude_array = []
longitude_array = []
tone_array = []

# Downloads each time data file, and extracts the longitude and latitude data
# Prints the data to a CSV file

for hour in hour_range:
    hour = str(hour)
    if len(hour) == 1:
        hour = "0" + hour
    for minute in minute_range:
        URLpath = "http://data.gdeltproject.org/gdeltv2/" + year + month + day + hour + minute + "00" + ".gkg.csv.zip"
        localDestination = "Datasets/" + hour + minute + ".gkg.csv.zip"
        resultFilePath, responseHeaders = urllib.urlretrieve(URLpath, localDestination)
        zip_ref = zipfile.ZipFile(resultFilePath, 'r')
        zip_ref.extractall("Datasets/")
        zip_ref.close()
        os.remove("Datasets/" + hour + minute + ".gkg.csv.zip")

        filename = "Datasets/" + year + month + day + hour + minute + "00.gkg.csv"
        f = open(filename)
        x = 0
        while x==0:
            try:
                row = f.readline()
                if company in row.split("\t")[13] or company in row.split("\t")[14]:
                    for item in row.split("\t")[9].split(";"):
                        print "success"
                        latitude_array.append(item.split("#")[4])
                        longitude_array.append(item.split("#")[5])
                        tone_array.append(int(float(row.split("\t")[15].split(",")[0])))
                    for item in row.split("\t")[10].split(";"):
                        print "success"
                        latitude_array.append(item.split(",")[1].split("#")[4])
                        longitude_array.append(item.split(",")[1].split("#")[5])
                        tone_array.append(int(float(row.split("\t")[15].split(",")[0])))
            except:
                print latitude_array
                x=1

data = {}
data['features'] = []
for i in range(len(latitude_array)):
    add_on = {}
    add_on['type'] = "Feature"
    add_on["properties"] = {}
    add_on["properties"]["tone"] = (int(tone_array[i]))
    add_on["geometry"] = {}
    add_on["geometry"]["coordinates"] = []
    add_on["geometry"]["coordinates"].append(float(longitude_array[i]))
    add_on["geometry"]["coordinates"].append(float(latitude_array[i]))
    add_on["geometry"]["type"] = "Point"
    add_on["id"] = str(i)
    data['features'].append(add_on)
data["type"] = "FeatureCollection"

print data
with open("test.geojson", 'w') as outfile:
    json.dump(data, outfile)

# with open("dynamic.csv", 'wb') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     text = "Latitude","Longitude"
#     writer.writerow(text)
#     column_array = range(len(latitude_array))
#     for i in column_array:
#         text = latitude_array[i],longitude_array[i]
#         writer.writerow(text)
