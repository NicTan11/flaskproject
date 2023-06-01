from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

@app.route('/convert/<float:celsius>/')
def convert(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"The temperature in Fahrenheit is: {fahrenheit}"

if __name__ == '__main__':
    app.run()
