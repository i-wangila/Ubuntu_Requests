import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url, content):
    """Extracts a filename from the URL or generates one if not found."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename:  
        # Generate filename based on hash of content to avoid duplicates
        hash_val = hashlib.md5(content).hexdigest()
        filename = f"image_{hash_val}.jpg"
    return filename


def download_image(url):
    """Downloads an image from the given URL into Fetched_Images directory."""
    try:
        # Create directory if it doesn’t exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Validate content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping {url} — not an image (Content-Type: {content_type})")
            return

        # Extract or generate filename
        filename = get_filename_from_url(url, response.content)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs
    urls = input("Please enter image URL(s) separated by spaces: ").split()

    for url in urls:
        download_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
