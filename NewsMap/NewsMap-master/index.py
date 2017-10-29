import os
import csv
import urllib.request 
import zipfile
import sys
from flask import Flask, request, render_template,request,url_for
import json

global count
count = 1
app = Flask(__name__)

@app.route("/")
def render():
	return render_template('layout.html')

@app.route("/generate_map", methods=['GET', 'POST'])
def generate_map():
	global count
	company = request.form['company']
	month = request.form['month']
	day = request.form['day']
	year = request.form['year']
	hour_range = request.form['time']
	generate_json(company, month, day, year, hour_range)
	n = count-1
	#url_for('static', filename ="%06d"%n+".geojson")
	temp_filename = url_for('static', filename ="%06d"%n+".geojson")
	print(temp_filename)
	
	return render_template('generate_map.html', filename = temp_filename)

@app.route("/map")
def map():
	return render_template('static_map.html')
@app.route("/static_goldman")
def map_static_goldman():
	return render_template('static_goldman.html')

@app.route("/static_huawei")
def map_static_huawei():
	return render_template('static_huawei.html')

@app.route("/static_bah")
def map_static_bah():
	return render_template('static_bah.html')

@app.route("/static_nasdaq")
def map_static_nasdaq():
	return render_template('static_nasdaq.html')

@app.route("/static_disney")
def map_static_disney():
	return render_template('static_disney.html')

@app.route("/description")
def descript():
	return render_template('description.html')

@app.route("/static_ibm")
def map_static_ibm():
	return render_template('static_ibm.html')

@app.route("/static_baidu")
def map_static_baidu():
	return render_template('static_baidu.html')

def generate_json(company, month, day, year, hour_range):
	global count
	year = year
	month = month
	day = day
	hour_range = hour_range
	hour_range = hour_range.split("-")
	hour_range = range(int(hour_range[0]),int(hour_range[1]))
	minute_range = ["00","15","30","45"]

	# Defines the company name to be searched
	company = company

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
			urllib.request.urlretrieve(URLpath, localDestination)
			try:
				zip_ref = zipfile.ZipFile(localDestination, 'r')
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
								print("success")
								latitude_array.append(item.split("#")[4])
								longitude_array.append(item.split("#")[5])
								tone_array.append(int(float(row.split("\t")[15].split(",")[0])))
							for item in row.split("\t")[10].split(";"):
								print("success")
								latitude_array.append(item.split(",")[1].split("#")[4])
								longitude_array.append(item.split(",")[1].split("#")[5])
								tone_array.append(int(float(row.split("\t")[15].split(",")[0])))
					except:
						print(latitude_array)
						x=1
			except:
				pass

	data = {}
	data['features'] = []
	for i in range(len(latitude_array)):
		try:
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
		except:
			pass
	data["type"] = "FeatureCollection"
	file_name = "static/%06d"%count+".geojson"
	print(file_name)
	with open(file_name, 'w') as outfile:
	    json.dump(data, outfile)
	count+=1

if __name__ == '__main__':
	app.run(debug = 1)

