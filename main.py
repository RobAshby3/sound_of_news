import requests
import re
import pysynth_c as ps

bad_words = ["covid", "omicron", "scapegoat", "predator", "kill", "dead", "death", "deaths", "shooting", "shoot", "shortage", "coronavirus", "variant"]
notes = ["a", "ab", "a#", "b", "bb", "b#", "c", "cb", "c#", "d", "db", "d#", "e", "eb", "e#", "f", "fb", "f#", "g", "gb", "g#"]


def getAPIKey():
    keyfile = open("ApiKey.txt", 'r')
    key  = keyfile.read()
    keyfile.close()
    return key[0:len(key) - 1]

def main():

    headlines = []
    headlines_p = []
    headlines_decomposed = []
    key = getAPIKey()
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + key
    res = requests.get(url).json()

    for article in res['articles']:
        headlines.append(article["title"])

    exp = re.compile('[,\.!?-]')
    for headline in headlines:
        headline = exp.sub("", headline)
        headlines_p.append(headline.split(" "))

    for headline_p in headlines_p:
        for i in range(0, len(headline_p)):
            if len(headline_p[i]) != 0:
                headlines_decomposed.append(headline_p[i])

    song = []
    octave = 4;
    for i in headlines_decomposed:
        if i in bad_words and octave < 7:
            octave += 1
        for j in range(0, len(i)):
            song.append([notes[ord(i[j]) % 21] + str(octave), 16])

    ps.make_wav(song, fn = "sound_of_news.wav", bpm = 280)

if __name__ == "__main__":
    main()
