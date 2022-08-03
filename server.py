from pickle import NONE
from flask import Flask, render_template, request
from hamcrest import none
from pymysql import NULL
from werkzeug.utils import secure_filename
import cv2
from apimodule import *


app = Flask(__name__)


img_list=[]

@app.route('/', methods=["GET","POST"])
def home(img_list=[],img=None):
    if request.method=="GET":
        return render_template("home.html",img_list=img_list,img=img)
    
    elif request.method=="POST": #image 업로드 들어옴
        f=request.files['file']
        f.save(secure_filename(f.filename))
        img_list.append(f.filename)
        print("file {} uploaded successfully".format(f.filename))
        
        # run api
        img, result=execute_api(secure_filename(f.filename))
        #execute_api(secure_filename('chicken_10'))
        analyzed_img="static/"+f.filename
        print("analyzed_img path:" , analyzed_img)
        cv2.imwrite(analyzed_img,img)
        return render_template("home.html",img_list=img_list,img=f.filename)

if __name__ == '__main__':
    app.run(debug=True)