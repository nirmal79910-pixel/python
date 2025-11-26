from flask import Flask, render_template, request, jsonify
import secrets
import string
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    result = None
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight', 0))
            height = float(request.form.get('height', 0))
            height_unit = request.form.get('height_unit', 'cm')
            
            if height_unit == 'cm':
                height_m = height / 100
            else:
                height_m = height
            
            if height_m > 0 and weight > 0:
                bmi_value = weight / (height_m ** 2)
                
                if bmi_value < 18.5:
                    category = 'Underweight'
                    color = 'yellow'
                elif bmi_value < 25:
                    category = 'Normal'
                    color = 'green'
                elif bmi_value < 30:
                    category = 'Overweight'
                    color = 'orange'
                else:
                    category = 'Obese'
                    color = 'red'
                
                result = {
                    'bmi': round(bmi_value, 1),
                    'category': category,
                    'color': color
                }
        except (ValueError, ZeroDivisionError):
            result = {'error': 'Please enter valid numbers'}
    
    return render_template('bmi.html', result=result)

@app.route('/life-weeks', methods=['GET', 'POST'])
def life_weeks():
    result = None
    if request.method == 'POST':
        try:
            input_type = request.form.get('input_type', 'age')
            
            if input_type == 'age':
                age = int(request.form.get('age', 0))
            else:
                dob = request.form.get('dob', '')
                if not dob:
                    raise ValueError("Date of birth is required")
                birth_date = datetime.strptime(dob, '%Y-%m-%d').date()
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            lifespan = 90
            total_weeks = lifespan * 52
            weeks_lived = age * 52
            weeks_left = max(0, total_weeks - weeks_lived)
            percentage_lived = min(100, (weeks_lived / total_weeks) * 100)
            
            result = {
                'age': age,
                'weeks_lived': weeks_lived,
                'weeks_left': weeks_left,
                'total_weeks': total_weeks,
                'percentage': round(percentage_lived, 1),
                'years_left': max(0, lifespan - age)
            }
        except (ValueError, TypeError):
            result = {'error': 'Please enter a valid age or date of birth'}
    
    return render_template('life_weeks.html', result=result)

@app.route('/password', methods=['GET'])
def password():
    return render_template('password.html')

@app.route('/api/generate-password', methods=['POST'])
def generate_password():
    try:
        data = request.get_json()
        length = int(data.get('length', 12))
        include_uppercase = data.get('uppercase', True)
        include_numbers = data.get('numbers', True)
        include_symbols = data.get('symbols', True)
        
        length = max(8, min(32, length))
        
        characters = string.ascii_lowercase
        required_chars = [secrets.choice(string.ascii_lowercase)]
        
        if include_uppercase:
            characters += string.ascii_uppercase
            required_chars.append(secrets.choice(string.ascii_uppercase))
        
        if include_numbers:
            characters += string.digits
            required_chars.append(secrets.choice(string.digits))
        
        if include_symbols:
            symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
            characters += symbols
            required_chars.append(secrets.choice(symbols))
        
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(characters) for _ in range(remaining_length)]
        
        secrets.SystemRandom().shuffle(password_chars)
        password = ''.join(password_chars)
        
        return jsonify({'password': password, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
