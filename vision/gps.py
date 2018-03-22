import requests
import json
#import webbrowser
#import urllib2
#import ssl
#ssl._create_default_https_context=ssl._create_unverified_context
send_url='http://freegeoip.net/json'
r=requests.get(send_url)
j=json.loads(r.text)
lat = j['latitude']
lon=j['longitude']
city=j['city']
url='http://maps.google.com/maps?q={},{}&z=18'.format(lat,lon)
print 'your location is',url,' and city = ',city
#gcontext=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#var =urllib2.urlopen('http://gymkhana.iitb.ac.in/~hostel16/weSee/Mail.php?url={},city={}'.format(url,city),context=gcontext).read()
#print 'Mail sent to your guardian'
