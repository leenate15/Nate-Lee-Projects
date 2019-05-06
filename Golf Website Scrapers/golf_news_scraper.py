from bs4 import BeautifulSoup
import requests


# URLs of interest
golf_channel_homepage = 'https://www.golfchannel.com/'
golf_digest_homepage = 'https://www.golfdigest.com/'

# Make the URL request(s)
golf_channel_page_response = requests.get(golf_channel_homepage)
golf_digest_page_response = requests.get(golf_digest_homepage)

# Parse the URL content using Python's standard HTML parser
gc_hp_content = BeautifulSoup(golf_channel_page_response.content, 'html.parser') # Golf Channel Homepage Content
gd_hp_content = BeautifulSoup(golf_digest_page_response.content, 'html.parser') # Golf Digest Homepage Content


################# SCRAPE 'TOP STORIES' ######################

golf_news_headlines = []

# Gather all the top stories and links from Golf Channel
golf_channel_top_stories = gc_hp_content.findAll('li', {'class': 'views-row headline'})
golf_channel_happening_now = gc_hp_content.findAll('article', {'class': 'main-content teaser_vertical'})
golf_digest_latest_news = gd_hp_content.findAll('a', {'class': 'latest-news-item-link'})

BS_objects = [golf_channel_top_stories, golf_channel_happening_now, golf_digest_latest_news]

for objects in BS_objects:
	for headlines in objects:
		if objects == golf_channel_top_stories:
			golf_news_headlines.append(headlines.a)
		elif objects == golf_channel_happening_now:
			golf_news_headlines.append(headlines.h1.a)
		elif objects == golf_digest_latest_news:
			golf_news_headlines.append(headlines)

print(golf_news_headlines)

# # Print the headlines and links
# for headlines in top_stories:
# 	print(headlines.a)


# ################# SCRAPE 'WHAT'S HAPPENING NOW' ####################
# print('Golf Channel Happening Now')


# # Print the headlines and links
# for headlines in happening_now:
# 	print(headlines.h1.a)


# ################# SCRAPE 'LATEST NEWS' ######################



# for headlines in latest_news_titles:
# 	print(headlines)