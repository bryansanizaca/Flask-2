from flask import Flask
from flask_cors impor CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hellow_world():
    return 'Hello, World!'

@app.route('/predict')
def hellow_predict():
    return 'predicciones!'
if __name__ =="__main__":
    app.run()