import cv2
import numpy as np
import json
import sys
import requests

from subprocess import check_output


headers = {'Authorization': 'Bearer ' + '3d59cef697bcc7734a9ec19107ac1618224902f9'}

def execute_api(filename):
    rect=[]
    result_str=""
    
    command = "node 4.js {}".format(filename.split('.')[0]) 
    result = check_output(command,shell=True).decode(sys.stdout.encoding)
    #p = p[:len(p)-2]
    #print ("result:\n", result)

    json_obj = json.loads(result)
    #print(json_obj)
    #print(len(json_obj["segmentation_results"]))
    
    for obj in json_obj["segmentation_results"]:
        rect.append(obj["contained_bbox"])

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    for idx,r in enumerate(rect):
        img = cv2.rectangle(img, (r['x'], r['y']), (r['x'] + r['w'], r['y'] + r['h']), (255-idx*30, 0, 0), 4)
        #img = cv2.rectangle(img, (rect2['x'], rect2['y']), (rect2['x'] + rect2['w'], rect2['y'] + rect2['h']), (0, 255, 0), 4)

    
    # get nutrients info
    imgid = json_obj['imageId']
    print(imgid)
    url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
    resp = requests.post(url,json={'imageId': 1448610}, headers=headers)
    #print("food name : ", resp.json())
    
    print(resp)
    nutri =['CHOCDF','FAT', 'NA' , 'PROCNT']#탄수화물 지방 나트륨 단백질

    #print("calories is:", int(resp.json()['nutritional_info']['calories']))
    result_str+="Total calories: "+ str(resp.json()['nutritional_info']['calories'])
    
    ###########level, percent정보#################
    for nut in nutri:
        a =resp.json()['nutritional_info']['dailyIntakeReference']['{}'.format(nut)]
        #print('{} level, percent is'.format(a['label']), a['level'], int(a['percent']))
        result_str+="{} level, percent: ".format(a['label'])+ a['level']+ str(a['percent'])
    ##########자세한 g 정보 #######################
            
    for nut in nutri:
        a =resp.json()['nutritional_info']['totalNutrients']['{}'.format(nut)]
        #print('{} quantity is'.format(a['label']), int(a['quantity']), a['unit'])
        result_str+="{} quantity: ".format(a['label'])+ str(a['quantity'])+ a['unit']   
    
    return img, result_str
    #cv2.imshow('1', img)
    #cv2.waitKey(0)
    
#execute_api("1.jpg")