import hashlib
import random
from datetime import datetime

def apply_aes_hashing(data):
        return hashlib.sha256(data.encode()).hexdigest()

def aggregate_time(timestamp, aggregation_unit):
    date_format = "%Y-%m-%d %H:%M:%S"  # Assuming timestamp format
    try:
        dt = datetime.strptime(timestamp, date_format)
    except ValueError:
        return timestamp
    
    if aggregation_unit == 'Year':
        return dt.year
    elif aggregation_unit == 'Month':
        return dt.month

def bin_age(age):
    try:
        age = int(float(age))
        if age < 18:
            return 'Child'
        elif age < 60:
            return 'Adult'
        else:
            return 'Senior'
    except ValueError:
        return age

def add_random_noise(value, noise_factor=0.1):
    try:
        value = float(value)
        noise = random.uniform(-noise_factor, noise_factor) * value
        return value + noise
    except ValueError:
        return value

def category_generalization(value):
    return f"Category_{value}"

def location_aggregation(location):
    return f"Location_{location}"

def boolean_masking(value):
    return 'True' if value.lower() in ['true', '1', 'yes'] else 'False'

def text_redaction(text):
    return '[REDACTED]'

def date_generalization(date):
    date_format = "%Y-%m-%d %H:%M:%S"
    try:
        dt = datetime.strptime(date, date_format)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return date

def postal_code_masking(postal_code):
    return postal_code[:3] + '*'

def geographic_masking(lat_or_long):
    try:
        value = float(lat_or_long)
        noise = random.uniform(-0.01, 0.01)
        return value + noise
    except ValueError:
        return lat_or_long