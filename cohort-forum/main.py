#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
from google.appengine.api import users
from profile import Profile

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or Register</a>.' %
                users.create_login_url('/'))

        self.response.write('<html><body>%s</body></html>' % greeting)

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        self.response.write(template.render())
        
class ChatHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/chat.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/chat.html')
        m_list = []
        m_list.append(self.request.get("user_message"))
        for x in range(0,m_list):
            messages = {
            str(x): m_list[x]
            }
        self.response.write(template.render(messages))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/chat',ChatHandler),
    ('/profile',ProfileHandler)
], debug=True)
