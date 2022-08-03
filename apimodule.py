import cv2
import numpy as np
import json
import sys
import requests

from subprocess import check_output


headers = {'Authorization': 'Bearer ' + '191fb802fa3c0d692dfd859587ae8f28f9ee4d22'}

def execute_api(filename):
    rect=[]
    
    command = "node 4.js {}".format(filename.split('.')[0]) 
    result = check_output(command,shell=True).decode(sys.stdout.encoding)
    #p = p[:len(p)-2]
    print ("result:\n", result)

    json_obj = json.loads(result)
    print(len(json_obj["segmentation_results"]))
    
    for obj in json_obj["segmentation_results"]:
        rect.append(obj["contained_bbox"])

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    for idx,r in enumerate(rect):
        img = cv2.rectangle(img, (r['x'], r['y']), (r['x'] + r['w'], r['y'] + r['h']), (255-idx*30, 0, 0), 4)
        #img = cv2.rectangle(img, (rect2['x'], rect2['y']), (rect2['x'] + rect2['w'], rect2['y'] + rect2['h']), (0, 255, 0), 4)

    
    # get nutrients info
    imgid = json_obj['imageId']
    url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
    resp = requests.post(url,json={'imageId': imgid}, headers=headers)
    print("food name : ", resp.json())
    return img, result
    #cv2.imshow('1', img)
    #cv2.waitKey(0)
    
execute_api("1.jpg")