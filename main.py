import http.client
import tkinter as tk

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

conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c4fb5f1f31msh492ecef4fd3350fp1d56b0jsn45ae19f27e93",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
}


class PlagiarismChecker:
    def __init__(self, user_text):
        self.user_text = user_text

    def checker(self):
        print(self.user_text)
        words = self.user_text.split(".")
        print(words)
        conn.request("GET", "/api/v1/search/q=elon+musk&num=10", headers=headers)

        res = conn.getresponse()
        data = res.read()
        print(data)

    def speaking_time(self):
        print(self.user_text)

    def submit(self):
        txt = t.get("1.0", "end")
        self.user_text = txt
        self.checker()

    def get_text(self):
        print(self.user_text)


hi = PlagiarismChecker('')

window = tk.Tk()
label = tk.Label(text="Topic", bg='black', fg='#fff')
label1 = tk.Label(text="Text", bg='black', fg='#fff')
entry = tk.Entry()

frame = tk.Frame(window, width=400, height=20, background='black')
frame1 = tk.Frame(window, width=400, height=20, background='black')
frame2 = tk.Frame(window, width=300, height=20, background='black')
frame3 = tk.Frame(window, width=300, height=20, background='black')

t = tk.Text(window, height=20, width=45)
button = tk.Button(window, text="Submit", width=10, command=hi.submit)
window.configure(background='black')

frame.pack(fill=None, expand=False)
label.pack()
entry.pack()
frame1.pack(fill=None, expand=False)
label1.pack()
t.pack()
frame2.pack(fill=None, expand=False)
button.pack()
frame3.pack(fill=None, expand=False)


window.mainloop()

