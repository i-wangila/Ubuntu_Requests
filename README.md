Ubuntu Image Fetcher

A mindful tool inspired by Ubuntu philosophy: "I am because we are."

🌍 Description

This Python program fetches images from the web and organizes them locally in a Fetched_Images directory.
It embodies the Ubuntu values of community, respect, sharing, and practicality by connecting to the internet community, handling errors gracefully, and storing resources for future sharing.

✨ Features

Fetch one or multiple image URLs at once

Creates a Fetched_Images folder automatically

Handles errors gracefully (bad URLs, failed connections)

Checks Content-Type to ensure only images are saved

Prevents downloading duplicate images

Extracts filename from URL or generates one if missing

🛠️ Requirements

Python 3.7+

Install dependencies with:

pip install requests

▶️ Usage

Run the script:

python ubuntu_fetcher.py


Example run:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URL(s) separated by spaces: https://example.com/ubuntu-wallpaper.jpg https://example.com/logo.png

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: logo.png
✓ Image saved to Fetched_Images/logo.png

Connection strengthened. Community enriched.

📜 Ubuntu Principles in Action

Community: Connects with the wider web community to fetch shared resources

Respect: Handles errors gracefully without crashing

Sharing: Organizes images into a dedicated directory for reuse

Practicality: A simple, real-world tool for mindful resource collection

“A person is a person through other persons.” – Ubuntu Philosophy

📂 Project Structure
Ubuntu_Requests/
│-- ubuntu_fetcher.py
│-- README.md
│-- Fetched_Images/   # created automatically after fetching
