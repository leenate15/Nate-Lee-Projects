# first = '=IF(COUNTIF(\'Prototype Order Sheet\'!G2:G,A'
# first_2 = '=IF(COUNTIF(\'Prototype Order Sheet\'!E2:E,A'
# second = ')=1,"SOLD","")'
#
# for j in range(1,90):
#     print(first+str(j)+second)
# for i in range(90,190):
#     print(first_2+str(i)+second)


# for i in range(5,38):
#     print('=J'+str(i)+'-B15')


# import pandas as pd
# import time
#
# email_open_data = pd.DataFrame([])
# email_lists = ['Thirteenth','Fourteenth','Fifteenth'] # Change the email lists here
# campaign_group = '5'
#
#
# month = time.strftime('%m') # Get the month
# day = str(int(time.strftime('%d')))
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
# # MAKE SURE TO CHANGE THE OPENED DATE TO THE CORRECT DATE BEFORE RUNNING SCRIPT
# for list in email_lists:
#     for num in range(1,3):
#         df = pd.read_csv('C:/Users/Nate/Downloads/members_Catering_'+list+'_50_Email_'+str(num)+'_opened_'+months[int(month)-1]+'_'+day+'_2019.csv')
#         email_open_data = email_open_data.append(df)
# print(df)
#
# # EOD_size = 0
#
# # for list in email_lists:
# #     for num in range(1,3):
# #         # df = "C:/Users/Nate/Downloads/members_Catering_"+list+"_50_Email_"+str(num)+"_opened_Feb_6_2019.csv" # Manual date entry
# #         df = 'C:/Users/Nate/Downloads/members_Catering_'+list+'_50_Email_'+str(num)+'_opened_'+months[int(month)-1]+'_'+day+'_2019.csv' # Automated date entry (on day of)
#
# print(email_open_data)
#
# email_open_data.to_csv('C:/Users/Nate/Downloads/Campaign Group '+campaign_group+' - Opened Emails.csv')
