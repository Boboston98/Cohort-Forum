from google.appengine.ext import ndb

class Profile(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.StringProperty()
    program = ndb.StringProperty()
    cohort = ndb.StringProperty()
    grad_year = ndb.IntegerProperty()
    interests = ndb.StringProperty()
    emailID = ndb.StringProperty()
    url = ndb.StringProperty()
    about = ndb.StringProperty()
class Messages(ndb.Model):
    user = ndb.StringProperty()
    message = ndb.StringProperty()
