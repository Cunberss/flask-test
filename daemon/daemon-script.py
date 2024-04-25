import time
import requests
import argparse
import psutil


def get_cpu_percent():
    return psutil.cpu_percent(interval=1)


def send_post_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f'Successfully sent POST request. Status code: {response.status_code}')
    else:
        print(f'Failed to send POST request. Status code: {response.status_code}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to send POST requests at regular intervals')
    parser.add_argument('--server', default='127.0.0.1', help='IP address of the server')
    parser.add_argument('--port', default='5000', help='Port of the server')
    args = parser.parse_args()

    server_url = f'http://{args.server}:{args.port}/api/save-data'

    while True:
        send_post_request(server_url, {'cpu_percent': get_cpu_percent()})
        time.sleep(10)
