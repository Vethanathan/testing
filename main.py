from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    cwd = os.getcwd()
    r=[]
    file_name = "example.txt"
    file_path = os.path.join(cwd, file_name)
    open(file_path, 'a').close()
    files = os.listdir(cwd)
    h=str(files)
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"+h})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
