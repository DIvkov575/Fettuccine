import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("APIKEY")
BASE_URL = 'https://public-api.beatoven.ai/api/v1'
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

def generate_song():
    r = requests.post(f'{BASE_URL}/tracks', json={'prompt': {'text': '2-minute ambient frequencies'}}, headers=HEADERS)
    # r = requests.post(f'{BASE_URL}/tracks', json={'prompt': {'text': '2-minute lo-fi super-ambient chillhop track'}}, headers=HEADERS)
    print("a", r.json())
    track_id = r.json()['tracks'][0]
    print(f'Created track: {track_id}')

    r = requests.post(f'{BASE_URL}/tracks/compose/{track_id}', json={'format': 'wav', 'looping': 'False'}, headers=HEADERS)
    print("b", r.json())
    task_id = r.json()['task_id']
    print(f'Composing... task ID: {task_id}')

    while True:
        r = requests.get(f'{BASE_URL}/tasks/{task_id}', headers=HEADERS)
        status = r.json()['status']
        print(f'Status: {status}')
        print(r.json())
        if status == 'composed':
            file_name = f"./source/{track_id}.mp3"
            track_url = r.json()['meta']['track_url']
            response = requests.get(track_url)

            with open(file_name, "wb") as f:
                f.write(response.content)
            break

        elif status == 'failed':
            print('Composition failed.')
            break
        time.sleep(6)

for i in range(1):
    generate_song()
