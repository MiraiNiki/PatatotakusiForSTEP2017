#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import logging
import cgi
from google.appengine.ext.webapp import template 
from google.appengine.ext import webapp
from google.appengine.ext import ndb

class MainHandler(webapp.RequestHandler):
    def get(self):
		data = cgi.FieldStorage()
		first = data.getvalue('first', 'notfound').decode('utf-8')
		first_list = []
		if first != 'notfound':
			first_list = list(first)   
		second = data.getvalue('second', 'notfound').decode('utf-8')
		second_list = []
		if second != 'notfound':
			second_list = list(second)
		result = []
		cnt = 1
		while len(first_list) != 0 or len(second_list) != 0:
			cnt = (cnt + 1) % 2
			if len(first_list) == 0:
				cnt = 1
			elif len(second_list) == 0:
				cnt = 0
			if cnt == 0:
				result.append(first_list.pop(0))
			else:
				result.append(second_list.pop(0))
		body = "hoge"
		template_values = {'body': body,}
		path = os.path.join(os.path.dirname(__file__) + '/', 'main.html')
		self.response.out.write(template.render(path,template_values))
		self.response.write("".join(result))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
