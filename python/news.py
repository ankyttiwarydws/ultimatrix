import requests
import datetime
import os
import json

JSON_FILE = os.path.join('data', 'news', 'news-data.json')  # You can change this to any filename you want
API_KEY = 'pub_29a24501e65546a183c11fb52dea5171'  # Replace this with your actual key
OUTPUT_DIR = 'data\news\news_articles'

def fetch_news(category='business', country='in', language='en', max_articles=10):
    url = f'https://newsdata.io/api/1/news?apikey={API_KEY}&country={country}&language={language}&category={category}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('results', [])[:max_articles]
    print(articles)
    return articles

def transform_article(article, category='business'):
    return {
        "title": article.get("title", "Untitled"),
        "shortDesc": article.get("description", "No short description available."),
        "timestamp": article.get("pubDate", ""),  # Use raw pubDate or format as needed
        "synopsis": article.get("content", "No synopsis available."),
        "fullStory": [
            article.get("content", "No content available."),
            f'{article.get("source_id", "").title()} says, “More to explore at source.”'
        ],
        "link": article.get("link", ""),
        "imageSrc": "/assets/img/default.jpg",  # Placeholder: you can enhance this later
        "imageAlt": "News image",
        "author": "Ultimatrix Team",  # Placeholder: you can enhance this later
        # "sourceURL": article.get("link", ""),
        "sourceURL": article.get("source_url", ""),
        "sourceName": article.get("source_name", "Unknown Source"),
        "imageCredit": "NewsAPI / CC BY-SA 4.0",
        "category": category,
        "date": article.get("pubDate", "")[:10]
    }

def append_transformed_articles_to_json(articles, category):
    structured_articles = [transform_article(article, category) for article in articles]

    os.makedirs(os.path.dirname(JSON_FILE), exist_ok=True)

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.extend(structured_articles)

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(structured_articles)} structured articles to {JSON_FILE}")

# === Run this ===
if __name__ == '__main__':
    category = 'business'  # change to 'sports', 'technology', etc.
    articles = fetch_news(category=category)
    append_transformed_articles_to_json(articles, category)
