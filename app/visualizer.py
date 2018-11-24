from flask import Flask
from flask import request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def visualize():
	my_dict = read_csv()
	return render_template('html_page.html', my_dict=my_dict)

def read_csv():
	disaster_dict = {}
	with open('disasters.csv') as csv_file:
		line_reader = csv.reader(csv_file, delimiter=',')
		for row in line_reader:
			print(row)
	return disaster_dict

if __name__ == '__main__':
	read_csv()