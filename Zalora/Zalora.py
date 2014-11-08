
# coding: utf-8

# 1A

# In[10]:

array = [['a','b','c'],['d','e','f']]


# In[12]:

for item in sum(array,[]):
    print item


# 1B

                Have a look at "programming-tasks/top10_sample.csv"
Each line in this file represents a list of Brand in our store.
Write a script to print out a list of brand names and their occurrence counts (sorted).
                
# In[42]:

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            mapper(line)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])


# In[43]:

mr = MapReduce()

def mapper(record):
    brands = record[0].replace('[','').replace(']','').split(',')
    for brand in brands:
      mr.emit_intermediate(brand, 1)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))


# In[44]:

import csv

data = open('top10_sample.csv')
inputdata = csv.reader(data)
mr.execute(inputdata, mapper, reducer)
data.close()

#for k,v in sorted(mr.intermediate.items()):
#    print k,v


for item in sorted(mr.result):
    print item


# SQL

# a) What is the relation between Database, Schema, Tables, View in PostgreSQL / MySQL?
# b) What is the difference between a table and a view?
# c) Table reporting.items has 4 columns: Item_Code - Date - Visits - Orders
# Write a query to get total number of Visit over all Item_Codes for the day '2013-01-12'.
# Write a query to get total number of visit over all Item_Codes for every year?.
# d) As a DBA: in PostgreSQL DB, write query(s) needed to give account "buying" access to all tables currently in schema "sales", and all future Tables created in schema "sales".

# In[ ]:

select sum(Visits) from table where Date='2013-01-12'

select year(Date), sum(Visits) from table group by year(Date)


GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA sales TO buying
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA sales TO buying
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL SEQUENCES IN SCHEMA sales TO buying


# a) Write a bash script for the below set of tasks:
# [
# - connect to ftp server (host=10.11.12.13 port=22 username=helloFTP password=world)
# - download all files that have their name started with "webtrekk_marketing" into "home/Marketing Report/Data/"
# - run ZMR.py which is located in "home/Marketing Report/Scripts/"
# - run UpdateWebtrekk.sql which is located in "home/Marketing Report/Scripts/" on a PostgreSQL DB (host=10.11.12.13 port=5439 database=zalora username=helloDB password=world)
# ]
# How would you schedule the above as a cron job every day at 2.35am?

                # content of file test.sh
# Can add return code check if there are dependencies

#!/bin/sh
echo 'Start'
date

echo 'Downloading the files'
sshpass -p "world" scp -P 22 helloFTP@10.11.12.13:webtrekk_marketing.* home/Marketing Report/Data/

if ["$?" -eq 0];then
echo 'Executing ZMR'
./home/Marketing Report/Scripts/ZMR.py

echo 'Executing SQL'
EXEC SQL CONNECT TO unix:postgresql://10.11.12.13:5439/zalora USER helloDB USING world
psql -f home/Marketing Report/Scripts/UpdateWebtrekk.sql
EXEC SQL DISCONNECT

echo 'End'
else echo 'Download failed'
fi

                
                # use crontab -l to list all the crons
First execute "crontab -e"
Append cron job "35 2 * * * /home/Marketing Report/Scripts/test.sh > output.log"
Save and close the file
                
                b) Have a look at the folder "/programming-tasks/bash/"
- Write a bash script to rename all files below from "zalora-*" to "Zalora-*"
- All Zalora-* files contain a single string: "this is a test." (with a new line at the end):
    Write a shell script to change the content of those files to all uppercase.
    Write a shell script to remove all dot character (.) within those files.
                
# In[67]:

get_ipython().system(u'for file in bash/zalora*; do mv "$file" "${file//zalora/Zalora}"; done')


# In[96]:

get_ipython().system(u'ls -lrt bash')


# In[127]:

get_ipython().system(u'head bash/Zalora*')


                #toggles the case
!for file in bash/Zalora*; do sed "y/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/" $file > temp.txt; mv temp.txt $file; done
                
# In[128]:

get_ipython().system(u'head bash/Zalora*')


                !for file in bash/Zalora*; do sed 's/\.//g' $file > temp.txt; mv temp.txt $file; done
                
# In[129]:

get_ipython().system(u'head bash/Zalora*')


# In[ ]:



