from flask import Flask, render_template
import pathlib
import sqlite3

base_path = pathlib.Path(r'C:\Users\nicho\Github\project_group_13\database')
db_name = "hospital.db"
db_path = base_path / db_name
print(db_path)

hos = Flask(__name__)

@hos.route("/")
def index():
    return render_template("index.html")

@hos.route("/about")
def about():
    return render_template("about.html")

@hos.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    lst = cursor.execute('SELECT * FROM hospital_table Limit 5').fetchall()
    con.close()
    
    # for title
    column_headers = ['Provider_ID', 'Hospital_Name', 'Address', 'City', 'State', 'ZIP_Code',
       'County_Name', 'Hospital_Type', 'Hospital_Ownership',
       'Emergency_Services', 'Disease_Name', 'Days', 'Predicted_Cases',
       'Observed_Cases', 'SIR']
    
    return render_template("data.html", column=column_headers, hospital_features=lst)

if __name__=="__main__":
    hos.run(debug=True)