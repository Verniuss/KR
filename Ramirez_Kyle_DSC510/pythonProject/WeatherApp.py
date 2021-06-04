# Week 12
# 12.1 Programming Assignment
# Author Kyle Ramirez
# Date Created: 3-June-2021
# Create a Python Application which asks the user for their zip code or city.
# Display the weather forecast in a readable format to the user.
# Use functions including a main function.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
import requests
import sys

url_city = 'http://api.openweathermap.org/data/2.5/weather?q={},&appid={}'
API_Key = '87e470f22c3e22a7be1ac60c894fcc7a'
url_zip = 'http://api.openweathermap.org/data/2.5/weather?zip={},&appid={}'
acceptable_inputs = (1, 2, 3)


# this function will connect to the API with the city and API key
def get_weather_city(city):
    output = requests.get(url_city.format(city, API_Key))
    if output:
        json = output.json()
        city = json['name']
        country = json['sys']['country']
        weather1 = json['weather'][0]['main']
        weather2 = json['weather'][0]['description']
        tp_kelvin = json['main']['temp']
        tp_kelvin_min = json['main']['temp_min']
        tp_kelvin_max = json['main']['temp_max']
        tp_celsius = tp_kelvin - 273.15
        tp_celsius_min = tp_kelvin_min - 273.15
        tp_celsius_max = tp_kelvin_max - 273.15
        tp_fahrenheit = (tp_kelvin - 273.15) * 9 / 5 + 32
        tp_fahrenheit_min = (tp_kelvin_min - 273.15) * 9 / 5 + 32
        tp_fahrenheit_max = (tp_kelvin_max - 273.15) * 9 / 5 + 32
        humidity = json['main']['humidity']
        pressure = json['main']['pressure']
        # This tuple will structure the API response to easily sort and extract the data
        return_output = (city, country, humidity, pressure, weather1, weather2,
                         tp_celsius, tp_celsius_max, tp_celsius_min, tp_fahrenheit,
                         tp_fahrenheit_min, tp_fahrenheit_max, tp_fahrenheit_min)
        return return_output
    else:
        no_return = None
        return no_return


# this function will connect to the API with the zipcode and API key
def get_weather_zip(zipcode):
    output = requests.get(url_zip.format(zipcode, API_Key))
    if output:
        json = output.json()
        city = json['name']
        country = json['sys']['country']
        weather1 = json['weather'][0]['main']
        weather2 = json['weather'][0]['description']
        tp_kelvin = json['main']['temp']
        tp_kelvin_min = json['main']['temp_min']
        tp_kelvin_max = json['main']['temp_max']
        tp_celsius = tp_kelvin - 273.15
        tp_celsius_min = tp_kelvin_min - 273.15
        tp_celsius_max = tp_kelvin_max - 273.15
        tp_fahrenheit = (tp_kelvin - 273.15) * 9 / 5 + 32
        tp_fahrenheit_min = (tp_kelvin_min - 273.15) * 9 / 5 + 32
        tp_fahrenheit_max = (tp_kelvin_max - 273.15) * 9 / 5 + 32
        humidity = json['main']['humidity']
        pressure = json['main']['pressure']
        # This tuple will structure the API response to easily sort and extract the data
        return_output = (city, country, humidity, pressure, weather1, weather2,
                         tp_celsius, tp_celsius_max, tp_celsius_min, tp_fahrenheit,
                         tp_fahrenheit_min, tp_fahrenheit_max, tp_fahrenheit_min)
        return return_output
    else:
        no_return = None
        return no_return


# This function handles the user input for city.
# It handles whether the user entered in a valid response.
# If a valid response is given by the user it will return the weather as a result
# If non valid response is given. It will kick back to the user to enter in a valid response
def user_input_city():
    while True:
        get_input_city = input("Type in the city: ")
        try:
            get_input_city = str(get_input_city)
            weather = get_weather_city(get_input_city)
            if weather is not None:
                print("Location: {}, {}".format(weather[0], weather[1]))
                print("Humidity: {}".format(weather[2]))
                print("Pressure: {}".format(weather[3]))
                print("Weather Type1: {}".format(weather[4]))
                print("Weather Type2: {}".format(weather[5]))
                print("Celsius: {:.2f}°C".format(weather[6]))
                print("Max Celsius Temperature: {:.2f}°C".format(weather[7]))
                print("Min Celsius Temperature: {:.2f}°C".format(weather[8]))
                print("Fahrenheit: {:.2f}°F".format(weather[9]))
                print("Max Fahrenheit Temperature: {:.2f}°F".format(weather[10]))
                print("Min Fahrenheit Temperature: {:.2f}°F".format(weather[11]))
            if weather is None:
                print("You did not enter in a valid city")
            break
        except ValueError:
            try:
                if get_input_city == int(get_input_city):
                    print("You did not enter a valid response. "
                          "Only letters are acceptable when entering in a city")
            except ValueError:
                print("You did not enter a valid response. "
                      "Only letters are acceptable when entering in a city")
    return get_input_city


# This function handles the user input for zipcode.
# It handles whether the user entered in a valid response.
# If a valid response is given by the user it will return the weather as a result
# If non valid response is given. It will kick back to the user to enter in a valid response
def user_input_zip():
    while True:
        get_input_zip = input("Type in the zip code: ")
        try:
            get_input_zip = int(get_input_zip)
            weather = get_weather_zip(get_input_zip)
            if weather is not None:
                print("Location: {}, {}".format(weather[0], weather[1]))
                print("Humidity: {}".format(weather[2]))
                print("Pressure: {}".format(weather[3]))
                print("Weather Type1: {}".format(weather[4]))
                print("Weather Type2: {}".format(weather[5]))
                print("Celsius: {:.2f}°C".format(weather[6]))
                print("Max Celsius Temperature: {:.2f}°C".format(weather[7]))
                print("Min Celsius Temperature: {:.2f}°C".format(weather[8]))
                print("Fahrenheit: {:.2f}°F".format(weather[9]))
                print("Max Fahrenheit Temperature: {:.2f}°F".format(weather[10]))
                print("Min Fahrenheit Temperature: {:.2f}°F".format(weather[11]))
            if weather is None:
                print("You did not enter in a valid zip code")
            break
        except ValueError:
            try:
                if get_input_zip == str(get_input_zip):
                    print("You did not enter a valid response. "
                          "Only numbers are acceptable when entering in a Zipcode")
            except ValueError:
                print("You did not enter a valid response. "
                      "Only numbers are acceptable when entering in a Zipcode")
    return get_input_zip


# This is the initial function to determine what functions to run based on the user response
def city_or_zip():
    while True:
        get_input = input("For the City selection enter 1. "
                          "For the Zipcode selection enter 2. If you wish to quit enter 3: ")
        try:
            get_input = int(get_input)
            if get_input == 1:
                break
            if get_input == 2:
                break
            if get_input == 3:
                print("You have elected to exit the program")
                sys.exit()
            if get_input not in acceptable_inputs:
                print("You did not enter a valid response. "
                      "Only 1, 2 or 3 is a valid response.")
                continue
        except ValueError:
            try:
                if get_input == str(get_input):
                    print("You did not enter a valid response. "
                          "Only 1, 2 or 3 is a valid response.")
            except ValueError:
                print("You did not enter a valid response. "
                      "Only 1, 2 or 3 is a valid response.")
    return get_input


def main():

    print("Welcome, Enter either a 1 to search by City or 2 to search by Zipcode."
          "If you wish to quit enter 3: ")
    while True:
        get_input = city_or_zip()
        # This option will proceed to the city functions
        if get_input == 1:
            user_input_city()
        # This option will proceed to the zipcode functions
        if get_input == 2:
            user_input_zip()
        # This option will quit the program
        if get_input == 3:
            print("You have elected to exit the program")
            sys.exit()
        if get_input not in acceptable_inputs:
            print("You did not enter a valid response. "
                  "Only 1, 2 or 3 is a valid response.")
            continue


if __name__ == "__main__":
    main()
