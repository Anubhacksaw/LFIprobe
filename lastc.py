import requests

def fi(url):

    response = requests.get(url)

    response_text = response.text.split("\n")

    if "root" in response_text[0]:
        return True
    else:
        return False
