import requests
import json
import os
from sys import platform
import pandas as pd
import csv
import xlrd
import xlsxwriter



path = os.path.dirname(os.getcwd())

# Key and unit needs to be changed.
# ----------------------------------
google_key = 'AIzaSyBOpfbJt97X-nUq76lbVyAnukrwKgFQDa4'
measurement_unit = 'imperial'
filepath = path+'/GoogleDistanceCalculator/data_files/' \
           if platform == 'linux' or platform == 'linux2' \
           else path+'\\GoogleDistanceCalculator\\data_files\\'

filename = 'input_origins_and_destinations.csv'

filename_origins  = 'input_origins.xlsx'
filename_destinations ='input_destinations.xlsx'
filename_output = 'output_matrix.xlsx'

final_path_origins = filepath + filename_origins
final_path_destinations = filepath + filename_destinations
final_path_output = filepath + filename_output

print(final_path_origins)

input_df_origins = pd.read_excel(final_path_origins, sheet_name='input_origins')
input_df_destinations = pd.read_excel(final_path_destinations, sheet_name='input_destinations')

#output_df = pd.DataFrame(columns=['S.No.', 'origin', 'destination', 'distance', 'raw_response'])

url_endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json'
#fields = ['S. No', 'origin', 'destination', 'distance', 'raw_response' ]
fields = ['S. No', 'origin']
error_message = ''
distance = ''

workbook =xlsxwriter.Workbook(final_path_output)
worksheet = workbook.add_worksheet()
# values = ['3', '6', '9']
# worksheet.write(1, 1, '\n'.join(values))

#worksheet.write(row, col,     'First Name')

excel_row = 1
excel_column = 1

for index, row in input_df_destinations:
    destination = row['destinations']
    worksheet.write(excel_row, 0, destination)
    for i, r in input_df_origins:
        origin = r['origins']
        mydict = {'units': measurement_unit,
                  'origins': origin,
                  'destinations': destination,  # row['destination_address'],
                  'key': google_key}
        error_message = 'No Error'
        # try:
        #     resp = requests.get(url_endpoint, params=mydict)
        #     if(resp.ok):
        #         jData = json.loads(resp.text)
        #         distance = jData['rows'][0]['elements'][0]['distance']['text']
        # except Exception as e:
        #         error_message = 'Error'
        #         pass
        worksheet.write(excel_row, excel_column, origin)








# with open(final_path_output,'w', newline='') as newFile:
#    # newFileWriter =    csv.writer(newFile)
#   #  newFileWriter.writerow(input_df['origins'])
#
#     for index, row in input_df.iterrows():
#         mydict = {'units'       : measurement_unit,
#                   'origins'     : row['origins'],
#                   'destinations': '2901 NE Blakeley St Seattle, WA 98105',  #row['destination_address'],
#                   'key'         : google_key}
#         error_message = 'No Error'
#         try:
#             resp = requests.get(url_endpoint, params=mydict)
#             if(resp.ok):
#                 jData = json.loads(resp.text)
#                 distance = jData['rows'][0]['elements'][0]['distance']['text']
#         except Exception as e:
#                 error_message = 'Error getting distance.'
#                 pass
#         #combined_row = [row['origins'], '2901 NE Blakeley St Seattle, WA 98105', distance , str(jData), error_message ]
#         #newFileWriter.writerow(combined_row)
#
#         combined_row = [row['origins'], '2901 NE Blakeley St Seattle, WA 98105', distance, str(jData), error_message]
#
#         if index == 0:
#             worksheet.write(row, row['origins'])
#
#         worksheet.write(row, 'test', 'First Name')
#
#         print(jData)
workbook.close()