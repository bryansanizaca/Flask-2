from flask import Flask
app = Flask(__name__)

@app.route('/')
def hellow_world():
    return 'Hello, World!'

@app.route('/predict')
def hellow_predict():
    return 'predicciones!'
if __name__ =="__main__":
    app.run()