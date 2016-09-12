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
from caesar import encrypt
import cgi

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Formation</title>
    </head>
    <body>
        <h1>Enter text</h1>
"""
page_footer = """
</body>
</html>
"""

form = """
<form method="post">
    <div>
        <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="{0}">
            <p class="error"></p>
    </div>
    <textarea type="text" name="text">{1}</textarea>
    <br>
    <input type="submit">
</form>
"""

# {0} can also be "%s"

class Rot13(webapp2.RequestHandler):

    def get(self):

        temp = ""
        response = page_header + form.format(temp, temp) + page_footer
        self.response.write(response)

    def post(self):
        rot_num = int(self.request.get("rot"))
        rot_answer = self.request.get("text")
        answer = encrypt(rot_answer, rot_num)
        answer = cgi.escape(answer)

        response = page_header + form.format(rot_num, answer)
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Rot13)
], debug=True)
