# Harvard Art Museums API Doc
# https://github.com/harvardartmuseums/api-docs

# Imports
import requests
import os
import random
import webbrowser
import time


def main():
    # Set up
    # Load API key from environment
    # Request API key here: https://docs.google.com/forms/d/e/1FAIpQLSfkmEBqH76HLMMiCC-GPPnhcvHC9aJS86E32dOd0Z8MpY2rvQ/viewform
    key = os.environ['harvard_art_api_key']
    base_url = 'https://api.harvardartmuseums.org/image'

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
    images = requests.get(base_url, params=payload)
    images = images.json()
    images = images['records']

    # Choose random image from list of images
    chosen_image = random.choice(images)
    chosen_image_url = chosen_image['baseimageurl']

    # Open in browser
    webbrowser.open(chosen_image_url)

    # Pause
    time.sleep(3)

if __name__ == "__main__":
    main()
