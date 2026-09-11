import requests

def get_weather(latitude,longitude):
    response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data=response.json();
    return data['current']['temperature_2m']

paris_temp=get_weather(48.85,2.35)
london_temp=get_weather(51.50,-0.12)
tokyo_temp=get_weather(35.68,139.69)

print(f"Paris:{paris_temp} degree Celsius   \nLondon: {london_temp} degree Celsius \n Tokyo:{tokyo_temp}degree Celsius  ")
    