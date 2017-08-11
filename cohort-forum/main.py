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
from databases import Profile
from databases import Messages

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout_link = users.create_logout_url('/')
            user_id = user.user_id()
            profile_query = Profile.query(Profile.emailID == user_id)
            profile = profile_query.get()
            if profile is not None:
                self.redirect('/chat')
            else:
                self.redirect('/profile')

            #greeting = ('Welcome, %s! (<a href="%s">LOGOUT</a>)' %
            #    (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or Register</a>.' %
                users.create_login_url('/'))

            self.response.write('<html><body>%s</body></html>' % greeting)
        def post(self):
            greeting = ('Welcome, %s! (<a href="%s">LOGOUT</a>)' %
            (user.nickname(), users.create_logout_url('/')))
class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/profile.html')
        self.response.write(template.render())
    def post(self):

        user = users.get_current_user()
        user_id = user.user_id()
        name = self.request.get('name')
        currloc = self.request.get('current_location')
        prgm = self.request.get('program')
        cohort = self.request.get('cohort')
        year = self.request.get('year')
        interests = self.request.get('interest')
        pic_url = self.request.get('image')
        about = self.request.get('about')
        new_profile = Profile(name = name, location = currloc, program = prgm, cohort = cohort,
        grad_year = int(year), interests = interests, emailID = user_id, url = pic_url,about = about)
        key = new_profile.put()
        self.redirect('/logout')
class EditProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/editprofile.html')
        self.response.write(template.render())
    def post(self):
        user = users.get_current_user()
        user_id = user.user_id()
        profile_query = Profile.query(Profile.emailID == user_id)
        profile = profile_query.get()
        profile.name = self.request.get('name')
        profile.program = self.request.get('program')
        profile.location = self.request.get('current_location')
        profile.cohort = self.request.get('cohort')
        profile.grad_year = self.request.get('year')
        profile.interest = self.request.get('interest')
        profile.url = self.request.get('image')
        profile.about = self.request.get('about')
        self.redirect('/chat')
class ChatHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/chat.html')
        chat_list = []
        user = users.get_current_user()
        user_id = user.user_id()
        print(user_id)
        profile_query = Profile.query(Profile.emailID == user_id)
        profile = profile_query.get()
        name = profile.name
        chat_message = self.request.get('user_message')
        new_message =  Messages(user = name, message = chat_message)
        key = new_message.put()

        message_query = Messages.query()
        messages = message_query.fetch()
        for chat_item in messages:
            chat_list.append(chat_item.user+ " : "+chat_item.message)
        for item in chat_list:
            print(item)
        print(chat_list)
        template_variables ={
            'list': chat_list
        }
        self.response.write(template.render(template_variables))

    def post(self):
        print("*********************test")
        chat_list = []
        template = jinja_environment.get_template('templates/chat.html')
        # for x in range(0,m_list):
        #     messages = {
        #     str(x): m_list[x]
        #     }
        user = users.get_current_user()
        user_id = user.user_id()
        print(user_id)
        profile_query = Profile.query(Profile.emailID == user_id)
        profile = profile_query.get()
        name = profile.name
        chat_message = self.request.get('user_message')
        new_message =  Messages(user = name, message = chat_message)
        key = new_message.put()

        message_query = Messages.query()
        messages = message_query.fetch()
        for chat_item in messages:
            chat_list.append(chat_item.user+ " : "+chat_item.message)
        for item in chat_list:
            print(item)
        print(chat_list)
        template_variables ={
            'list': chat_list
        }
        self.response.write(template.render(template_variables))
class logoutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/logout.html')
        self.response.write(template.render())
class ShowHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/showprofile.html')
        user = users.get_current_user()
        user_id = user.user_id()
        profile_query = Profile.query(Profile.emailID == user_id)
        profile = profile_query.get()
        template_variables = {
            'name': profile.name,
            'location': profile.location,
            'program': profile.program,
            'cohort': profile.cohort,
            'grad_year': profile.grad_year,
            'interests': profile.interests,
            'url': profile.url
             }
        self.response.write(template.render(template_variables))
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/chat',ChatHandler),
    ('/profile',ProfileHandler),
    ('/showprofile',ShowHandler),
    ('/editprofile',EditProfileHandler),
    ('/logout',logoutHandler)
], debug=True)
