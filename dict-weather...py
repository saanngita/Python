
weather_data= [
    {
      "city": "Kathmandu",
      "temperature": 15,
      "humidity": 60,
      "description": "Partly Cloudy"
    },
    {
      "city": "Pokhara",
      "temperature": 18,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Biratnagar",
      "temperature": 20,
      "humidity": 70,
      "description": "Cloudy"
    },
    {
      "city": "Birgunj",
      "temperature": 22,
      "humidity": 75,
      "description": "Clear"
    },
    {
      "city": "Dharan",
      "temperature": 19,
      "humidity": 68,
      "description": "Rain"
    },
    {
      "city": "Butwal",
      "temperature": 21,
      "humidity": 72,
      "description": "Drizzle"
    },
    {
      "city": "Hetauda",
      "temperature": 23,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Nepalgunj",
      "temperature": 25,
      "humidity": 60,
      "description": "Clear"
    },
    {
      "city": "Dhangadhi",
      "temperature": 24,
      "humidity": 70,
      "description": "Windy"
    },
    {
      "city": "Ghorahi",
      "temperature": 17,
      "humidity": 55,
      "description": "Partly Cloudy"
    },
    {
      "city": "Tulsipur",
      "temperature": 16,
      "humidity": 58,
      "description": "Sunny"
    },
    {
      "city": "Lamahi",
      "temperature": 18,
      "humidity": 60,
      "description": "Clear"
    },
    {
      "city": "Ilam",
      "temperature": 14,
      "humidity": 80,
      "description": "Rain"
    },
    {
      "city": "Janakpur",
      "temperature": 20,
      "humidity": 65,
      "description": "Sunny"
    },
    {
      "city": "Bhairahawa",
      "temperature": 22,
      "humidity": 68,
      "description": "Cloudy"
    },
    {
      "city": "Mahendranagar",
      "temperature": 23,
      "humidity": 70,
      "description": "Clear"
    },
    {
      "city": "Chitwan",
      "temperature": 19,
      "humidity": 75,
      "description": "Drizzle"
    },
    {
      "city": "Lalitpur",
      "temperature": 15,
      "humidity": 60,
      "description": "Sunny"
    },
    {
      "city": "Bhaktapur",
      "temperature": 16,
      "humidity": 62,
      "description": "Partly Cloudy"
    },
    {
      "city": "Khandbari",
      "temperature": 18,
      "humidity": 78,
      "description": "Rain"
    }
  ]
city_found = False
city_weather = weather_data
usercity = input("Enter your city.")
for weather in city_weather:
    if (usercity==weather["city"]):
        print(f"Your city weather: temperature:{weather["temperature"]} humidity:{weather["humidity"]} description:{weather["description"]}")
        city_found = True
        break
if city_found == False:
        print("city is not found.")
       


