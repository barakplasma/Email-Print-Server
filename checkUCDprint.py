#lets do it
#resources
#from http://crc-app.ucdavis.edu/forum/index.cfm?page=topic&topicID=1703&start=1

import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('ucdprint@gmail.com', os.environ.get("password"))
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

