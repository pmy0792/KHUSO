from pickle import NONE
from flask import Flask, render_template, request
from hamcrest import none
from pymysql import NULL
from werkzeug.utils import secure_filename
import cv2
from apimodule import *


app = Flask(__name__)


meal_list=[]

@app.route('/', methods=["GET","POST"])
def home(meal_list=[],img=None):
    if request.method=="GET":
        return render_template("home.html",meal_list=meal_list,img=img)
    
    #elif request.method=="POST": 
    #    return render_template("home.html",meal_list=meal_list,img=f.filename)

@app.route('/upload',methods=["POST"])
def upload(meal_list=[],img=None):
    # image upload
    f=request.files['file']
    f.save(secure_filename(f.filename))
    print("file {} uploaded successfully".format(f.filename))
        
    # run api
    img, result=execute_api(secure_filename(f.filename))
    print("img: ",img)
    #execute_api(secure_filename('chicken_10'))
    analyzed_img="static/"+f.filename
    print("analyzed_img path:" , analyzed_img)
    cv2.imwrite(analyzed_img,img)
        
    # save meal info based on analysis
    # 여기서 meal name, nutrients info 뽑아내고 사용자가 g수 입력할 수 있도록
    meal_list.append(f.filename)
    #meal_list.append({"image":f.filename,"meal_name": meal_name})
    
    return render_template("home.html", meal_list=meal_list,img=analyzed_img,result=result)

@app.route('/save',methods=["POST"])
def save():
    # meal_list에 모든 정보 저장
    meal_list=[] 
    #quantity_data=request.form.items()
    #for food,quantity in quantity_data:
    #    # g수에 맞춰 nutrients 계산 후 meal_list update
     
    return render_template("home.html",meal_list=meal_list,img=None)


if __name__ == '__main__':
    app.run(debug=True)