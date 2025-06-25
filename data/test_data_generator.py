import random
import string
from datetime import date, timedelta

import requests

from data import data


def generate_random_string(length, letters=string.ascii_letters):
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_numeric_string(length):
    return ''.join(random.choice(string.digits) for _ in range(length))


def generate_random_cyrillic_string(length):
    letters = "абвгдежзийклмнопрстуфхцчшщыэюя"
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    login = generate_random_string(random.randint(2, 10))
    password = generate_random_numeric_string(4)
    first_name = generate_random_cyrillic_string(random.randint(2, 10))

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


def register_new_courier_and_return_login_password():
    courier_data = generate_courier_data()

    response = requests.post(data.BASE_URL + data.API_ENDPOINTS["courier_create"], json=courier_data)

    if response.status_code == 201:
        return [courier_data['login'], courier_data['password'], courier_data['firstName']]

    return []


def generate_order_data():
    first_name = generate_random_cyrillic_string(random.randint(2, 15))
    last_name = generate_random_cyrillic_string(random.randint(2, 15))
    address = generate_random_cyrillic_string(random.randint(5, 50))
    metro_station = random.randint(1, 200)
    phone = '+' + generate_random_numeric_string(random.randint(10, 12))
    rent_time = random.randint(1, 7)
    delivery_date = (date.today() + timedelta(days=random.randint(1, 7))).strftime('%Y-%m-%d')
    comment = generate_random_cyrillic_string(random.randint(0, 24))
    colors = data.ORDER_COLORS
    color = random.choices(colors, k=random.randint(0, 2))

    return {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment,
        "color": color if color else None
    }