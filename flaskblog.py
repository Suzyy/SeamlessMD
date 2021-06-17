from flask import Flask, render_template
app = Flask(__name__)

import json
import datetime

with open('patient30.json') as f:
    data = json.load(f)

headings = ("ID", "First Name", "Last Name", "Birth Date", "Gender")
tableData = []
#retrieving key data from json file
for patient in data['patients']:
    id = patient['resource']['id']
    firstName = patient['resource']['name'][0]['given']
    lastName = patient['resource']['name'][0]['family']
    birthDate = patient['resource']['birthDate']
    gender = patient['resource']['gender']
    tableData.append([id, firstName, lastName, birthDate, gender])
    #print(firstName, lastName, birthDate, gender)

#basic stats
numberOfPatients = (len(data['patients']))
avgAgeOfPatients = 0
totAgeOfPatients = 0

#calculating average age of patients
for patient in data['patients']:
    birthDate = patient['resource']['birthDate']
    year = int(birthDate[0:4])
    month = int(birthDate[5:7])
    date = int(birthDate[8:])
    birth_date = datetime.date(year, month, date)
    today_date = datetime.date(2021, 6, 17)
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) <(birth_date.month, birth_date.day))
    totAgeOfPatients += age
    #print(totAgeOfPatients)

avgAgeOfPatients = totAgeOfPatients/numberOfPatients
#print(avgAgeOfPatients)

posts = [
    {
        'author': 'Suzy Lee',
        'title': 'SeamlessMD Notification 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Suzy Lee',
        'title': 'SeamlessMD Notification 2',
        'content': 'Second post content',
        'date_posted': 'May 20, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/patientData")
def about():
    return render_template('patientData.html', title='Patient Data', totNum=numberOfPatients, avgAge=avgAgeOfPatients, headings=headings, tableData=tableData)

if __name__ == '__main__':
    app.run(debug=True)