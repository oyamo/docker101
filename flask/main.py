from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return 'Hello, World!' 
  
 
if __name__ == '__main__':
    app.run()
    
# $ export FLASK_APP=hello.py
# $ python -m flask run
