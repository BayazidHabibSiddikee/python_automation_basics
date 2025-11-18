import requests
from bs4 import BeautifulSoup

url = 'https://m.kuku.lu/new.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all forms
forms = soup.find_all('form')
print(f"Found {len(forms)} form(s).")

# Print action and input names of each form
for index, form in enumerate(forms):
    print(f"\nForm {index + 1}:")
    print("Action:", form.get('action'))
    print("Method:", form.get('method'))
    inputs = form.find_all('input')
    for inp in inputs:
        print("  Input:", inp.get('name'), "Type:", inp.get('type'), "Value:", inp.get('value'))
