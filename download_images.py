import csv
import os
import requests

if not os.path.exists("modern1furniture"):
    os.makedirs("modern1furniture")
csv_file = 'modern1furniture.csv'

def download_image(image_url, filename):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")

with open(csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        uuid = row['UUID']
        image_url = row['IMAGE_URL']
        
        if image_url:
            filename = os.path.join("modern1furniture", f"{uuid}.png")
            download_image(image_url, filename)
        else:
            print(f"Skipping row with empty IMAGE_URL for UUID: {uuid}")
