import json
import requests


from samplebase import SampleBase
from rgbmatrix import graphics
import time

api_key = "36b1c67493e5574c5658dbc7f3c92b40"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

units = "imperial"

city_name = input("Enter city name: ")

complete_url = base_url + "q=" + city_name + "&units=" + units + "&appid=" + api_key 
# http://api.openweathermap.org/data/2.5/weather?q=pueblo&units=imperial&appid=36b1c67493e5574c5658dbc7f3c92b40
# http://api.openweathermap.org/data/2.5/weather?q=moscow&units=imperial&appid=36b1c67493e5574c5658dbc7f3c92b40

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"] 
    
    current_temperature = y["temp"] 
  
    current_pressure = y["pressure"] 

    current_humidiy = y["humidity"] 

    z = x["weather"] 
  
    weather_description = z[0]["description"] 

    print(" Temperature = " +
                    str(current_temperature) + 
          "\n atmospheric pressure = " +
                    str(current_pressure) +
          "\n humidity = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 

    print(complete_url)

else: 
    print(" City Not Found ")

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/5x8.bdf")

        color = graphics.Color(0, 255, 48)
        graphics.DrawText(canvas, font, 10, 25, color, "" + str(int(current_temperature)))

        time.sleep(900)

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()