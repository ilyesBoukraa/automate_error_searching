#! python3

import pyperclip
import webbrowser

def google_search(query):
    base_url = "https://www.google.com/search?q="
    search_url = base_url + query
    webbrowser.open(search_url)

if __name__ == "__main__":
    query = pyperclip.paste()
    google_search(query)