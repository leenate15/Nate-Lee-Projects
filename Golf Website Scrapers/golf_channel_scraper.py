# Import libraries
from bs4 import BeautifulSoup
import requests


# Golf Channel URLs of interest
golf_channel_homepage = 'https://www.golfchannel.com/'

# Make the URL request(s)
page_response = requests.get(golf_channel_homepage)

# Parse the URL content using Python's standard HTML parser
gc_hp_content = BeautifulSoup(page_response.content, 'html.parser')


################# SCRAPE 'TOP STORIES' ######################

# Gather all the top stories and links from Golf Channel
print('Golf Channel Top Stories')
top_stories = gc_hp_content.findAll('li', {'class': 'views-row headline'})

# Print the headlines and links
for headlines in top_stories:
	print(headlines.a)


################# SCRAPE 'WHAT'S HAPPENING NOW' ####################
print('Golf Channel Happening Now')
happening_now = gc_hp_content.findAll('article', {'class': 'main-content teaser_vertical'})

# Print the headlines and links
for headlines in happening_now:
	print(headlines.h1.a)