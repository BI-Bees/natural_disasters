from flask import Flask
from flask import request
import pandas as pd
import csv
import json
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def visualize():
	result_list = read_csv()
	return render_template('html_page.html', result_list=result_list)

#Reading csv file and creates a list of dictionaries.
def read_csv(custom_csv):
	disaster_list = []
	with open(custom_csv) as csv_file:
		for row in csv.DictReader(csv_file, skipinitialspace=True):
			disaster_list.append({key: value for key, value in row.items()})
	disaster_list = empty_space_filler(disaster_list)
	return disaster_list

#Filling all empty values in a given list of dictionaries
def empty_space_filler(custom_list):
	for dicts in custom_list:
		dicts.update((key, 0) for key, value in dicts.items() if not value)
	return custom_list

def cleanForInt(csv, listString):
    finalList = []
    headers = []
    
    keys = csv[0].keys()
    for key in keys:
        try:
            int(key)
            pass     
        except:
            headers.append(key)
            
    for dic in csv:
        for key, value in dic.items():
            tempDict = ()
            for head in range(len(headers)):
                for head in headers:
                    tempDict = tempDict + (dic.get(head),)
                break
            if key not in headers:
                tempDict = tempDict + (key,value)
                finalList.append(tempDict)
    headers = headers + listString

    return pd.DataFrame(finalList, columns=headers)

if __name__ == '__main__':
	read_csv()