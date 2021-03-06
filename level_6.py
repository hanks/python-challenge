#!usr/bin/env python
# coding: utf-8

'''
question with zip function in python
1. change 'html' to 'zip' in the web site to 
download a zip file
2. download the channel.zip file and read the 
readme file in it then to solve it.
3. start from 90052.txt
4. end with 'Collect the comments'
5. use zipfile object to collect zip file comment info
'''

import zipfile
import re

start = '90052'
zipFileName = 'channel.zip'
file = zipfile.ZipFile(zipFileName, 'r')

nextIndex = start 
# need to collect zip file comment info
comments = []

while True:
    data = file.read(nextIndex + '.txt')
    comments.append(file.getinfo(nextIndex + '.txt').comment)
    print 'File', nextIndex, ':', data
    nextIndex = ''.join(re.findall(r'[0-9]', data))
    # when there is no next index, break
    if len(nextIndex) == 0:
        break

# print the comments
print ''.join(comments)

# the next website is :www.pythonchallenge.com/pc/def/hockey.html
# then you need to do a small quiz...
# It is in the air, look at the letters
# so the final answer is oxygen...
# replace hockey with oxygen, and you will find the true site.
        

