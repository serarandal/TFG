import urllib3
import requests


def camera1_on():
    try:
        url = 'http://192.168.1.184'
        http = urllib3.PoolManager()
        resp = http.request('GET', url, timeout=0.1)
        if resp.status == '200': return True
    except urllib3.exceptions.HTTPError as e:
        return False
def camera2_on():
    try:
        url = 'http://192.168.1.185'
        http = urllib3.PoolManager()
        resp = http.request('GET', url, timeout=0.1)
        if resp.status == '200': return True
    except urllib3.exceptions.HTTPError as e:
        return False

def sendSpeedDirection(buttonpressed):
    r = requests.post('http://192.168.1.110:70/data/', data='180=100&')
    r = requests.post('http://192.168.1.110:70/data/', data='0=100&')
    r = requests.post('http://192.168.1.110:70/data/', data='90=100&')
    r = requests.post('http://192.168.1.110:70/data/', data='180=100&')
    r = requests.post('http://192.168.1.110:70/data/', data='380=100&')
    r = requests.post('http://192.168.1.110:70/data/', data='270=100&')
    r = r = requests.post('http://192.168.1.110:70/data/', data='0,0')
