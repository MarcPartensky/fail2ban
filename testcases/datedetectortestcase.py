# This file is part of Fail2Ban.
#
# Fail2Ban is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Fail2Ban is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Fail2Ban; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# Author: Cyril Jaquier
# 
# $Revision: 253 $

__author__ = "Cyril Jaquier"
__version__ = "$Revision: 253 $"
__date__ = "$Date: 2006-07-17 00:21:58 +0200 (Mon, 17 Jul 2006) $"
__copyright__ = "Copyright (c) 2004 Cyril Jaquier"
__license__ = "GPL"

import unittest, time
from server.datedetector import DateDetector
from server.datetemplate import DateTemplate

class DateDetectorTest(unittest.TestCase):

	def setUp(self):
		"""Call before every test case."""
		self.datedetector = DateDetector()
		self.datedetector.addDefaultTemplate()

	def tearDown(self):
		"""Call after every test case."""
	
	def testGetEpochTime(self):
		log = "1138049999 [sshd] error: PAM: Authentication failure"
		date = [2006, 1, 23, 20, 59, 59, 0, 23, 0]
		dateUnix = 1138046399.0
		
		self.assertEqual(self.datedetector.getTime(log), date)
		self.assertEqual(self.datedetector.getUnixTime(log), dateUnix)
	
	def testGetTime(self):
		log = "Jan 23 21:59:59 [sshd] error: PAM: Authentication failure"
		date = [2006, 1, 23, 21, 59, 59, 1, 23, -1]
		dateUnix = 1138049999.0
	
		self.assertEqual(self.datedetector.getTime(log), date)
		self.assertEqual(self.datedetector.getTime(log), date)
		self.assertEqual(self.datedetector.getTime(log), date)
		self.assertEqual(self.datedetector.getUnixTime(log), dateUnix)
		self.assertEqual(self.datedetector.getUnixTime(log), dateUnix)
		self.assertEqual(self.datedetector.getUnixTime(log), dateUnix)
		