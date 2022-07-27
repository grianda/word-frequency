from flask import Flask, render_template
import lyrics

app = Flask(__name__)

@app.route('/')
def home():
    lyrs = lyrics.get_lyrics("Carly Rae Jepsen","Run Away with Me")
    freq = lyrics.word_freq(lyrs)
    words = lyrics.sort_by_occ(freq)
    return render_template("index.html", words=words, freq=freq)