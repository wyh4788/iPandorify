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

import cgi

from webapp2_extras import jinja2



class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

class MainHandler(BaseHandler):
    def get(self):
        context = {'message': 'Hello, world!'}
        self.render_response('index.html', **context)

    def post(self):
        name = self.request.get('search-song')
        test = self.request.get('test')
        context = {'message': 'Hello, world!'}
        self.render_response('index.html', **context)
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
