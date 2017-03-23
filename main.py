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
import random

def getRandomFortune():
    # list of possible fortunes
    fortunes = [
        "whoops...eternal damnation",
        "long weekend in 6th circle of hell (with the heretics)",
        "vacation for 3: you, Dante and Virgil visit the inferno",
        "ouch...a daily ripping out of your regenerating liver by a bald eagle",
        "several ungentle slaps on the wrist",
        "forever haunted by the ghost of sammy haggar"

    ]

    # randomly select one of the fortunes
    index = random.randint(0,len(fortunes)-1)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = getRandomFortune()
        fortune_sentence = "Your fortune: <b>" + fortune + "</b>"
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = random.randint(1,100)
        number_sentence = 'Your lucky number: <strong> a billion</strong>' #+ str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href='.'><button> Another cookie, please </button> </a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again_button


        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
