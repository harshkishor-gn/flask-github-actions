from flask import Flask

# Create a Flask web app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, system!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
