import sys
import requests
import time


def update_record(username, password):
    url = 'http://' + username + ':' + password + '@dyn.dns.he.net/nic/update?hostname=' + username
    try:
        r = requests.get(url)
        print(r.status_code)
    except requests.RequestException as e:
        print(e)

if __name__ == '__main__':
    your_domain = str(sys.argv[1])
    your_domain_key = str(sys.argv[2])
    while True:
        update_record(your_domain, your_domain_key)
        time.sleep(600)
