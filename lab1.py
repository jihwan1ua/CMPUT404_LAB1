# will get you to use pip request then get python version

import requests

# requests from google.com

#response = requests.get("http://google.com")

response = requests.post("http://ccid-eddieantonio.rhcloud.com/jihwan")

#print requests.__version__

print response.status_code