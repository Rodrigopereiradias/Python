import threading
import urllib2
import time

start = time.time()
urls = ["www.google.com", "www.apple.com" ,"www.Microsoft.com" ,"www.instagram.com"]

def chama_url(url):
    req = urllib2.Request(url)
    response= urllib2.urlopen(req)
    the_page = response.read()
    print("'%s\' carregando em %ss" % (url, (time.time())- start))
    #print(the_page)

threads = [threading.Thread(target=chama_url(), args=(url,)) for url in urls]

for threads in threads:
    threads.start()
for threads in threads:
    threads.join()

print("elapsed time: %s" % (time.time()-start))