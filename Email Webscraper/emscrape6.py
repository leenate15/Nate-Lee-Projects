from bs4 import BeautifulSoup
from urllib.request import urlopen

############################################################
####################### FUNCTIONS ##########################
############################################################

#######################################################################
# Creates a Beautiful Soup object out of the website
def create_BS_object(URL):
    BSobj = None
    try:
        BSobj = BeautifulSoup(urlopen(URL).read(), "lxml")
    except:
        if URL == None:
            print('No contact page found.')
        else:
            print(URL,'is not a valid URL.')
    return BSobj

#######################################################################
# Specifies which tag to search for in the BS object
def tag_search(BS_Obj,tag):
    if BS_Obj == None:
        tag_search = []
    else:
        tag_search = BS_Obj.findAll(tag)
    return tag_search

#######################################################################
# Function that finds and returns all instances of a substring within a string
# SOI: String of Interest
# SSOI: Substring of Interest
def str_find_all(SOI, SSOI):
    SSOI_instances = [] # list of substring instances
    SOI_copy = SOI # Make a copy of the SOI
    counter, idx_adjust, SSOI_loc = 0,0,0 # Set a counter, an index adjustment, and an initial SSOI index location
    while len(SOI_copy) > 1: # As long as the SOI has more than one character
        if counter > len(SOI): # Prevent an infinite loop
            print("Kill")
            exit()
        SSOI_loc = SOI_copy.find(SSOI) # Look for the first instance of the SSOI in the SOI
        if counter == 0 and SSOI_loc == -1: # If the SSOI is not found on the first pass through, there are no emails in the SOI
            break
        if SSOI_loc > -1: # A returned '-1' indicates no instance found of the substring
            SOI_copy = SOI_copy[SSOI_loc+1:] # After an instance of the SSOI is found, chop off the already search part of the SOI
            SSOI_instances.append(SSOI_loc + counter + idx_adjust) # Save the index of the instance found - MAY WANT TO REMOVE
            idx_adjust = SSOI_loc + idx_adjust # Reset the idx_adjust to count the offset
        else:
            break # If no more instances occur, break out of the loop
        counter += 1 # Iterate the counter
    return SSOI_instances # Return all of the instances of the SSOI


#######################################################################
def find_emails2(tag_obj_collection):
    email_domains = ['.com','.net','.org'] # These are the possible email domains
    emails, em_beg_idxs, dom_end_idxs = [],[],[] # Stores the emails, indices of the beginnings & ends of emails
    for tag_obj in tag_obj_collection:
        possible_email = str(tag_obj) # Convert the tag object into a string
        # Start the email search algorithm
        for domain in email_domains: # Iterate through the possible domains
            if domain in possible_email and '@' in possible_email: # If both an '@' and domain is found
                at_instances = str_find_all(possible_email,'@') # Store all the instances of '@'
                for dom_idx in str_find_all(possible_email,domain): # Store all the instances of the email domain
                    # print(dom_idx+len(domain))
                    dom_end_idxs.append(dom_idx+len(domain))
                # The idea is that you can search backwards from an '@' to find
                # the first character that is not a letter and assume from that
                # index to the end of the domain is the email
                for at_idx in at_instances: # For all the '@' instances
                    for str_idx in range(at_idx-1,0,-1):
                        if possible_email[str_idx].isalnum() == False: #is_letter(possible_email[str_idx]) == False:
                            em_beg_idxs.append(str_idx + 1)
                            break
                if em_beg_idxs[0] < dom_end_idxs[0] and possible_email[em_beg_idxs[0]:dom_end_idxs[0]].endswith(domain) and ('@' in possible_email[em_beg_idxs[0]:dom_end_idxs[0]]):
                    emails.append(possible_email[em_beg_idxs[0]:dom_end_idxs[0]])
                    break
    if len(emails) > 1:
        emails = list(set(emails)) # Remove any duplicate emails
    return emails

#######################################################################
def find_contact_page(div_obj_collection):
    contact_URL = None
    regex = 'href="' # Each contact page URL (and pretty much every other URL) should have an href=" before it and an " after
    URL_domains = ['.com','.net','.org','.php']
    for div_obj in div_obj_collection:
        possible_contact_page = str(div_obj)
        counter = 0
        while len(possible_contact_page) > len(regex):
            URL_present = possible_contact_page.find(regex)
            if URL_present > -1:
                possible_contact_page = possible_contact_page[URL_present+len(regex):]
                URL_end = possible_contact_page.find('"')
                possible_contact_URL = possible_contact_page[0:URL_end]
                if possible_contact_URL.find('contact') > -1:
                    for domain in URL_domains:
                        if domain in possible_contact_URL:
                            contact_URL = possible_contact_URL
                            break
                    break
            elif URL_present == -1:
                break
            elif counter > 500:
                print('I got stuck.')
                break
            counter += 1
        if contact_URL != None:
            break
    return contact_URL

#######################################################################
def is_URL():
    return
############################################################
########################## END #############################
############################################################



############################################################
################### FUNCTION GRAVEYARD #####################
############################################################

# The function graveyard consists of functions that were written and never used
# or written for previous versions of emscrape but are no longer used. The functions
# below are not listed in any particular order. This section is just to keep track
# of code that was written and could be useful in the future.


#######################################################################
# Search for, identify, and extract URLs:
def find_contact_URL(website_obj):
    contact_URL = None # Initialize a contact URL variable
    URLs = [] # Used to store URLs found
    URL_domain_idx = []
    all_divs = tag_search(BS_Obj,'div')
    for div_obj in all_divs:
        num_contacts = str_find_all(div_obj,'contact')
    http_idx = str_find_all(str(website_obj),'http')
    URL_domains = ['.com','.net','org']
    for ext in URL_domains:
        URL_domain_idx = str_find_all(str(website_obj),ext)
        break
    if len(email_ext) == len(http_idx):
        for idxs in range(len(email_ext)):
            URLs.append(str(website_obj)[http_idx[idxs]:URL_ext_idx[idxs]+len(URL_ext_idx[idxs])])
    else:
        print("Mismatching number of http to URL extensions")
    return contact_URL

#######################################################################
# Searches all collected tags for emails
def find_emails(tag_obj_collection):
    emails = []
    for tag_obj in tag_obj_collection: # Iterate through all tag objects collected
        str_tag_obj = str(tag_obj) # Turn the tag object into a string
        at_present = str_tag_obj.find('@') # Search the string for an '@'
        if at_present > -1: # If there is an '@' found
            new_email = check_and_gather_email(str_tag_obj) # Verify that there is an email and collect it
            if new_email.find('@') > -1: # Just make sure the gathered email is an email, not a URL by mistake
                emails.append(new_email) # Finally add the email
    if len(emails) > 1:
        emails = list(set(emails)) # Erase any duplicate emails
    return emails

#######################################################################
# Combines original gather_email & is_email functions (Function Graveyard)
def check_and_gather_email(possible_email):
    dom_check = False # Initialize a URL domain checker
    email_domains = ['.com','.net','.org'] # List of all possible email domains that could be used in an email
    dom_used = None # Initialize the used domain to save for later
    dom_end_idxs = [] # List to collect the end indices of all found domain instances
    email = []
    for domain in email_domains: # Loop through all possible URL domain
        if len(str_find_all(possible_email,domain)) > 0:
            dom_check = True # If an instance is found, that check is true
            dom_used = domain # Save the domain that was used
            for idx in str_find_all(possible_email,domain):
                dom_end_idxs.append(idx + len(domain)) # Save the ending index of the domain
    if dom_check == True:
        email_beg_markers = ['mailto:',':','>','"','\'','" ', '\' ',': '] # These are the possible symbols that could indicate the beginning of an email
        for marker in email_beg_markers:
            marker_idx = possible_email.find(marker)
            if marker_idx > -1:
                for end_idx in dom_end_idxs:
                    if marker_idx < end_idx:
                        email = possible_email[marker_idx+len(marker):end_idx]
                        if is_letter(email[0]) == False:
                            email = email[1:]
                        break
                break
    return email

#######################################################################
# Quick function to determine if a character is a letter or not
def is_letter(char):
    verdict = False
    if (ord(char) > 64 and ord(char) < 91) or (ord(char) > 96 and ord(char) < 123):
        verdict = True
    return verdict

#######################################################################
# Function that verifies whether or not a string is an email
def is_email(possible_email):
    verdict,at_check,ext_check = False,False,False # Initialize a verdict, @ checker, and URL extension checker
    email_extensions = ['.com','.net','.org'] # List of all possible URL extensions that could be used in an email
    ext_used = None # Initialize the used extension to save for later
    ext_end_idx = None # Initialize an extension used index
    if possible_email.find('@') > -1: # Check if there are any @s
        at_check = True
    for extensions in email_extensions: # Loop through all possible URL extensions
        if possible_email.find(extensions) > -1:
            ext_check = True # If an instance is found, that check is true
            ext_used = extensions # Save the extension that was used
            ext_end_idx = possible_email.find(extensions) + len(extensions) - 1 # Save the ending index of the extension
            break
    if at_check == True and ext_check == True:
        verdict = True # If there is both an @ and a URL extension in the string, it's likely that there is an email
    return [verdict,ext_used,ext_end_idx]

#######################################################################
# Once a possible email is identified, this function gathers the whole string
def gather_email(str_tag_obj):
    print(str_tag_obj)
    is_email_verdict = is_email(str_tag_obj) # First verify that there is an email present
    email = 'None' # Initialize an email variable
    if is_email_verdict[0] == True: # If there is in fact an email present
        email_beg_markers = ['mailto:',':','>','"','\''] # These are the possible symbols that could indicate the beginning of an email
        email_end_marker = is_email_verdict[1] # This is the URL extension
        for marker in email_beg_markers:
            marker_idx = str_tag_obj.find(marker)
            if marker_idx > -1:
                # print(marker_idx,marker,marker_idx+len(marker),is_email_verdict[2])
                # print(str_tag_obj[marker_idx+len(marker):is_email_verdict[2]+1])
                email = str_tag_obj[marker_idx+len(marker):is_email_verdict[2]+1]
                break
    if is_letter(email[0]) == False:
        email = email[1:]
    return email
