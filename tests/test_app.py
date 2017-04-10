#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for count by alexa."""

import json
import unittest

from countbyalexa.app import app, countby_inc
import test_request_json as test_request_json


class TestApp(unittest.TestCase):
    """TestApp class."""

    def setUp(self):
        """ Test Suite Setup Disables ASK_VERIFY_REQUESTS."""
        app.config['ASK_VERIFY_REQUESTS'] = False
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """ Test Suite Tear down."""
        pass

    def test_countby_inc(self):
        """Test Count By inc function."""
        expected = 11
        actual = len(countby_inc(1, 10))
        print actual
        assert expected == actual

    def test_launch(self):
        """Test Launch Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.launch_body))
        assert result.status_code == 200

    def test_sess_end(self):
        """Test Session End."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.sess_end_body))
        assert result.status_code == 200

    def test_CountIntent(self):
        """Test Count Intent Basic."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.count_body))
        assert result.status_code == 200

    def test_CountErrorIntent(self):
        """Test Count Intent String in Slot."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.count_string_body))
        assert result.status_code == 200

    def test_CountZero(self):
        """Test Count Intent for count by zero."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.count_body_zero))
        assert result.status_code == 200

    def test_CountReverse(self):
        """Test Count Intent for Reverse."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.count_reverse_body))
        assert result.status_code == 200

    def test_CountError(self):
        """Test Count Intent for Error."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.count_error_body))
        assert result.status_code == 200

    def test_HelpIntent(self):
        """Test Help Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.help_body))
        assert result.status_code == 200

    def test_yes(self):
        """Test Yes Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.yes_body))
        assert result.status_code == 200

    def test_stop(self):
        """Test Stop Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.stop_body))
        assert result.status_code == 200

    def test_cancel(self):
        """Test Cancel Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.cancel_body))
        assert result.status_code == 200

    def test_no(self):
        """Test No Intent."""
        result = self.app.post('/', data=json.dumps(
                                test_request_json.no_body))
        assert result.status_code == 200


if __name__ == '__main__':
    """Main Function"""
    unittest.main()
