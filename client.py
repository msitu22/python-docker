import requests

def call_url_with_zip_code(city_name):
    # URL for the server
    server_url = "http://127.0.0.1:5000/city_to_zip/" + city_name
    
    # Making the API call to the server
    response = requests.get(server_url)

    print(response)
    
    # Parsing the server response
    zipcode = response.json()
    
    print(f"zipcode: {zipcode}")

    server2_url = "http://127.0.0.1:4001/zip_to_weather/" + zipcode

    response_from_sev2 = requests.get(server2_url)

    weather = response_from_sev2.json()

    print(f"Weather for {city_name}: {weather}")


city_name = input("Enter a city name: ")
# city_name = "Sunnyvale"
call_url_with_zip_code(city_name)
