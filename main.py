#retrieve lyrics to a song from lyrics.ovh and return each word with how many times it appears

import requests
import json
import re

def get_lyrics(artist, title):
    req = requests.get(str.format('https://api.lyrics.ovh/v1/{}/{}', artist, title))
    if req.status_code == 200:
        data = json.loads(req.content)
        if "Paroles de la chanson" == data['lyrics'][:21]:
            print('trace')
            return data['lyrics'].split('\r\n', 2)[1]
        return data['lyrics']
    else:
        return None

def word_freq(lyrics):
    words = re.split('[\.\"\',;:!?\(\)\[\]\{\}\<\>]*[ \n\r]+[\.\"\',;:!?\(\)\[\]\{\}\<\>]*', lyrics)
    freq = {}
    for word in words:
        try:
            freq[word.lower()] += 1
        except KeyError:
            freq[word.lower()] = 1
    return freq

if __name__ == '__main__':
    lyrics = get_lyrics("Carly Rae Jepsen", "Run Away with Me")
    """if lyrics == None:
        print("lyrics not found")
    else:
        print(lyrics)"""
    freq = word_freq(lyrics)
    #print(freq)
    f = open("lyrics.csv", "w")
    for word in freq:
        f.write(str.format("{},{}\n", word, freq[word]))
    f.close()
