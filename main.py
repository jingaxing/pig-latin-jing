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
import jinja2
import os

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#data type class, from library webapp2, mainhandler is a variable

#handler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        my_variables = {"numbers" : [9,5,5,10]}
        count_template = my_env.get_template('templates/count.html')
        self.response.write(count_template.render(my_variables))

class PigHandler(webapp2.RequestHandler):
    def get(self):
        #put in dictionary, render dictionary, passed to template
        pig_template = my_env.get_template('templates/pig.html')
        self.response.write(pig_template.render())

    def post(self):
        user_input = self.request.get('user_word')
        def translatePigLatin(old_word):
            new_word = old_word[1:] + old_word[0] + "ay"
            return(new_word)
        pl_result = translatePigLatin(user_input)
        translated_words = {"words": pl_result}
        #put in dictionary, render dictionary, passed to template
        pig_template = my_env.get_template('templates/pig.html')
        self.response.write(pig_template.render(translated_words))

#route, address book as to where you find things
app = webapp2.WSGIApplication([
    ('/hello', MainHandler),('/count', CountHandler),('/pig', PigHandler)
], debug=True)
