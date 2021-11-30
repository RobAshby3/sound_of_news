import requests
import re
from PyDictionary import PyDictionary

def getAPIKey():
    keyfile = open("ApiKey.txt", 'r')
    key  = keyfile.read()
    keyfile.close()
    return key

def main():
    headlines = []
    headlines_p = []
    headlines_decomposed = []
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + getAPIKey()
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
    

    print(headlines_decomposed)

    # dict = PyDictionary()
    # print(dict.meaning(""))

if __name__ == "__main__":
    main()
