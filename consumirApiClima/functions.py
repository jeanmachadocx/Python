import requests

def get_weather_from_api(api_key, city):
    """
    Consulta a API OpenWeather e retorna os dados do clima.
    """
    url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{url}appid={api_key}&q={city}&units=metric&lang=pt_br"  # Incluí unidades em Celsius e idioma PT-BR
    response = requests.get(complete_url)
    
    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        return response.json()

    else:
        return {"error": f"Erro ao buscar dados: {response.status_code}, {response.reason}"}

def get_weather(city_name):
    """
    Obtém os dados de clima de uma cidade específica.
    """
    api_key = "1013b9e664d13fa0e0e44100946b8a48"
    weather_data = get_weather_from_api(api_key, city_name)
    
    # Verifica se houve erro na resposta
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        # Extrai as informações do clima
        main = weather_data.get("main", {})
        weather = weather_data.get("weather", [{}])[0]
      
        print("\n")
        print(f"Clima em {city_name}:")
        print(f"Temperatura: {main.get('temp', 'N/A')}°C")
        print(f"Sensação Térmica: {main.get('feels_like', 'N/A')}°C")
        print(f"Condição: {weather.get('description', 'N/A').capitalize()}")
        print(f"Umidade: {main.get('humidity', 'N/A')}%")
  
