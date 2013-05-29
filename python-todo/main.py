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
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):
    def get(self):
	
	user = users.get_current_user()

	if user:
	    nickname = user.nickname()
	    #atlocation = nickname.index("@")
	    #nickname = nickname[:atlocation]
	    todos = Todo.all()
	    template_values = {'nickname':nickname, 'todos':todos}
		
	    path = os.path.join(os.path.dirname(__file__), 'index.html')
	    self.response.out.write(template.render(path, template_values))
	else:
	    self.redirect(users.create_login_url(self.request.uri))
		
    def post(self):

	    todo = Todo()
	    todo.author = users.get_current_user()
	    todo.item = self.request.get("item")
	    todo.completed = False
		
	    #self.response.out.write(self.request.get("item"));

	    todo.put()

	    #self.response.out.write("Saved: " + self.request.get("item"));
		
	    self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Todo(db.Model):
    author = db.UserProperty()
    item = db.StringProperty()
    completed = db.BooleanProperty()
    date = db.DateTimeProperty(auto_now_add=True)


	  
	  
	  
	  