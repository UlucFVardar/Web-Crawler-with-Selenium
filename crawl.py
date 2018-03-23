# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#need libs for selenium 
from selenium import webdriver
import time
#---

#to convert to strings to a english coded strings
def conv(a):
    a = str(a)
    for x in range(0, len(a)):
        a = a.replace('\"', '\'')
        a = a.replace('İ', 'I')
        a = a.replace('Ş', 's')
        a = a.replace('Ç', 'C')
        a = a.replace('Ü', 'U')
        a = a.replace('Ö', 'O')
        a = a.replace('ş', 's')
        a = a.replace('ğ', 'g')
        a = a.replace('ı', 'i')
        a = a.replace('ö', 'o')
        a = a.replace('ü', 'u')
        a = a.replace('ç', 'c')
    return a
#----

def crawlNewsStand():
	#to connect newstand.google selenium set up.
	chrome_path="./chromedriver" #chrome driver path
	driver =webdriver.Chrome(chrome_path)
	driver.get('https://newsstand.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYUnlMVlJTR2dKVVVpZ0FQAQ')
	time.sleep(5)
	#--- after pages open, program needs time because information of news dont exist the page at that time.

	#These for the header news information
	ab=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[3]/div/div/article/div[2]/div[1]/a/span[1]')
	re=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[3]/div/div/article/div[3]/div[1]/div/span')
	be=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[3]/div/div/article/div[3]/div[1]/div/div/time')
	li=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[3]/div/div/article/a')
	if len(ab)==len(re)==len(be)==len(li)==1 :
		header=conv(ab[0].text)
		resource=conv(re[0].text)
		before_time=conv(be[0].text)
		newsURL=li[0].get_attribute("href")
		print "baslik ",header
		print "Kaynak ",resource
		print "Sure   ",before_time
		print "Link   ",newsURL,"\n\n"  
	#---

	#For take informations about the news on the page in one page always exists 70 news
	for i in range (1,70):
		print str(i)+". haber!"
		ab=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[2]/div[1]/a/span[1]')
		re=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[3]/div[1]/div/span')
		be=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[3]/div[1]/div/div/time')
		li=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/a') 
		if len(ab)==len(re)==len(be)==len(li)==1 :
			header=conv(ab[0].text)
			resource=conv(re[0].text)
			before_time=conv(be[0].text)
			newsURL=li[0].get_attribute("href")
			print "baslik ",header
			print "Kaynak ",resource
			print "Sure   ",before_time
			print "Link   ",newsURL,"\n\n"  
			#-- untill here every think okey crawl could read all infor about one news BUT
		else :
			#-- I noticed that some times news doesn't have image so the palece of informations are changed 
			#if my crawller couldn't read an information about a news it's trys to read that news assuming that news doesn't have an image 
			#print "PROBLEM",len(ab)," ",len(re)," ",len(be)," ",len(li)
			ab=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[1]/div[1]/a/span[1]')
			re=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[2]/div[1]/div/span')
			be=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/div[2]/div[1]/div/div/time')
			li=driver.find_elements_by_xpath('//*[@id="app-main"]/div/div/div/div[5]/div/div['+str(i)+']/article/a')
			if len(ab)==len(re)==len(be)==len(li)==1 :
				#if my assuming is true crawller could read information about that news 
				###print "######PROBLEM solved"
				###print "PROBLEM",len(ab)," ",len(re)," ",len(be)," ",len(li)
				header=conv(ab[0].text)
				resource=conv(re[0].text)
				before_time=conv(be[0].text)
				newsURL=li[0].get_attribute("href")
				print "baslik ",header
				print "Kaynak ",resource
				print "Sure   ",before_time
				print "Link   ",newsURL,"\n\n"  
			else :			
				#if my assuming is wrong that information about the news couldn't read 
				print "PROBLEM COULDN'T HANDLE************** FOR ",str(i),". NEWS"
				print "PROBLEM",len(ab)," ",len(re)," ",len(be)," ",len(li)
	
	driver.close() 
#----

   
crawlNewsStand()



