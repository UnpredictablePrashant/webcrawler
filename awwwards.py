import sys  # Need to have acces to sys.stdout
import requests   #Requests is not a built in module, so you will have to download it.
from bs4 import BeautifulSoup


def webcrawler(max_pages):
	search=raw_input("Enter the type of website you want to search: ")
	page = 1
	filename = search + ".txt"
	fd = open(filename,'w') # open the result file in write mode
	old_stdout = sys.stdout   #store the default system handler to be able to restore it
	sys.stdout = fd #file is being used by print as destination 
	print "This is the list of best websites enlisted under the category: ", search # statement is added to file
	print "\n\n"
	sys.stdout=old_stdout #here we restore the default behavior
	while page<=max_pages:
		url="http://www.awwwards.com/search-websites/?text=" + str(search) + "&submit=&search-section=on&page="+ str(page)
		sourcecode = requests.get(url)
		plaintext = sourcecode.text
		soup = BeautifulSoup(plaintext, "html.parser")
		for link in soup.findAll('a',{'class': 'bt-url'}):
			href = link.get('href')
			old_stdout = sys.stdout   #store the default system handler to be able to restore it
			sys.stdout = fd #file is being used by print as destination 
			print href # 'href' is added to file
			sys.stdout=old_stdout #here we restore the default behavior
			print href #printed on the console
			
		page+=1
	fd.close() 
		
webcrawler(200)






