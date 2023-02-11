import re
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <span>House of Metazord</span>
        <body>

        
        <style>
        
            body {background-color: #f0f0f0;}
            input[type=text] {width: 300px; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;}
            input[type=submit] {width: 100px; background-color: #ffd700; color: white; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; font-color: black;}
            input[type=submit]:hover {background-color: #45a049;}

            @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

            span {
            font-family: 'Bebas Neue', cursive;
            font-size: 3em;
            position: absolute;
            top: 8%;
            left: 48%;
            transform: translate(-50%,-50%);
            background-image: linear-gradient(gold, gold);
            background-size: 100% 10px;
            background-repeat: no-repeat;
            background-position: 100% 0%;
            transition: background-size .7s, background-position .5s ease-in-out;
            }

            span:hover {
            background-size: 100% 100%;
            background-position: 0% 100%;
            transition: background-position .7s, background-size .5s ease-in-out;
            }


        </style>
        <center>
        <br><br><br><br><br><br><br><br><br><br>
        <form method="post">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
        </center>
        </body>
        </html>
        
    '''

@app.route('/', methods=['POST'])
def say_hello():
    name = request.form['name']
    if re.fullmatch(r'^[a-zA-Z0-9]+$', name):
        return f'Text entered =  {name}'
    else:
        return 'Invalid name'

if __name__ == "__main__":
    app.run(host= os.getenv('IP',"0.0.0.0"), port=int(os.getenv('PORT',8081)))
