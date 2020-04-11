from quickstart import *

# A function that sends the email of the result to hadas.c@velismedia.com.
def sendemail(message):
    sender = 'hopetoworkforyou@gmail.com'
    subject = 'Finished The Program'
    login = 'hopetoworkforyou'
    password = "" #TODO:DELETED.
    to_addr = 'hadas.c@velismedia.com'
    service = main()
    SendMessage(service, "me",CreateMessage(to_addr, to_addr, subject, message))
