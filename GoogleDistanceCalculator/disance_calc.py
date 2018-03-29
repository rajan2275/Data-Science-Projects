import requests
import json
import os
from sys import platform
import pandas as pd


from urllib.parse import urlencode
from collections import OrderedDict
#https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyBOpfbJt97X-nUq76lbVyAnukrwKgFQDa4

# initial_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
# units='imperial'
# key='AIzaSyBOpfbJt97X-nUq76lbVyAnukrwKgFQDa4'
#
path = os.path.dirname(os.getcwd())

google_key = 'AIzaSyBOpfbJt97X-nUq76lbVyAnukrwKgFQDa4'
measurement_unit = 'imperial'
filepath = path+'/GoogleDistanceCalculator/data_files/' \
           if platform == 'linux' or platform == 'linux2' \
           else path+'\\GoogleDistanceCalculator\\data_files\\'

filename = 'origins_and_destinations.csv'

final_path = filepath + filename
input_df = pd.read_csv(final_path)

output_df = pd.DataFrame(columns=['S. No', 'origin', 'destination', 'distance', 'raw_response'])

url_endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json'


for index, row in input_df.iterrows():
    mydict = {'units'       : measurement_unit,
              'origins'     : row['origin_address'],
              'destinations': row['destination_address'],
              'key'         : google_key}

    resp = requests.get(url_endpoint, params=mydict)


    if(resp.ok):
        jData = json.loads(resp.text)




    print(jData)