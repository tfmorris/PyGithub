# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework

import datetime


class GistComment(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.comment = self.g.get_gist("2729810").get_comment(323629)

    def testAttributes(self):
        self.assertEquals(self.comment.body, "Comment created by PyGithub")
        self.assertEquals(self.comment.created_at, datetime.datetime(2012, 5, 19, 7, 7, 57))
        self.assertEquals(self.comment.id, 323629)
        self.assertEquals(self.comment.updated_at, datetime.datetime(2012, 5, 19, 7, 7, 57))
        self.assertEquals(self.comment.url, "https://api.github.com/gists/comments/323629")
        self.assertEquals(self.comment.user.login, "jacquev6")

    def testEdit(self):
        self.comment.edit("Comment edited by PyGithub")
        self.assertEquals(self.comment.body, "Comment edited by PyGithub")
        self.assertEquals(self.comment.updated_at, datetime.datetime(2012, 5, 19, 7, 12, 32))

    def testDelete(self):
        self.comment.delete()
