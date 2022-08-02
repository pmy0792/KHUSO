from flask import Flask, render_template, request
from pymysql import NULL
from werkzeug.utils import secure_filename
from apimodule import *

app = Flask(__name__)


img_list=[]

@app.route('/', methods=["GET","POST"])
def home(img_list=[]):
    if request.method=="GET":
        return render_template("home.html",img_list=img_list)
    
    elif request.method=="POST": #image 업로드 들어옴
        f=request.files['file']
        f.save(secure_filename(f.filename))
        img_list.append(f.filename)
        print("file {} uploaded successfully".format(f.filename))
        
        # run api
        execute_api(secure_filename(f.filename))
        #execute_api(secure_filename('chicken_10'))
        return render_template("home.html",img_list=img_list)

if __name__ == '__main__':
    app.run(debug=True)