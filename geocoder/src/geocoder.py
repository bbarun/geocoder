'''
Created on 2. 4. 2014.

@author: barboz
'''

import re
import requests


if __name__ == '__main__':
    request = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false')
    print request
    print request.text
    print request.json()