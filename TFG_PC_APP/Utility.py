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
        r = requests.post('http://192.168.1.110:70/data/', data='179=100&')
    if buttonpressed == 1:
        r = requests.post('http://192.168.1.110:70/data/', data='-1=100&')
    if buttonpressed == 0:
        r = requests.post('http://192.168.1.110:70/data/', data='89=100&')
    if buttonpressed == 3:
        r = requests.post('http://192.168.1.110:70/data/', data='181=100&')
    if buttonpressed == 4:
        r = requests.post('http://192.168.1.110:70/data/', data='379=100&')
    if buttonpressed == 5:
        r = requests.post('http://192.168.1.110:70/data/', data='269=100&')
    if buttonpressed == 6:
        r = requests.post('http://192.168.1.110:70/data/', data='0,0')
