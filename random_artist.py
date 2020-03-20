# Harvard Art Museums API Doc
# https://github.com/harvardartmuseums/api-docs

# Imports
import requests
import os
import random
import webbrowser
import time


def main():
    '''
    Script to load the webpage for a random artist from the Harvard Art Collections
    '''
    # Set up
    # Load API key from environment
    # Request API key here: https://docs.google.com/forms/d/e/1FAIpQLSfkmEBqH76HLMMiCC-GPPnhcvHC9aJS86E32dOd0Z8MpY2rvQ/viewform
    key = os.environ['harvard_art_api_key']
    base_url = 'https://api.harvardartmuseums.org/person'

    # Parameters
    payload = {'apikey': key}

    # Get total pages to choose a random one to query
    r = requests.get(base_url, params=payload)
    pages = r.json()
    pages = pages['info']['pages']
    time.sleep(.5)

    # Choose a random page of results
    random_page = random.randint(1, pages)

    # Update payload parameters with random page number
    payload['page'] = random_page

    # Get images for that page
    artists = requests.get(base_url, params=payload)
    artists = artists.json()
    artists = artists['records']

    # Choose random image from list of images
    chosen_artist = random.choice(artists)
    print(chosen_artist)
    chosen_artist_url = chosen_artist['url']

    # Open in browser
    webbrowser.open(chosen_artist_url)

    # Open Wikipedia page in another tab
    if 'wikipedia_id' in chosen_artist.keys():
        wiki_id = chosen_artist['wikipedia_id']
        base_wiki_url = 'http://en.wikipedia.org/?curid='
        artist_wiki_url = base_wiki_url + wiki_id

        webbrowser.open(artist_wiki_url)
    else:
        print('No Wikipeda ID available')

    # Pause
    time.sleep(1)

if __name__ == "__main__":
    main()
