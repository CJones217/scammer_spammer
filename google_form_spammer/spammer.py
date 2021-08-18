import requests
import os
import random
import string
import json
import time


random.seed = (os.urandom(1024))

names = json.loads(open('first.json').read())
states = json.loads(open('states.json').read())
cities = json.loads(open('cities.json').read())


url = 'https://docs.google.com/forms/d/e/1FAIpQLSeP_xpcQ7P0Uan_p-hGBCP7Ipwm4FCXXQTNDUvyjqG4u42Vmg/formResponse'

while True:
    first_name = random.choice(names)
    middle_name = random.choice(names)
    last_name = random.choice(names)
    state = random.choice(states)
    date = f'{random.randint(1,30)}-{random.randint(1,12)}-{random.randint(1930,2021)}'
    ssn = f'{random.randint(100,999)}-00-{random.randint(1000,9999)}'
    num = f'{random.randint(100000000,999999999)}'
    expire = f'{random.randint(1,30)}-{random.randint(1,12)}-{random.randint(2026,2031)}'
    height = f'{random.randint(1,8)}\' {random.randint(0,11)}\'\' '
    weight = f'{random.randint(0,400)}'
    addy = f'{random.randint(123,99999)} {random.choice(names)}dr'
    city = random.choice(cities)
    zip = f'{random.randint(1,999999)}'
    phone = f'555-{random.randint(100,999)}-{random.randint(1000,9999)}'

    try:
        requests.post(url,allow_redirects=False, data={
            'entry.1087930455': first_name,
            'entry.1053893224': middle_name,
            'entry.996642920': last_name,
            'entry.253203409': date,
            'entry.58615951': ssn,
            'entry.1044347020': num,
            'entry.305968062': date,
            'entry.412762834': expire,
            'entry.624979867': state,
            'entry.772765424': height,
            'entry.1373129095': weight,
            'entry.72381656': addy,
            'entry.1239012354': city,
            'entry.1523547596': state,
            'entry.904681537': zip,
            'entry.1362139680': phone,
            'entry.276154064': 'Male',
            'entry.276154064_sentinel': '',
            'fvv': '1',
            'draftResponse': '[null,null,"-2814579426008475198"]',
            'pageHistory': '0',
            'fbzx': '-2814579426008475198',
        })

        print(first_name,middle_name,last_name,date,ssn,num,date,expire,state,height,weight,addy,city,state,zip,phone)
        time.sleep(10)
    except Exception:
        print('something bad happened :(')