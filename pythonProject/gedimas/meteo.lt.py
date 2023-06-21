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

night_temp = [temperature.get_text() for temperature in temperatures[::2]]
week_day = [day.get_text() for day in week_days]

data = {'weekday': week_day, 'temperature': night_temp}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by='temperature')

plt.bar(df_sorted['weekday'], df_sorted['temperature'])
plt.xlabel('Savaitės diena')
plt.ylabel('Temperatūra')
plt.title('Orų prognozė Vilniuje')
plt.show()
