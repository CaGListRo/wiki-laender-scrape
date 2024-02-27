Wikipedia Country Data Scraper
This Python script scrapes data from the Wikipedia page "Liste der Staaten der Erde" (List of countries on Earth) and extracts information about countries such as population and area.

Dependencies
BeautifulSoup (bs4)
Requests (requests)
Pandas (pandas)
NumPy (numpy)
Installation
Install the required dependencies using pip:

Copy code
pip install beautifulsoup4 requests pandas numpy
Clone or download this repository to your local machine.

Usage
Run the Python script wikipedia_country_scraper.py.
The script will fetch data from the Wikipedia page and parse it to extract country information.
Extracted data will be saved to a CSV file named Laenderliste.csv in the specified directory (C:/Users/admin/MyDocuments/vs code/EigeneProjekte/).

Features
Scrapes data from the Wikipedia page "Liste der Staaten der Erde".
Extracts information about countries including population and area.
Handles empty fields by replacing them with "NaN" (Not a Number) using NumPy.

Notes
The script assumes a specific structure of the Wikipedia page and may need adjustments if the structure changes.
Ensure a stable internet connection while running the script to fetch data from Wikipedia.

License
This project is licensed under the MIT License.
