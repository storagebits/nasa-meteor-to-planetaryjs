#!/usr/bin/env python3

import json
import datetime
import pytz
import dateutil
import dateutil.parser

# read NASA datas
with open('nasa-datas.json', 'r') as j:
	nasaevents = json.load(j)

for nasaevent in nasaevents:
	if "year" in nasaevent and "mass" in nasaevent and "geolocation" in nasaevent:
		#print("nasaevent:" + nasaevent['year'])
		# 1995-01-01T00:00:00.000
		#print(nasaevent['year'].split("-", 1)[0])
		
		t = "2016-05-24 11:30 PST"

		#datetime_object = datetime.strptime(nasaevent['year'].split("-", 1)[0], '%Y')
		#seconds_since_epoch = datetime.datetime.now().timestamp()
		#milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000
		milliseconds_since_epoch = str(datetime.datetime(int(nasaevent['year'].split("-", 1)[0]), 1, 1).timestamp() * 1000)
		nasaevent['time'] = milliseconds_since_epoch
		nasaevent['lat'] = nasaevent['geolocation']['latitude']	
		nasaevent['lng'] = nasaevent['geolocation']['longitude']	
		nasaevent['mag'] = nasaevent['mass']	
		#print(milliseconds_since_epoch)

#for nasaevent in nasaevents:
#	if "year" in nasaevent and "time" in nasaevent:
#		print("nasaevent:" + str(nasaevent['time']))
#		print("nasaevent:" + str(nasaevent['lat']))
#		print("nasaevent:" + str(nasaevent['lng']))

# order json
#nasaevents.sort(key = lambda x:x["time"])

output_json = json.dumps(nasaevents)
print(nasaevents)

