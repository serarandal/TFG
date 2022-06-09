import urllib3
import requests


def camera1_on():
    try:
        url = 'http://192.168.1.184'
        http = urllib3.PoolManager()
        resp = http.request('GET', url, timeout=0.1)
        if resp.status == 200: return True
    except urllib3.exceptions.HTTPError as e:
        return False
def camera2_on():
    try:
        url = 'http://192.168.1.185'
        http = urllib3.PoolManager()
        resp = http.request('GET', url, timeout=0.1)
        if resp.status == 200: return True
    except urllib3.exceptions.HTTPError as e:
        return False

def sendSpeedDirection(buttonpressed):
    if buttonpressed == 2:
      try:
          r = requests.post('http://192.168.1.110:70/data/', data='179=100&')
      except requests.exceptions.Timeout as e :
          raise print(e)

    if buttonpressed == 1:
        try:
            r = requests.post('http://192.168.1.110:70/data/', data='-1=100&')
        except requests.exceptions.Timeout as e:
            raise print(e)
    if buttonpressed == 0:
        try:
         r = requests.post('http://192.168.1.110:70/data/', data='89=100&')
        except requests.exceptions.Timeout as e:
            raise print(e)
    if buttonpressed == 3:
        try:
            r = requests.post('http://192.168.1.110:70/data/', data='181=100&')
        except requests.exceptions.Timeout as e:
            raise print(e)
    if buttonpressed == 4:
        try:
            r = requests.post('http://192.168.1.110:70/data/', data='379=100&')
        except requests.exceptions.Timeout as e:
            raise print(e)
    if buttonpressed == 5:
        try:
            r = requests.post('http://192.168.1.110:70/data/', data='269=100&')
        except requests.exceptions.Timeout as e:
            raise print(e)
    if buttonpressed == 6:
        try:
            r = requests.post('http://192.168.1.110:70/data/', data='0,0')
        except requests.exceptions.Timeout as e:
            raise print(e)
