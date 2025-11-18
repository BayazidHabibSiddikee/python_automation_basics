import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the webpage
url = 'https://m.kuku.lu/new.php'  # Replace with the target URL
response = requests.get(url)
response.raise_for_status()  # Raises an error for bad responses (e.g. 404)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Save to a file
with open('ch11.p4.2.Getting html formats.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
file = open('ch11.p4.2.Getting html formats.txt', 'wb')
for i in response.iter_content(10000):
    file.write(i)
file.close()


print("HTML page saved successfully as saved_page.txt")
