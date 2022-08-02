import cv2
import numpy as np
import json
import sys

from subprocess import check_output

def execute_api(filename):
    rect=[]
    
    command = "node 4.js {}".format(filename.split('.')[0]) # 4.js: nodejs 파일 이름, chicken_10: 이미지 이름
    p = check_output(command,shell=True).decode(sys.stdout.encoding)
    #p = p[:len(p)-2]
    print (p)

    json_obj = json.loads(p)
    print(len(json_obj["segmentation_results"]))
    
    for obj in json_obj["segmentation_results"]:
        rect.append(obj["contained_bbox"])
    #rect1 = json_obj["segmentation_results"][0]["contained_bbox"]
    #rect2 = json_obj["segmentation_results"][1]["contained_bbox"]

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    for idx,r in enumerate(rect):
        img = cv2.rectangle(img, (r['x'], r['y']), (r['x'] + r['w'], r['y'] + r['h']), (255-idx*30, 0, 0), 4)
        #img = cv2.rectangle(img, (rect2['x'], rect2['y']), (rect2['x'] + rect2['w'], rect2['y'] + rect2['h']), (0, 255, 0), 4)

    #_,img_encoded=cv2.imencode('.jpg',img)
    
    cv2.imshow('1', img)
    cv2.waitKey(0)