import requests
import json
import os
from sys import platform
import pandas as pd
import csv

path = os.path.dirname(os.getcwd())

# Key and unit needs to be changed.
# -----------------------------------
google_key = 'AIzaSyBOpfbJt97X-nUq76lbVyAnukrwKgFQDa4'
measurement_unit = 'imperial'
filepath = path+'/GoogleDistanceCalculator/data_files/' \
           if platform == 'linux' or platform == 'linux2' \
           else path+'\\GoogleDistanceCalculator\\data_files\\'

filename = 'input_origins_and_destinations.csv'

final_path = filepath + filename
input_df = pd.read_csv(final_path)

output_df = pd.DataFrame(columns=['S.No.', 'origin', 'destination', 'distance', 'raw_response'])

url_endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json'
fields = ['S. No', 'origin', 'destination', 'distance', 'raw_response' ]
error_message = ''
distance = ''

with open(filepath + 'output_distances.csv','w', newline='') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['S.No.', 'origin', 'destination', 'distance', 'raw_response', 'Error' ])

    for index, row in input_df.iterrows():
        mydict = {'units'       : measurement_unit,
                  'origins'     : row['origin_address'],
                  'destinations': row['destination_address'],
                  'key'         : google_key}
        error_message = 'No Error'
        try:
            resp = requests.get(url_endpoint, params=mydict)
            if(resp.ok):
                jData = json.loads(resp.text)
                distance = jData['rows'][0]['elements'][0]['distance']['text']
        except Exception as e:
                error_message = 'Error getting distance.'
                pass
        combined_row = [row['S.No.'], row['origin_address'], row['destination_address'], distance , str(jData), error_message ]
        newFileWriter.writerow(combined_row)
        print(jData)