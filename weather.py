import requests, json
import error
import pymongo
import traceback
class weatherCast(object):
    def on_post(self, req, resp):
        try:
            request_body = req.context['request']
            headers = {'Content-Type' : 'application/json' , 'Accept': 'application/json'}
            api_key = "Your_API_Key"
            payload = input("Enter city name : ")
            url = "http://api.openweathermap.org/data/2.5/weather?"
            print('url ------>> ',url)
            complete_url = url + "appid=" + api_key + "&q=" + payload
            response = requests.get(complete_url)
            call_resp = response(method='POST', url=url, json_data=payload, headers=headers)
            x = response.json()
            client = pymongo.MongoClient("mongodb://localhost:27017/") 
            
            db = client.weather_data # Database Name
            
           
            col = db["Weather"]      # Collection Name   
            x = col.find_one()                
            print(x)
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
            
                # print following values
                print(str(current_temperature))
                    
            
            else:
                print(" City Not Found ")
                
        except Exception as e:
            traceback.print_exc()
            
            