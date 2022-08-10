from pickle import NONE
from flask import Flask, render_template, request
from hamcrest import none
from pymysql import NULL
from werkzeug.utils import secure_filename
import cv2
from apimodule import *

app = Flask(__name__)
meal_list=[]
challenge_info=dict()
challenging=False
input_weight=False
graph_data={
    "date":['08.05', '08.06', '08.07', '08.08', '08.09', '08.10', '08.11'],
    "calorie":[1278, 2210, 1955, 1982, 1570, 2730, 1432],
    "carbs":[154, 107, 124, 96, 184, 135,104],
    "protein":[10, 120, 84, 96, 142, 127,135],
    "fat":[54, 67, 74, 61, 84, 48,96]
}



@app.route('/test',methods=['GET'])
def test():
    return render_template("test.html")


@app.route('/', methods=["GET","POST"])
def home(img=None):
    global meal_list
    global challenging
    global challenge_info
    global graph_data
    global input_weight
    
    if request.method=="GET":
        # 그래프 정보 넘겨줘야함
        # 날짜, 칼로리, 탄, 단, 지
        
        
        
        return render_template("home.html",graph_data=graph_data,meal_list=meal_list,img=img,challenging=challenging,challenge_info=challenge_info,input_weight=input_weight)
    
    elif request.method=="POST": #챌린지 참가!!
        challenging=True
        goal=request.form.get('goal')
        current_state=request.form.get('current-state')
        goal_state=request.form.get('goal-state')
        deadline=request.form.get('deadline')
        challenge_info = {
            "goal":goal,
            "current_state":float(current_state),
            "goal_state":float(goal_state),
            "deadline":deadline[5:7] + '.' + deadline[8:]
        }
        print("challenge info: ",challenge_info)
        return render_template("home.html",graph_data=graph_data,meal_list=meal_list,img=img,challenging=challenging,challenge_info=challenge_info,input_weight=input_weight)
        
    #elif request.method=="POST": 
    #    return render_template("home.html",meal_list=meal_list,img=f.filename)

@app.route('/upload',methods=["GET","POST"])
def upload(img=None):
    global meal_list, challenging, input_weight
    print("Request to /upload")
    # image upload
    f=request.files['file']
    
    # api 사용 시
    #filename=f.filename
    
    # api 사용 안 할 때
    filename='4.jpg'
    
    
    # 노트북에서 돌릴 때 
    f.save(secure_filename(filename))
    print("file {} uploaded successfully".format(f.filename))
     
    # 모바일에서 돌릴 때
     
     
        
    # run api
    img, result=execute_api(secure_filename(f.filename)) #result는 meal 정보 담는 dict
    print("img: ",img)
    
    # api 사용시...
    '''
    analyzed_img=f.filename
    print("analyzed_img path:" , analyzed_img)
    cv2.imwrite(analyzed_img,img)
    '''
        
    # api 사용 안 할 때
    analyzed_img='4.jpg'
        
        
    # save meal info based on analysis
    # 여기서 meal name, nutrients info 뽑아내고 사용자가 g수 입력할 수 있도록,,,,
   
    meal_list.append({"id": len(meal_list)+1,"image":f.filename,"meal_info": result})
    print("/upload   meal_list:",meal_list)
    return render_template("home.html", meal_list=meal_list,img=analyzed_img,challenging=challenging,challenge_info=challenge_info,input_weight=input_weight)


@app.route('/kgupload', methods=["POST"])
def homee(img=None):
    global today_weight
    input_weight = True
    
    print("connect")
    if request.method=="POST":
        print("connect_pub")
        
        today_weight = request.form.get('today-weight')
        today_info = float(today_weight)
        print("today info: ", today_info)
    return render_template("home.html",graph_data=graph_data,meal_list=meal_list,img=img,challenging=challenging,challenge_info=challenge_info,today_info = today_info, input_weight = input_weight)



@app.route('/detail/<int:id>', methods=["GET"])
def detail(id):
    global meal_list
    print("/detail   meal_list: ",meal_list)
    found=dict()
    for meal in meal_list:
        print("meal: ",meal)
        print(type(meal["id"]), type(meal))
        if meal["id"]==id:
            print("found!!!")
            found=meal # 해당 dict 통째로 가져오기
    return render_template("foodinfo.html",meal=found)


if __name__ == '__main__':
    #meal_list=[]
    app.run(debug=True)
    