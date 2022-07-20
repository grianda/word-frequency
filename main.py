#retrieve lyrics to a song from lyrics.ovh and return each word with how many times it appears

import requests
import json

def get_lyrics(title, artist):
    req = requests.get(str.format('https://api.lyrics.ovh/v1/{}/{}', title, artist))
    if req.status_code == 200:
        data = json.loads(req.content)
        return data['lyrics']
    else:
        return None

if __name__ == '__main__':
    lyrics = get_lyrics("Coldplay", "Paradise")
    if lyrics == None:
        print("lyrics not found")
    else:
        print("successful")