from google.appengine.ext import ndb

class Profile(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.StringProperty()
    profile = ndb.StringProperty()
    cohort = ndb.StringProperty()
    grad_year = ndb.IntegerProperty()
    interests = ndb.StringProperty()
    emailID = ndb.StringProperty()

class Messages(ndb.Model):
    user = ndb.StringProperty()
    message = ndb.StringProperty()
