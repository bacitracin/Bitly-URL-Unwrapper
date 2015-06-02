# -*- coding: utf-8 -*-
"""
Edited on Mon May 11 13:00:14 2015

Shortened Twitter Link Unwrapper
(Doesn't work on all vanity urls, best to use http://t.co link from 
the Radian6 / Sysomos CSV Download to avoid issues.)

@author: Tracy
"""
#pip install these packages if you don't already have them
import urllib2 
import csv


short_urls = []
unwrapped_urls = []

#Update name of row with shortened links here
f = open('shortlinks20.csv')
csv_f = csv.reader(f)

for row in csv_f:
    short_urls.append(row) 
    
    try:
        response = urllib2.urlopen(row[0], timeout = 60)
        url_destination = response.geturl()   
        unwrapped_urls.append(url_destination)

    except urllib2.HTTPError, e:
        url_destination = "Error HTTP Error"
        unwrapped_urls.append(url_destination)
        
    except urllib2.URLError, e:
        url_destination = "Error URL Error"
        unwrapped_urls.append(url_destination)
   
    except urllib2.HttpException, e:
        url_destination = "Error HTTP Exception"
        unwrapped_urls.append(url_destination)
    
    except Exception:
        url_destination = "Exception"
        unwrapped_urls.append(url_destination)   
        
    else: 
        continue
    
zipped = zip(short_urls, unwrapped_urls) 
   
f.close()

#Update the name of the resulting file
with open('shortlinks20UNWRAP.csv', 'wb') as newfile:
    writer = csv.writer(newfile)
    writer.writerows(zipped)

newfile.close()

print("All Done! Check it out!")


    