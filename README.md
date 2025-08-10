# News Headlines Web Scraper

A Python-based web scraper that automatically extracts news headlines from websites and saves them to a text file. 

##  Project Overview

This web scraper visits news websites, extracts headlines using HTML parsing, and saves the results to a text file. 

##  Features

-  Automatic headline extraction from news websites
-  **Smart parsing** using multiple HTML tag detection (h1, h2, h3, title tags)
-  **File output** saves headlines to `news_headlines.txt`
-  **Error handling** with user-friendly messages
- **Interactive interface** with sample website suggestions
-  **Duplicate removal** ensures unique headlines only
-  **Progress indicators** show scraping status

##  Technologies Used

- **Python 3.7+**
- **requests** - For HTTP requests and webpage fetching
- **BeautifulSoup4** - For HTML parsing and element extraction
- **Built-in libraries**: `time`, `os`, `sys`

## Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher installed
- Internet connection for downloading web pages
- Basic understanding of command line operations

##  Installation

### Step 1: Clone or Download
bash
# Clone the repository (if using Git)
git clone <repository-url>
cd news-scraper

# Or download the files manually


### Step 2: Install Required Libraries

**Option A: Using pip**
`bash
pip install requests beautifulsoup4


**Option B: Using conda (if you have Anaconda)**
bash
conda install requests beautifulsoup4


**Option C: Using requirements.txt**
`bash
pip install -r requirements.txt


### Step 3: Verify Installation
```bash
python -c "import requests, bs4; print('All libraries installed successfully!')"


##  Usage

### Basic Usage

1. **Run the scraper:**
   bash
   python news_scraper.py
   

2. **Choose a website:**
   - Press Enter to use BBC News (default)
   - Or enter a custom news website URL

3. **View results:**
   - Headlines will be displayed in the terminal
   - All headlines saved to `news_headlines.txt`



##  Project Structure


news-scraper/
│
├── news_scraper.py          # Main scraper script
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── news_headlines.txt      # Output file (generated)
└── examples/
    ├── sample_output.txt   # Example output
    └── test_scraper.py     # Testing utilities




##  Sample Output

### Terminal Output

 Starting News Headlines Web Scraper
==================================================
 Enter a news website URL (or press Enter to use BBC News):

Fetching data from: https://www.bbc.com/news
 Successfully fetched the webpage!
 HTML content parsed successfully!
 Searching for headlines...
 Found 25 unique headlines!

 Found Headlines (25 total):
--------------------------------------------------
1. Breaking: Major economic summit begins today
2. Technology sector shows strong growth
3. Climate change talks resume in Geneva


 Saving headlines to file...
 Headlines saved to news_headlines.txt
 Task completed successfully!


### File Output (`news_headlines.txt`)

NEWS HEADLINES
==================================================

1. Breaking: Major economic summit begins today

2. Technology sector shows strong growth

3. Climate change talks resume in Geneva

4. New breakthrough in renewable energy research



##  How It Works

1. **HTTP Request**: Sends GET request to target website
2. **HTML Parsing**: Uses BeautifulSoup to parse webpage structure
3. **Element Extraction**: Searches for common headline tags and classes
4. **Text Cleaning**: Removes HTML tags and extra whitespace
5. **Deduplication**: Filters out duplicate headlines
6. **File Writing**: Saves results to formatted text file

