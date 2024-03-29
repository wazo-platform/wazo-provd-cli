# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest

from wazo_provd_cli.mac import norm_mac


class TestNormMac(unittest.TestCase):
    def test_norm_mac(self):
        expected = '00:11:22:aa:bb:cc'
        macs = [
            '001122AABBCC',
            '00-11-22-aa-Bb-cc',
        ]

        for mac in macs:
            self.assertEqual(norm_mac(mac), expected)
