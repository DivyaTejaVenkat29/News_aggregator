import pandas as pd
from textblob import TextBlob
import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

CATEGORY_KEYWORDS = {
    "Politics": ["election", "government", "politician", "parliament", "president", "voter"],
    "Technology": ["tech", "AI", "machine learning", "software", "robotics", "innovation"],
    "Sports": ["sports", "football", "cricket", "athlete", "tournament", "world cup", "team"]
}

def create_phrase_matcher():
    """Creates a PhraseMatcher for detecting phrases related to categories."""
    matcher = PhraseMatcher(nlp.vocab)
    for category, keywords in CATEGORY_KEYWORDS.items():
        patterns = [nlp.make_doc(keyword) for keyword in keywords]
        matcher.add(category, None, *patterns)
    return matcher

def categorize_articles(file_path):
    df = pd.read_csv(file_path)
    matcher = create_phrase_matcher()

    def get_category(title):
        doc = nlp(title.lower())
        
        # Check for exact matches using PhraseMatcher
        matches = matcher(doc)
        for match_id, start, end in matches:
            category = nlp.vocab.strings[match_id]
            return category
        
        # Fallback to basic keyword matching
        for category, keywords in CATEGORY_KEYWORDS.items():
            if any(keyword in doc.text for keyword in keywords):
                return category
        return "Other"

    # Apply categorization to titles and save to CSV
    df["Category"] = df["Title"].apply(get_category)
    df.to_csv(file_path, index=False)
    print(f"Categorized articles saved to {file_path}.")

if __name__ == "__main__":
    categorize_articles("../scraper/news_articles.csv")
