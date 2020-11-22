# -*- coding:utf-8 -*-

import unittest

from camcli.client import send


class TestRunner(unittest.TestCase):

    def test_run(self):
        self.assertEqual("hello cambrian", send())


if __name__ == '__main__':
    unittest.main()
