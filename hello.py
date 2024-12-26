from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the comedy class!!! Bapat is doing comedy with dhanno by calling him meetha"
if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)






















