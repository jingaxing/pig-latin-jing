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
#data type class, from library webapp2, mainhandler is a variable

#handler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for number in range(1,10):
            #print "what happens"
            self.response.write(number)

class PigHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("I can translate your phrases")

#route, address book as to where you find things
app = webapp2.WSGIApplication([
    ('/hello', MainHandler),('/count', CountHandler),('/pig', PigHandler)
], debug=True)
