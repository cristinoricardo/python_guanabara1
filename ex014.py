#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input("Informe a temperatura em C:"))
f = ((9*c/5)+32)
print("A temperatura em {} é {} em F!".format(c, f))

import requests

# Solicita ao usuário o nome da cidade
city = input("Digite o nome da cidade: ")

# Geocode (obter latitude e longitude da cidade) usando Open-Meteo
geocode_url = f'https://geocode.maps.co/search?q={city}'
geocode_response = requests.get(geocode_url)

if geocode_response.status_code == 200:
    geocode_data = geocode_response.json()
    if geocode_data:
        lat = geocode_data[0]['lat']
        lon = geocode_data[0]['lon']

        # Obter o clima usando a latitude e longitude
        weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data['current_weather']['temperature']
            print(f'A temperatura atual em {city} é {temperature}°C.')
        else:
            print("Erro na obtenção dos dados climáticos!")
    else:
        print("Cidade não encontrada!")
else:
    print("Erro na busca da cidade!")