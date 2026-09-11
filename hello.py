import requests
import sys 

latitude=48.85 #Paris latitude
longitude=2.35  #Paris longitude
print(sys.executable)

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response=requests.get(url)
data=response.json()


print(data)
temperature=data["current"]
