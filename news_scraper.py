import requests
from bs4 import BeautifulSoup
import time

def scrape_news_headlines(url):
    """
    Function to scrape news headlines from a website
    """
    try:
        # Step 1: Send a request to the website
        print(f"Fetching data from: {url}")
        
        # Add headers to make the request look like it's coming from a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("✅ Successfully fetched the webpage!")
        else:
            print(f"❌ Failed to fetch webpage. Status code: {response.status_code}")
            return []
            
        # Step 2: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        print("✅ HTML content parsed successfully!")
        
        # Step 3: Find all headlines (we'll look for common headline tags)
        headlines = []
        
        # Common tags used for headlines: h1, h2, h3, title, and specific classes
        headline_tags = ['h1', 'h2', 'h3']
        
        print("🔍 Searching for headlines...")
        
        for tag in headline_tags:
            found_headlines = soup.find_all(tag)
            for headline in found_headlines:
                text = headline.get_text().strip()
                if text and len(text) > 10:  # Only keep meaningful headlines
                    headlines.append(text)
                    
        # Also look for common news headline classes (these vary by website)
        common_classes = [
            'headline', 'title', 'post-title', 'entry-title', 
            'article-title', 'news-title', 'story-headline'
        ]
        
        for class_name in common_classes:
            elements = soup.find_all(class_=class_name)
            for element in elements:
                text = element.get_text().strip()
                if text and len(text) > 10:
                    headlines.append(text)
        
        # Remove duplicates while preserving order
        unique_headlines = []
        seen = set()
        for headline in headlines:
            if headline not in seen:
                unique_headlines.append(headline)
                seen.add(headline)
                
        print(f"✅ Found {len(unique_headlines)} unique headlines!")
        return unique_headlines
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        return []

def save_headlines_to_file(headlines, filename="news_headlines.txt"):
    """
    Function to save headlines to a text file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("NEWS HEADLINES\n")
            file.write("=" * 50 + "\n\n")
            
            for i, headline in enumerate(headlines, 1):
                file.write(f"{i}. {headline}\n\n")
                
        print(f"✅ Headlines saved to {filename}")
        
    except Exception as e:
        print(f"❌ Error saving file: {str(e)}")

def main():
    """
    Main function to run the web scraper
    """
    print("🚀 Starting News Headlines Web Scraper")
    print("=" * 50)
    
    # List of popular news websites you can try
    # (Note: Always check robots.txt and terms of service before scraping)
    sample_urls = [
        "https://news.ycombinator.com/",  # Hacker News
        "https://www.bbc.com/news",       # BBC News
        "https://edition.cnn.com/",       # CNN
    ]
    
    print("Sample news websites you can try:")
    for i, url in enumerate(sample_urls, 1):
        print(f"{i}. {url}")
    
    # Get URL from user
    print("\n📝 Enter a news website URL (or press Enter to use BBC News):")
    user_url = input().strip()
    
    # Use default if no input
    if not user_url:
        user_url = "https://www.bbc.com/news"
        print(f"Using default URL: {user_url}")
    
    # Scrape headlines
    headlines = scrape_news_headlines(user_url)
    
    if headlines:
        print(f"\n📰 Found Headlines ({len(headlines)} total):")
        print("-" * 50)
        
        # Display first 10 headlines
        for i, headline in enumerate(headlines[:10], 1):
            print(f"{i}. {headline}")
            
        if len(headlines) > 10:
            print(f"... and {len(headlines) - 10} more headlines")
        
        # Save to file
        print(f"\n💾 Saving headlines to file...")
        save_headlines_to_file(headlines)
        
        print(f"\n✅ Task completed successfully!")
        print(f"📄 Check the 'news_headlines.txt' file in your current directory")
        
    else:
        print("❌ No headlines found. Try a different website.")

# Run the program
if __name__ == "__main__":
    main()