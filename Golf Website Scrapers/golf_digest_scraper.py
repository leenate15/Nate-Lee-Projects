from bs4 import BeautifulSoup
import requests


# Golf Digest URLs of interest
golf_digest_homepage = 'https://www.golfdigest.com/'

# Make the URL request(s)
page_response = requests.get(golf_digest_homepage)

# Parse the URL content using Python's standard HTML parser
gd_hp_content = BeautifulSoup(page_response.content, 'html.parser') # Golf Digest Homepage Content


################# SCRAPE 'LATEST NEWS' ######################

latest_news_titles = gd_hp_content.findAll('a', {'class': 'latest-news-item-link'})

for headlines in latest_news_titles:
	print(headlines)
