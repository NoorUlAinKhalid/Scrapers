import csv
import os
import requests

# Create a directory called "new" if it doesn't exist
if not os.path.exists("modern1furniture"):
    os.makedirs("modern1furniture")

# Replace 'your_file.csv' with the actual CSV file name
csv_file = 'modern1furniture.csv'

# Function to download and save the image
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

# Read the CSV file and download images
with open(csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        uuid = row['UUID']
        image_url = row['IMAGE_URL']
        
        # Ensure the image URL is not empty
        if image_url:
            # Create a filename by concatenating the UUID with '.png'
            filename = os.path.join("modern1furniture", f"{uuid}.png")
            download_image(image_url, filename)
        else:
            print(f"Skipping row with empty IMAGE_URL for UUID: {uuid}")
