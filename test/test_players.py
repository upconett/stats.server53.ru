import requests

def check_get():
    response = requests.get('http://127.0.0.1:8000/players/')
    print("GET", response.text, response.status_code)

def check_post():
    data = {
        'all_': ['Gay', 'Nigga_87', 'Egor'],
        'in_': 'Egor',
        'out_': None
    }
    response = requests.post(
        url='http://127.0.0.1:8000/players/',
        json=data
    )
    print("POST", response.text, response.status_code)

if __name__ == '__main__':
    check_post()
    check_get()
