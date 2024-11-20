import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus

# Function to scrape news articles
def scrape_news(topic):
    # Encode the topic to be URL friendly
    encoded_topic = quote_plus(topic)
    
    # RSS Feed URL
    rss_url = f"https://news.google.com/rss/search?q={encoded_topic}"
    
    # Send GET request to fetch the RSS feed
    response = requests.get(rss_url)
    soup = BeautifulSoup(response.content, "xml")
    
    articles = []
    
    # Parse each item (article) in the RSS feed
    for item in soup.find_all('item'):
        title = item.title.text
        summary = item.description.text
        pub_date = item.pubDate.text
        source = item.source.text
        url = item.link.text
        
        articles.append({
            "Title": title,
            "Summary": summary,
            "Publication Date": pub_date,
            "Source": source,
            "URL": url
        })
    
    # Convert the list of articles into a pandas DataFrame
    df = pd.DataFrame(articles)
    
    # Store the data into a CSV file
    df.to_csv('news_articles.csv', index=False)

# Example usage
scrape_news("technology")  # Replace "technology" with any topic
