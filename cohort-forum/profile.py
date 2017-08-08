from google.appengine.ext import nbd

class Profile(nbd.Model):
    name = nbd.StringProperty()
    location = nbd.StringProperty()
    profile = nbd.StringProperty()
    cohort = nbd.StringProperty()
    grad_year = nbd.IntegerProperty()
    interests = nbd.StringProperty()
    emailID = nbd.StringProperty()
