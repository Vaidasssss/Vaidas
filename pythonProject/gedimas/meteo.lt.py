import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define website
url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"

# Response from the website
response = requests.get(url)

# Create a bs4 object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

week_days = soup.find_all('span', class_='date')
temperatures = soup.find_all('span', class_='big up-from-zero')
seven_days = week_days[:7]
temperatures_days = temperatures [:7]

# print(temperatures)


night_temp = [temperature.get_text() for temperature in temperatures[::2]]
week_day = [day.get_text() for day in week_days]

temp_list = []
for temperature in temperatures:
        temp_text = temperature.get_text().replace('C','')
        temp_values = int(temp_text[:-1])
        temp_list.append(temp_values)

#
min_legth = min(len(week_day), len(temp_list))
week_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']
week_temp_orde = [0, 5, 10, 15, 20, 25, 30]
# print(temperatures)


reorder_weekdays = week_day [:min_legth]
reorder_temperature = night_temp[:min_legth]


data = {
        'weekday': week_day,
        'temperature': temp_list
        }

df = pd.DataFrame(data)

df_sorted = df.sort_values(by='temperature')

plt.bar(df_sorted['weekday'], df_sorted['temperature'])
plt.xlabel('Savaitės diena')
plt.ylabel('Temperatūra')
plt.title('Orų prognozė Vilniuje')
plt.show()




