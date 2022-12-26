import requests
import time

today = time.strftime('%Y-%m-%d')
API_KEY = "<api_here>" #api key | https://www.weatherapi.com/


def location(a): 
    global locate   
    locate = str(a)
    return locate 

class current:
    def __init__(self):
        response_curr = requests.get(f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={locate}&aqi=no")
        re_curr = (response_curr.status_code)
        if re_curr == 200:
            self.name = response_curr.json()['location']['name']
            re = response_curr.json()['current']
            self.temp = re['temp_c'] #temperature
            self.is_day = re['is_day'] #day(1)/night(0)
            cond = re['condition']
            self.condition = cond['text'] #condition
            self.icon = cond['icon']
            self.wind_spd = re['wind_kph'] #wind speed in kmh
            self.wind_deg = re['wind_degree'] ##wind direction
            self.wind_dir = re['wind_dir'] #wind direction
            self.precip = re['precip_mm'] #rain in mm
            self.humidity = re['humidity'] #humidity
            self.cloud = re['cloud'] #cloud cover
            self.feelslike = re['feelslike_c'] #temp feel
            self.vis = re['vis_km'] #visibility in km
            self.gust  = re['gust_kph'] #gust speed in kmh
            self.uv = re['uv'] #uv index
        elif re_curr == 401:
            print("API key not provided or Invalid")
        elif re_curr == 400:
            print("API request url is invalid")        
        else:
            print("Something went wrong")  

class astro:
    def __init__(self):
        response_astro = requests.get(f"https://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q={locate} &dt={today}")
        re_astro = (response_astro.status_code)
        if re_astro == 200:
            re = response_astro.json()['astronomy']['astro']
            self.sunrise = re['sunrise']
            self.sunset = re['sunset']
            self.moonrise = re['moonrise']
            self.moonset = re['moonset']
            self.moon_phase = re['moon_phase']
            self.moon_illumination = re['moon_illumination']
        elif re_astro == 401:
            print("API key not provided or Invalid")
        elif re_astro == 400:
            print("API request url is invalid")        
        else:
            print("Something went wrong")     
