
'''
Created on 2. 4. 2014.

@author: barboz
'''
import re
import requests
import cx_Oracle
import time


if __name__ == '__main__':
    
    connection = cx_Oracle.connect("bbarun/Krd5muh@XE")
    cursor = connection.cursor()
    cursor.execute("select * from geocoder_input")
    result_set = cursor.fetchall()
    
    for c in range(10): #range(len(result_set)):
        sql_result =  result_set[c][0].decode('latin2') + result_set[c][1]
        print sql_result
        request_string = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + sql_result + '+HR&sensor=false'
        request = requests.get(request_string)
        r_json = request.json()
        
        time.sleep(3)
          
        lat_long = [None] * 3
        lat_long[0] = r_json['results'][0]['geometry']['location']['lat']
        lat_long[1] = r_json['results'][0]['geometry']['location']['lng']
        lat_long[2] = r_json['results'][0]['formatted_address']
     
        print lat_long[0], lat_long[1], unicode(lat_long[2])
    
    
    