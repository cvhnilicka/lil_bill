
import requests




underground_key = "9336d91494799de4c1a02efcf9c84368"
google_api_key = "AIzaSyBVU2iI94OgOpwk_GvxEBQroZ-ryM6Znpw"
	

def weatherApi(num):
	print "WEATHERAPI YO"
	api = ('http://api.openweathermap.org/data/2.5/weather?''id=%s''&APPID=9336d91494799de4c1a02efcf9c84368') % (num) 

	r = requests.get(api)
       	feed = r.json()
	

       	#save the weather summary
    	weather_whole = feed["weather"][0]
      	weather_summary = weather_whole["main"]
       	#current temperature
       	temp = feed["main"]["temp"]
       	temp = ((temp - 273.15) * 1.8) + 32.00

       	#current description of weatheer
       	description = weather_whole["description"]

       	#current wind information
       	wind_speed = feed["wind"]["speed"]

	print temp, wind_speed, weather_summary, description


def checkCity(string):
	print "CHECK CITY YO"
	city = 4434663 #madison, wi
	if " in " in string:
		split = string.split(" ")
		index = string.index("in")
		cityname = split[index+1]
		print city
		cities = eval(open('cities_dict.txt', 'r').read())
		if cityname in cities:
			city = cities[cityname]
	weatherApi(city)



cmd = "this guy sounds like fun"

validAPIs = {
"weather" : checkCity(cmd)

}
