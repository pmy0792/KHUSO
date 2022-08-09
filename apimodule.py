import cv2
import numpy as np
import json
import sys
import requests
import json
import ast
from subprocess import check_output


headers = {'Authorization': 'Bearer ' + '191fb802fa3c0d692dfd859587ae8f28f9ee4d22'}

def execute_api(filename):
    rect=[]
    result_str=""
    
    command = "node 4.js {}".format(filename.split('.')[0]) 
    result = check_output(command,shell=True).decode(sys.stdout.encoding)
  
    # api 호출 될 때 사용
    '''
    json_obj = json.loads(result)    
    for obj in json_obj["segmentation_results"]:
        rect.append(obj["contained_bbox"])

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    for idx,r in enumerate(rect):
        img = cv2.rectangle(img, (r['x'], r['y']), (r['x'] + r['w'], r['y'] + r['h']), (255-idx*30, 0, 0), 4)
            
    # get nutrients info
    imgid = json_obj['imageId']
    print(imgid)
    url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
    resp = requests.post(url,json={'imageId': imgid}, headers=headers)
    print("food name : ", resp.json())
    '''
    
    # api 호출 안 될 때
    img='4.jpg'
    resp_str="{'foodName': ['steamed broccoli', 'baby back ribs'], 'hasNutritionalInfo': True, 'ids': [16, 686], 'imageId': 1448737, 'nutritional_info': {'calories': 819.67, 'dailyIntakeReference': {'CHOCDF': {'label': 'Carbs', 'level': 'LOW', 'percent': 4.769354941422913}, 'ENERC_KCAL': {'label': 'Energy', 'level': 'NONE', 'percent': 39.82288080588778}, 'FASAT': {'label': 'Saturated', 'level': 'HIGH', 'percent': 73.01867128661989}, 'FAT': {'label': 'Fat', 'level': 'HIGH', 'percent': 84.0893968041895}, 'NA': {'label': 'Sodium', 'level': 'MEDIUM', 'percent': 16.000666666666667}, 'PROCNT': {'label': 'Protein', 'level': 'NONE', 'percent': 44.019861763221115}, 'SUGAR': {'label': 'Sugars', 'level': 'MEDIUM', 'percent': 6.3232}}, 'totalNutrients': {'CA': {'label': 'Calcium', 'quantity': 99.47999999999999, 'unit': 'mg'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 11.0438, 'unit': 'g'}, 'CHOLE': {'label': 'Cholesterol', 'quantity': 210.0, 'unit': 'mg'}, 'ENERC_KCAL': {'label': 'Energy', 'quantity': 819.67, 'unit': 'kcal'}, 'FAMS': {'label': 'Monounsaturated fats', 'quantity': 25.12238, 'unit': 'g'}, 'FAPU': {'label': 'Polyunsaturated', 'quantity': 6.7636199999999995, 'unit': 'g'}, 'FASAT': {'label': 'Saturated', 'quantity': 19.287670000000002, 'unit': 'g'}, 'FAT': {'label': 'Fat', 'quantity': 67.309, 'unit': 'g'}, 'FATRN': {'label': 'Trans fat', 'quantity': 0.472, 'unit': 'g'}, 'FE': {'label': 'Iron', 'quantity': 3.877, 'unit': 'mg'}, 'FIBTG': {'label': 'Fiber', 'quantity': 4.682999999999999, 'unit': 'g'}, 'FOLAC': {'label': 'Folic acid', 'quantity': 0.0, 'unit': 'µg'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 151.29, 'unit': 'µg'}, 'FOLFD': {'label': 'Folate (food)', 'quantity': 151.29, 'unit': 'µg'}, 'K': {'label': 'Potassium', 'quantity': 952.28, 'unit': 'mg'}, 'MG': {'label': 'Magnesium', 'quantity': 66.15, 'unit': 'mg'}, 'NA': {'label': 'Sodium', 'quantity': 240.01, 'unit': 'mg'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 13.001199999999999, 'unit': 'mg'}, 'P': {'label': 'Phosphorus', 'quantity': 422.39, 'unit': 'mg'}, 'PROCNT': {'label': 'Protein', 'quantity': 45.3028, 'unit': 'g'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 0.8315, 'unit': 'mg'}, 'SUGAR': {'label': 'Sugars', 'quantity': 1.9759999999999998, 'unit': 'g'}, 'SUGAR.added': {'label': 'Sugars, added', 'quantity': 0.0, 'unit': 'g'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 0.9301999999999999, 'unit': 'mg'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 3.0298999999999996, 'unit': 'mg'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 107.8, 'unit': 'µg'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 0.9, 'unit': 'µg'}, 'VITB6A': {'label': 'Vitamin B6', 'quantity': 1.4970499999999998, 'unit': 'mg'}, 'VITC': {'label': 'Vitamin C', 'quantity': 91.79599999999999, 'unit': 'mg'}, 'VITD': {'label': 'Vitamin D', 'quantity': 4.4, 'unit': 'µg'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 200.60099999999997, 'unit': 'µg'}, 'ZN': {'label': 'Zinc', 'quantity': 7.184799999999999, 'unit': 'mg'}}}, 'nutritional_info_per_item': [{'food_item_position': 1, 'hasNutritionalInfo': True, 'id': 16, 'nutritional_info': {'calories': 97.67, 'dailyIntakeReference': {'CHOCDF': {'label': 'Carbs', 'level': 'LOW', 'percent': 4.769354941422913}, 'ENERC_KCAL': {'label': 'Energy', 'level': 'NONE', 'percent': 4.7452032748680075}, 'FASAT': {'label': 'Saturated', 'level': 'LOW', 'percent': 3.0425093105034353}, 'FAT': {'label': 'Fat', 'level': 'MEDIUM', 'percent': 6.982359546845372}, 'NA': {'label': 'Sodium', 'level': 'LOW', 'percent': 3.867333333333333}, 'PROCNT': {'label': 'Protein', 'level': 'NONE', 'percent': 3.42303718576943}, 'SUGAR': {'label': 'Sugars', 'level': 'MEDIUM', 'percent': 6.3232}}, 'totalNutrients': {'CA': {'label': 'Calcium', 'quantity': 61.48, 'unit': 'mg'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 11.0438, 'unit': 'g'}, 'CHOLE': {'label': 'Cholesterol', 'quantity': 0.0, 'unit': 'mg'}, 'ENERC_KCAL': {'label': 'Energy', 'quantity': 97.67, 'unit': 'kcal'}, 'FAMS': {'label': 'Monounsaturated fats', 'quantity': 3.70438, 'unit': 'g'}, 'FAPU': {'label': 'Polyunsaturated', 'quantity': 0.77162, 'unit': 'g'}, 'FASAT': {'label': 'Saturated', 'quantity': 0.80367, 'unit': 'g'}, 'FAT': {'label': 'Fat', 'quantity': 5.5889999999999995, 'unit': 'g'}, 'FATRN': {'label': 'Trans fat', 'quantity': 0.0, 'unit': 'g'}, 'FE': {'label': 'Iron', 'quantity': 1.017, 'unit': 'mg'}, 'FIBTG': {'label': 'Fiber', 'quantity': 4.682999999999999, 'unit': 'g'}, 'FOLAC': {'label': 'Folic acid', 'quantity': 0.0, 'unit': 'µg'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 151.29, 'unit': 'µg'}, 'FOLFD': {'label': 'Folate (food)', 'quantity': 151.29, 'unit': 'µg'}, 'K': {'label': 'Potassium', 'quantity': 422.28, 'unit': 'mg'}, 'MG': {'label': 'Magnesium', 'quantity': 30.15, 'unit': 'mg'}, 'NA': {'label': 'Sodium', 'quantity': 58.01, 'unit': 'mg'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 0.7952, 'unit': 'mg'}, 'P': {'label': 'Phosphorus', 'quantity': 98.39, 'unit': 'mg'}, 'PROCNT': {'label': 'Protein', 'quantity': 3.5227999999999997, 'unit': 'g'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 0.1755, 'unit': 'mg'}, 'SUGAR': {'label': 'Sugars', 'quantity': 1.9759999999999998, 'unit': 'g'}, 'SUGAR.added': {'label': 'Sugars, added', 'quantity': 0.0, 'unit': 'g'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 0.0942, 'unit': 'mg'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 2.7499, 'unit': 'mg'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 107.8, 'unit': 'µg'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 0.0, 'unit': 'µg'}, 'VITB6A': {'label': 'Vitamin B6', 'quantity': 0.31704999999999994, 'unit': 'mg'}, 'VITC': {'label': 'Vitamin C', 'quantity': 91.79599999999999, 'unit': 'mg'}, 'VITD': {'label': 'Vitamin D', 'quantity': 0.0, 'unit': 'µg'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 200.60099999999997, 'unit': 'µg'}, 'ZN': {'label': 'Zinc', 'quantity': 0.6648000000000001, 'unit': 'mg'}}}, 'serving_size': 148.0}, {'food_item_position': 2, 'hasNutritionalInfo': True, 'id': 686, 'nutritional_info': {'calories': 722.0, 'dailyIntakeReference': {'CHOCDF': {'label': 'Carbs', 'level': 'LOW', 'percent': 0.0}, 'ENERC_KCAL': {'label': 'Energy', 'level': 'NONE', 'percent': 35.07767753101977}, 'FASAT': {'label': 'Saturated', 'level': 'HIGH', 'percent': 69.97616197611644}, 'FAT': {'label': 'Fat', 'level': 'HIGH', 'percent': 77.10703725734415}, 'NA': {'label': 'Sodium', 'level': 'MEDIUM', 'percent': 12.133333333333333}, 'PROCNT': {'label': 'Protein', 'level': 'NONE', 'percent': 40.59682457745169}, 'SUGAR': {'label': 'Sugars', 'level': 'LOW', 'percent': 0.0}}, 'totalNutrients': {'CA': {'label': 'Calcium', 'quantity': 38.0, 'unit': 'mg'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 0.0, 'unit': 'g'}, 'CHOLE': {'label': 'Cholesterol', 'quantity': 210.0, 'unit': 'mg'}, 'ENERC_KCAL': {'label': 'Energy', 'quantity': 722.0, 'unit': 'kcal'}, 'FAMS': {'label': 'Monounsaturated fats', 'quantity': 21.418, 'unit': 'g'}, 'FAPU': {'label': 'Polyunsaturated', 'quantity': 5.992, 'unit': 'g'}, 'FASAT': {'label': 'Saturated', 'quantity': 18.484, 'unit': 'g'}, 'FAT': {'label': 'Fat', 'quantity': 61.72, 'unit': 'g'}, 'FATRN': {'label': 'Trans fat', 'quantity': 0.472, 'unit': 'g'}, 'FE': {'label': 'Iron', 'quantity': 2.86, 'unit': 'mg'}, 'FIBTG': {'label': 'Fiber', 'quantity': 0.0, 'unit': 'g'}, 'FOLAC': {'label': 'Folic acid', 'quantity': 0.0, 'unit': 'µg'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 0.0, 'unit': 'µg'}, 'FOLFD': {'label': 'Folate (food)', 'quantity': 0.0, 'unit': 'µg'}, 'K': {'label': 'Potassium', 'quantity': 530.0, 'unit': 'mg'}, 'MG': {'label': 'Magnesium', 'quantity': 36.0, 'unit': 'mg'}, 'NA': {'label': 'Sodium', 'quantity': 182.0, 'unit': 'mg'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 12.206, 'unit': 'mg'}, 'P': {'label': 'Phosphorus', 'quantity': 324.0, 'unit': 'mg'}, 'PROCNT': {'label': 'Protein', 'quantity': 41.78, 'unit': 'g'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 0.656, 'unit': 'mg'}, 'SUGAR': {'label': 'Sugars', 'quantity': 0.0, 'unit': 'g'}, 'SUGAR.added': {'label': 'Sugars, added', 'quantity': 0.0, 'unit': 'g'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 0.836, 'unit': 'mg'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 0.28, 'unit': 'mg'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 0.0, 'unit': 'µg'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 0.9, 'unit': 'µg'},'VITB6A': {'label': 'Vitamin B6', 'quantity': 1.18, 'unit': 'mg'}, 'VITC': {'label': 'Vitamin C', 'quantity': 0.0, 'unit': 'mg'}, 'VITD': {'label': 'Vitamin D', 'quantity': 4.4, 'unit': 'µg'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 0.0, 'unit': 'µg'}, 'ZN': {'label': 'Zinc', 'quantity': 6.52, 'unit': 'mg'}}}, 'serving_size': 200.0}], 'serving_size': 348.0} "
    replaced_resp_str=resp_str.replace("\'","\"")
    #resp_json=json.loads(replaced_resp_str)
    resp_dict= ast.literal_eval(replaced_resp_str)
    nutri_result=extract_nutritient(resp_dict)
    
    
    
    return img, nutri_result
   
def extract_nutritient(response):
    
    # api 호출 될 때
    '''
    info=dict()
    info["foodname"]=response.json()['foodName']
    nutri =['CHOCDF','FAT', 'NA' , 'PROCNT']#탄수화물 지방 나트륨 단백질
    calories=int(response.json()['nutritional_info']['calories'])
    info["calories"] = calories
    
    for nut in nutri:
        a =response.json()['nutritional_info']['totalNutrients']['{}'.format(nut)]
        #print('{} quantity is'.format(a['label']), int(a['quantity']), a['unit'])
        info[a['label']]=str(a['quantity'])+str(a['unit'])
    '''
        
    # api 호출 안 될 때
    info=dict()
    info["foodname"]=response['foodName']
    nutri =['CHOCDF','FAT', 'NA' , 'PROCNT'] #탄수화물 지방 나트륨 단백질
    calories=int(response['nutritional_info']['calories'])
    info["calories"] = calories
    
    for nut in nutri:
        a =response['nutritional_info']['totalNutrients']['{}'.format(nut)]
        #print('{} quantity is'.format(a['label']), int(a['quantity']), a['unit'])
        info[a['label']]=str(a['quantity'])+str(a['unit'])
 
    print("Extracted nutritients info: ",info)
    return info
