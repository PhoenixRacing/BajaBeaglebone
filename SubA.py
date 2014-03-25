from pydispatch import dispatcher

def handleMessageA(sender, signal):
    print 'Signal was sent by', sender, ' message is ', signal

def listenForMessageA():
    dispatcher.connect(handleMessageA, sender="PubA")
