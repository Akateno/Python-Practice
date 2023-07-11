import requests 

api="http://api.open-notify.org/iss-now.json"
response=requests.get(url=api)
data=response.json()
longitude=data["iss_position"]['longitude']
latitude=data["iss_position"]['latitude']
print(latitude,longitude)
if response.status_code != 200:
    print("YESSS")
    