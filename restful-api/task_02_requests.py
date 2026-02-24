#!/usr/bin/python3
"""Module that fetches posts from JSONPlaceholder"""

import requests
import csv


def fetch_and_print_posts():
    """Function fetches posts from JSONPlaceholder"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print(i)
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Function fetches and saves posts from JSONPlaceholder"""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        structured_posts = [
            {"id": i["id"], "title": i["title"], "body": i["body"]}
            for i in posts]
        with open("posts.csv", "w", encoding="utf-8") as csv_file:
            field_names = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for j in structured_posts:
                writer.writerow[j]
        print("Posts saved to posts.csv successfully.")
    else:
        print("Failed to fetch posts.")


fetch_and_print_posts()
