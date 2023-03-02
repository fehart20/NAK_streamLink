#!/usr/bin/env python
# coding: utf-8

# # Google sheet link update
#
#   import libs

#import pandas as pd
import json
#import csv
from google.oauth2 import service_account
import pygsheets
import sys
#import os
import getpass
import subprocess

username = getpass.getuser()
chrome_path = '/usr/bin/chromium %s'

# connect to google
with open('./service_account.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)
client = pygsheets.authorize(service_account_file='service_account.json')


# access spreadsheet
# only 3 of the three option is needed, we select option3
#spreadsheet_url = "https://docs.google.com/spreadsheets/d/1xwlGqzEG0fKI2hZlcI3KnBN5XuaV9mMdI_AfNTOfmkY/edit?usp=sharing"
#sheet_data = client.sheet.get('1xwlGqzEG0fKI2hZlcI3KnBN5XuaV9mMdI_AfNTOfmkY')
#sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1xwlGqzEG0fKI2hZlcI3KnBN5XuaV9mMdI_AfNTOfmkY/edit?usp=sharing')
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1kFFDm2zZXb88BOxrBPajjPAgIGAQJ8FTuiyc1Cn0V7s/edit?usp=sharing')

#print(sheet)

# open worksheet
wks = sheet.worksheet_by_title('links')
mailsheet = sheet.worksheet_by_title('Mail')
#print(wks)
#print(mailsheet)

sdate = mailsheet.get_value('G1')
print("Selected Date: " + sdate)

maxRows = wks.rows # To view the number of rows

#get shell commands for each "slot"
linkcode = wks.get_row(2)
#print(linkcode[1], linkcode[2], linkcode[3], linkcode[4], linkcode[5], linkcode[6])

#here are all the dates stored
first_column = wks.get_col(1)
#print(first_column[3], first_column[7])

#variable presets for the loop
finished = 0
found = False
search = not(found)
rowNumber=0
#print(maxRows)

#now walk over row, pick the first column and compare the date with the selected date
while search:
    rowNumber +=1
    if rowNumber >= maxRows:
        finished = 1;
        search = False;
    else:
        found = first_column[rowNumber] == sdate
        search = not(found)

#print(rowNumber)

if rowNumber < maxRows:
    print("Date found: " + first_column[rowNumber])
else:
    sys.exit('Date is not found')

#for some reasons the rowNumber is one higher than in the first_column function....
link_sel_link = wks.get_row(rowNumber+1)
#print(link_sel_link[0], link_sel_link[2])

#go over all (4) columns and pick up the entry in the selected row
for x in range(1, 5):
    #if selected element is empty exit...
    if(len(link_sel_link[x]) == 0):
        sys.exit('field is 0. Cannot be used')
    #if not split up the string
    link = link_sel_link[x].split("/")
    #print(link[3])
    if (linkcode[x] == 'nacUpdateNT'):
        youtubeLink = "https://youtu.be/"+link[3]
        subprocess.Popen(["python", "./streamLink_vlcOpener.py", youtubeLink])
        sys.exit('Finished')
    else:
        continue

print("Thanks for using streamLink")


