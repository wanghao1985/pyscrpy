
# coding: utf-8

# In[4]:


import urllib.request
 
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())


 #   在Pytho2.x中使用import urllib2——-对应的，在Python3.x中会使用import urllib.request，urllib.error。
 #   在Pytho2.x中使用import urllib——-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse。
 #   在Pytho2.x中使用import urlparse——-对应的，在Python3.x中会使用import urllib.parse。
 #   在Pytho2.x中使用import urlopen——-对应的，在Python3.x中会使用import urllib.request.urlopen。
 #   在Pytho2.x中使用import urlencode——-对应的，在Python3.x中会使用import urllib.parse.urlencode。
 #   在Pytho2.x中使用import urllib.quote——-对应的，在Python3.x中会使用import urllib.request.quote。
 #   在Pytho2.x中使用cookielib.CookieJar——-对应的，在Python3.x中会使用http.CookieJar。
 #   在Pytho2.x中使用urllib2.Request——-对应的，在Python3.x中会使用urllib.request.Request。
