#!/usr/bin/env python3

import json
import datetime
import pytz
import dateutil
import dateutil.parser
from operator import itemgetter
from collections import OrderedDict

# read NASA datas
with open('nasa-datas.json', 'r') as j:
	nasaevents = json.load(j)


for nasaevent in nasaevents:
	if "year" in nasaevent and "mass" in nasaevent and "geolocation" in nasaevent:
		milliseconds_since_epoch = int(datetime.datetime(int(nasaevent['year'].split("-", 1)[0]), 1, 1).timestamp() * 1000)
		nasaevent['time'] = milliseconds_since_epoch
		nasaevent['lat'] = nasaevent['geolocation']['latitude']	
		nasaevent['lng'] = nasaevent['geolocation']['longitude']	
		nasaevent['mag'] = nasaevent['mass']	
		nasaevent['year'] = nasaevent['year'].split("-", 1)[0]
	else:
		nasaevents.remove(nasaevent)

# sort by year 
nasaevents.sort(key=lambda x: x.get('year'))
output_json = json.dumps(nasaevents)
print(output_json)
