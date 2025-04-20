from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

def perform_calculation(input_text):
    input_text = input_text.strip().lower()

    # Basic math detection
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", input_text)

    if "plus" in input_text or "+" in input_text:
        if len(numbers) == 2:
            return f"The result is {float(numbers[0]) + float(numbers[1])}"
    elif "minus" in input_text or "-" in input_text:
        if len(numbers) == 2:
            return f"The result is {float(numbers[0]) - float(numbers[1])}"
    elif "times" in input_text or "multiply" in input_text or "*" in input_text:
        if len(numbers) == 2:
            return f"The result is {float(numbers[0]) * float(numbers[1])}"
    elif "divided" in input_text or "/" in input_text:
        if len(numbers) == 2 and float(numbers[1]) != 0:
            return f"The result is {float(numbers[0]) / float(numbers[1])}"
        else:
            return "Division by zero is not allowed."
    elif "square root" in input_text:
        if numbers:
            return f"The square root is {math.sqrt(float(numbers[0]))}"
    elif "power" in input_text or "^" in input_text:
        if len(numbers) == 2:
            return f"The result is {float(numbers[0]) ** float(numbers[1])}"
    elif "sin" in input_text:
        if numbers:
            return f"The sine is {math.sin(math.radians(float(numbers[0])))}"
    elif "cos" in input_text:
        if numbers:
            return f"The cosine is {math.cos(math.radians(float(numbers[0])))}"
    elif "tan" in input_text:
        if numbers:
            return f"The tangent is {math.tan(math.radians(float(numbers[0])))}"

    return "Sorry, I couldn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = perform_calculation(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
