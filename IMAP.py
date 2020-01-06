# uft-8

import imapclient
import pyzmail
imapObj = imapclient.IMAPClient(' ', ssl=True)
imapObj.login('my_email_address@gmail.com', 'My_SELECT_PASSWORD')
imapObj.select_folder('INBOX', readonly=True)
imapObj.delete_messages(UIDS)
imapObj.expunge()
UIDS = imapObj.search(['SINCE 05-Jul-2014'])
print(UIDS)
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))
print(message.get_address('cc'))
print(message.get_address('bcc'))
print(message.text_part != None)
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.logout()
