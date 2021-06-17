import http.client


class plagiarism_checker:
    def __init__(self, user_text):
        self.user_text = user_text

    def checker(self):
        print(self.user_text)
        words = self.user_text.split(".")
        print(words)

    def speaking_time(self):
        print(self.user_text)


text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
hi = plagiarism_checker(text)
hi.checker()

conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c4fb5f1f31msh492ecef4fd3350fp1d56b0jsn45ae19f27e93",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

conn.request("GET", "/api/v1/search/q=elon+musk&num=10", headers=headers)

res = conn.getresponse()
data = res.read()

