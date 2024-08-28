from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

app.config['DEBUG'] = True
app.config["MONGO_URI"]="mongodb://localhost:27017/form_data"
mongo=PyMongo(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("Form Submitted")


    form_data = {
        'Name': request.form.get('Name'),
        'Employee_ID':request.form.get('Employee_ID'),
        'Supervisor_rating':request.form.get('Supervisor_rating'),
        'hr_rating':request.form.get('hr_rating'),
        'team_satisfaction':request.form.get('team_satisfaction'),
        'team_helpfulness':request.form.get('team_helpfulness'),
        'additional_comments':request.form.get('additional_comments'),
    }

    print("Form data received:", form_data) 

    if form_data:
      mongo.db.form_entries.insert_one(form_data)
      print("Data inserted successfully")
    else:
        print("Failed to insert data")

    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)