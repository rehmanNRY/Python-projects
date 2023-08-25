import requests
def weather(city_name):
    api_key = "97e76093f85b8f152f68c2df93874f1e"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data["cod"]==200:
        temp = data['main']['temp']
        print(f"\n{temp-273.15 }° C\n")
    else:
        print("\nCity not found.\n")
print("============= Welcome to weather app =============")
while(True):
    print("****** Enter city or Press q to exit ******")
    city_name = input("==> Enter: ")
    if city_name == 'q':
        print("\nYou exit the program\n")
        break
    else:
        weather(city_name)