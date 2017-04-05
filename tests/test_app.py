#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for countbyalexa."""

import json
import unittest

from countbyalexa.app import app, countby_inc
from input_json import *


class TestApp(unittest.TestCase):
    """TestApp class."""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        app.config['ASK_VERIFY_REQUESTS'] = False
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_countby_inc(self):
        """Test echo_name function."""
        expected = 101
        actual = len(countby_inc(1))
        # print actual
        assert expected == actual

    def test_launch(self):
        result = self.app.post('/', data=json.dumps(launch_body))
        assert result.status_code == 200

    def test_sess_end(self):
        result = self.app.post('/', data=json.dumps(sess_end_body))
        assert result.status_code == 200

    def test_CountIntent(self):
        # print json.dumps(count_body)
        result = self.app.post('/', data=json.dumps(count_body))
        # print result
        assert result.status_code == 200

    def test_yes(self):
        # print json.dumps(yes_body)
        result = self.app.post('/', data=json.dumps(yes_body))
        # print result
        assert result.status_code == 200

    def test_stop(self):
        # print json.dumps(stop_body)
        result = self.app.post('/', data=json.dumps(stop_body))
        # print result
        assert result.status_code == 200

    def test_cancel(self):
        # print json.dumps(cancel_body)
        result = self.app.post('/', data=json.dumps(cancel_body))
        # print result
        assert result.status_code == 200


if __name__ == '__main__':
    unittest.main()
