##################### LIBRARIES ############################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import emscrape6 as es
import csv
import pandas as pd


######################### END ##############################

###################### BEGIN CODE #######################

# Import and store a website list to scrape

# Using the CSV library to import the websites
# URL_list = []
# with open('websites.csv') as f: # Once this statement ends, the file closes
#     reader = csv.reader(f) # Open the file
#     for row in reader: # Loop over and store while the file is open
#         URL_list.append(row[0])

# Use pandas instead of the csv library
URL_list = pd.read_csv('websites2.csv')

# URL_list = ['http://5flavors.com/']
# URL_list = ["http://blueplatechicago.com/contact-us/","http://www.adamospizzaandcatering.com/contact-us/","http://www.allnaturalchicago.com/contact-us/"]

#Tag List
tag_list = ['a','p','div','span']

# Open the websites and extract the emails - VERSION 2
email_list = []
final_email_list = []
URL_counter = 0
for URL in URL_list['Website']:

    print('Searching for',URL_list['Name'][URL_counter],'\'s email.' )
    URL_counter += 1

    main_page = es.create_BS_object(URL) # Creates BS object of website main page
    tag_counter = 0 # Counts the number of tags tested
    for tag in tag_list:
        tag_counter += 1
        tag_obj_collection = es.tag_search(main_page, tag)
        found_emails = es.find_emails2(tag_obj_collection)
        if len(found_emails) > 0:# and found_emails[0] != 'None':
            for email in found_emails:
                final_email_list.append([email,URL])
            break
        elif len(found_emails) == 0 and tag_counter == len(tag_list):

            # print('Searching contact page ...')

            div_obj_collection = es.tag_search(main_page, 'div')
            contact_URL = es.find_contact_page(div_obj_collection)
            if contact_URL != None:
                if contact_URL.startswith("http") == False:
                    contact_URL = URL[:URL.rfind('/')]+contact_URL
            contact_page = es.create_BS_object(contact_URL)
            tag_counter2 = 0
            for tag2 in tag_list:
                tag_counter2 += 1
                tag_obj_collection_2 = es.tag_search(contact_page, tag2)
                contact_found_emails = es.find_emails2(tag_obj_collection_2)
                if len(contact_found_emails) > 0:
                    for contact_email in contact_found_emails:
                        final_email_list.append([contact_email,URL])
                    break
                elif tag_counter2 == len(tag_list) and len(contact_found_emails) == 0:
                    final_email_list.append(['',URL])
            break
# print(final_email_list)

# Write the email list to CSV file in the working directory
with open('email_list2.csv', 'w',newline='') as myFile:
    writer = csv.writer(myFile,delimiter=',')
    writer.writerows(final_email_list)

print("Writing complete")
