from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/home')
def hello_world():
   return jsonify({"status_code":200,"msg":'success'})

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=4800,debug=True)