from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://de.wikipedia.org/wiki/Liste_der_Staaten_der_Erde'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
country_table = soup.find('table')
head_row = country_table.find('tr')
chart_titles = []
for i, tit in enumerate(head_row):
    if i % 2 != 0:
        title = tit.text.strip()
        if title == 'Einwohner2022[4]':
            title = 'Einwohner2022'
        if title == 'Flächein km²[5]':
            title = 'Flächein km²'
        chart_titles.append(title)

df = pd.DataFrame(columns=chart_titles)
print(len(chart_titles))
column_data = country_table.find_all('tr')
add_count, rel_count = 0, 0
for row in column_data[3:]:
    row_data = row.find_all('td')
    individual_row_data = []
    print(row_data)
    for data in row_data[:len(chart_titles)]:  # Begrenze die Anzahl der Elemente in row_data auf die Anzahl der Spalten in chart_titles
        temp_row_data = data.text.strip()
        if temp_row_data == '':
            temp_row_data = np.nan  # Leeres Feld wird mit "NaN" gefüllt
        individual_row_data.append(temp_row_data)
        print(len(individual_row_data))

    
    df.loc[len(df)] = individual_row_data


print(f'Added: {add_count}, Released: {rel_count}')
df.to_csv(r'C:/Users/admin/MyDocuments/vs code/EigeneProjekte/Laenderliste.csv')