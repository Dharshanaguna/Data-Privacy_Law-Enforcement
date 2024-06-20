from flask import Flask, request, render_template, redirect, url_for
from masking import (
    apply_aes_hashing, aggregate_time, bin_age, add_random_noise, category_generalization, 
    location_aggregation, boolean_masking, text_redaction, date_generalization, 
    postal_code_masking, geographic_masking
)
from masking_techniques import get_masking_technique

import pickle
import os

app = Flask(__name__)

# Load the TF-IDF vectorizer
with open('models/tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Load the best gradient boosting model
with open('models/best_gb_model.pkl', 'rb') as file:
    best_gb_model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    attribute = request.form['attribute']
    attribute_vectorized = tfidf_vectorizer.transform([attribute])
    prediction = best_gb_model.predict(attribute_vectorized)[0]
    return render_template('prediction.html', attribute=attribute, prediction=prediction)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('options'))
    return render_template('login.html')

@app.route('/options', methods=['GET', 'POST'])
def options():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        if form_type == 'FIR':
            return redirect(url_for('FIR'))
        elif form_type == 'ChargeSheet':
            return redirect(url_for('ChargeSheet'))
        elif form_type == 'Arrested':
            return redirect(url_for('Arrested'))
        elif form_type == 'Accused':
            return redirect(url_for('Accused'))
    return render_template('options.html')

@app.route('/FIR1', methods=['GET', 'POST'])
def FIR():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return redirect(url_for('maskfir', **form_data))
    return render_template('FIR1.html')

@app.route('/Accused1', methods=['GET', 'POST'])
def Accused():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return redirect(url_for('maskaccused', **form_data))    
    return render_template('Accused1.html')

@app.route('/ChargeSheet1', methods=['GET', 'POST'])
def ChargeSheet():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return redirect(url_for('maskchargesheet', **form_data))
    return render_template('ChargeSheet1.html')

@app.route('/Arrested1', methods=['GET', 'POST'])
def Arrested():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        return redirect(url_for('maskarrested', **form_data))
    return render_template('Arrested1.html')

@app.route('/maskfir', methods=['GET', 'POST'])
def maskfir():
    form_data = request.args.to_dict()
    if request.method == 'POST':
        form_data = request.form.to_dict()  # Get form data from POST request
        return redirect(url_for('masked_data', **form_data))
    return render_template('maskfir.html', form_attributes=form_data.keys(), form_data=form_data)

@app.route('/maskaccused', methods=['GET', 'POST'])
def maskaccused():
    form_data = request.args.to_dict()
    if request.method == 'POST':
        form_data = request.form.to_dict()  # Get form data from POST request
        return redirect(url_for('masked_data', **form_data))
    return render_template('maskaccused.html', form_attributes=form_data.keys(), form_data=form_data)

@app.route('/maskchargesheet', methods=['GET', 'POST'])
def maskchargesheet():
    form_data = request.args.to_dict()
    if request.method == 'POST':
        form_data = request.form.to_dict()  # Get form data from POST request
        return redirect(url_for('masked_data', **form_data))
    return render_template('maskchargesheet.html', form_attributes=form_data.keys(), form_data=form_data)

@app.route('/maskarrested', methods=['GET', 'POST'])
def maskarrested():
    form_data = request.args.to_dict()
    if request.method == 'POST':
        form_data = request.form.to_dict()  # Get form data from POST request
        return redirect(url_for('masked_data', **form_data))
    return render_template('maskarrested.html', form_attributes=form_data.keys(), form_data=form_data)


@app.route('/masked_data', methods=['GET'])
def masked_data():
    form_data = request.args.to_dict()
    masked_data = {}

    masking_functions = {
        'Hashing': apply_aes_hashing,
        'Time Aggregation': lambda x: aggregate_time(x, 'Year'),
        'Bin Age': bin_age,
        'Random Noise': add_random_noise,
        'Category Generalization': category_generalization,
        'Location Aggregation': location_aggregation,
        'Boolean Masking': boolean_masking,
        'Text Redaction': text_redaction,
        'Date Generalization': date_generalization,
        'Postal Code Masking': postal_code_masking,
        'Geographic Masking': geographic_masking,
    }

    for key, value in form_data.items():
        if key.startswith('mask_'):
            original_key = key[5:]  # Remove 'mask_' prefix to get the original key
            technique = get_masking_technique(original_key)
            if technique in masking_functions:
                masked_data[original_key] = masking_functions[technique](form_data[original_key])
            else:
                masked_data[original_key] = form_data[original_key]  # No masking technique found
        elif not f"mask_{key}" in form_data:
            masked_data[key] = value

    return render_template('masked_data.html', data=masked_data)



if __name__ == '__main__':
    app.run(debug=True)
