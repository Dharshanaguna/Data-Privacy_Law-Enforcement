from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import csv
import os

app = Flask(__name__)

# Create a directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# CSV file path
CSV_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')

# Function to append data to CSV file
def append_to_csv(data):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

# Function to read the last row of data from the CSV file
def get_last_row():
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        if len(rows) > 1:
            return rows[-1]  # Return the last row excluding the header
        else:
            return None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('options'))  # Redirect to options.html after login form submission
    return render_template('login.html')

@app.route('/options', methods=['GET', 'POST'])
def options():
    if request.method == 'POST':
        return redirect(url_for('FIR'))  # Redirect to FIR.html after options form submission
    return render_template('options.html')

@app.route('/FIR', methods=['GET', 'POST'])
def FIR():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('FIR.html')

@app.route('/Accident', methods=['GET', 'POST'])
def Accident():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('Accident.html')

@app.route('/Victim', methods=['GET', 'POST'])
def Victim():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('Victim.html')

@app.route('/Complaint', methods=['GET', 'POST'])
def Complaint():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('Complaint.html')

@app.route('/ChargeSheet', methods=['GET', 'POST'])
def ChargeSheet():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('ChargeSheet.html')

@app.route('/Arrested', methods=['GET', 'POST'])
def Arrested():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('Arrested.html')

@app.route('/Accused', methods=['GET', 'POST'])
def Accused():
    if request.method == 'POST':
        return redirect(url_for('masking'))  # Redirect to masking.html after FIR form submission
    return render_template('Accused.html')


@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Get form data from the POST request
    district_name = request.form['districtName']
    unit_name = request.form['unitName']
    fir_no = request.form['firNo']
    ri = request.form['ri']
    year = request.form['year']
    month = request.form['month']
    offence_from_date = request.form['offenceFromDate']
    offence_to_date = request.form['offenceToDate']
    fir_reg_date_time = request.form['firRegDateTime']
    fir_date = request.form['firDate']
    victim_count = request.form['victimCount']
    accused_count = request.form['accusedCount']
    arrested_male = request.form['arrestedMale']
    arrested_female = request.form['arrestedFemale']
    arrested_count = request.form['arrestedCount']
    serial_no = request.form['serialNo']
    accused_charge_sheeted_count = request.form['accusedChargeSheetedCount']
    conviction_count = request.form['convictionCount']
    fir_id = request.form['firID']
    unit_id = request.form['unitID']
    crime_no = request.form['crimeNo']

    # Prepare the data to be saved in CSV format
    csv_data = [district_name, unit_name, fir_no, ri, year, month,
                offence_from_date, offence_to_date, fir_reg_date_time, fir_date,
                victim_count, accused_count, arrested_male, arrested_female,
                arrested_count, serial_no, accused_charge_sheeted_count,
                conviction_count, fir_id, unit_id, crime_no]  

    # Append the data to the CSV file
    append_to_csv(csv_data)

    # Redirect to the masking page
    return redirect(url_for('masking'))

@app.route('/masking', methods=['GET', 'POST'])
def masking():
    if request.method == 'POST':
        return redirect(url_for('summary'))  # Redirect to summary.html after masking form submission
    return render_template('masking.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Process the form data here
    # After processing, redirect to the summary page
    return redirect(url_for('summary'))

# Define a route to render the summary page
@app.route('/summary')
def summary():
    row = get_last_row()

    if row:
        # Pass the data to the summary template
        return render_template('summary.html', 
                               districtName=row[0], unitName=row[1], 
                               firNo=row[2], ri=row[3], year=row[4], 
                               month=row[5], offenceFromDate=row[6], 
                               offenceToDate=row[7], firRegDateTime=row[8], 
                               firDate=row[9], victimCount=row[10], 
                               accusedCount=row[11], arrestedMale=row[12], 
                               arrestedFemale=row[13], arrestedCount=row[14], 
                               serialNo=row[15], accusedChargeSheetedCount=row[16], 
                               convictionCount=row[17], firID=row[18], 
                               unitID=row[19], crimeNo=row[20])
    else:
        # Handle the case where no data is found
        return render_template('summary.html', 
                               districtName='', unitName='', firNo='', 
                               ri='', year='', month='', offenceFromDate='', 
                               offenceToDate='', firRegDateTime='', firDate='', 
                               victimCount='', accusedCount='', arrestedMale='', 
                               arrestedFemale='', arrestedCount='', serialNo='', 
                               accusedChargeSheetedCount='', convictionCount='', 
                               firID='', unitID='', crimeNo='')

@app.route('/ocr', methods=['GET', 'POST'])
def ocr_form():
    if request.method == 'POST':
        # Handle the OCR form submission here
        return redirect(url_for('ocr'))  # Redirect to the OCR page after processing the form
    else:
        # Handle the GET request for the OCR page
        return render_template('ocr.html')

    
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
