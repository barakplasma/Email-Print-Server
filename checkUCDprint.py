#lets do it
#resources
#http://docs.python.org/library/urllib2.html
#http://docs.python.org/library/xml.dom.minidom.html
#from http://crc-app.ucdavis.edu/forum/index.cfm?page=topic&topicID=1703&start=1
import urllib2, xml.dom.minidom
from xml.dom.minidom import parse, parseString
# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of ``None``.
top_level_url = "https://mail.google.com"
password_mgr.add_password(None, top_level_url, 'ucdprint', 'itlm027test')

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use the opener to fetch a URL
#opener.open(a_url)

Emailfeed = opener.open("https://mail.google.com/mail/feed/atom")

emailxml = Emailfeed
domEmail = parse(emailxml)

mailSubj = domEmail.getElementsByTagName("title")
mailSubjList = mailSubj[0]
print mailSubjList.toxml()
