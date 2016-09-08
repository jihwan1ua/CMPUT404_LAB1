# will get you to use pip request then get python version

import requests

# requests from google.com

#response = requests.get("http://google.com")

#response = requests.post("http://ccid-eddieantonio.rhcloud.com/jihwan")

response = requests.get("https://raw.githubusercontent.com/jihwan1ua/CMPUT404_LAB1/master/lab1.py")

#print requests.__version__

#print response.status_code

print response.text
