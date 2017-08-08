from google.appengine.ext import nbd

class Messages(nbd.Model):
    user = StringProperty()
    message = StringProperty()
