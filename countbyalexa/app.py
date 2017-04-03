#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CountByAlexa App."""
import logging

from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def welcome_msg():
    """Welcome Message."""
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('YesIntent')
def count_by():
    """Count By Function."""
    numbers = list(range(1, 100, 1))
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.intent("CountIntent", convert={'count_by_inc': int})
def count_by_inc(count_by_inc):
    """Count By Function."""
    logging
    numbers = list(range(0, 100*count_by_inc, count_by_inc))
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.session_ended
def session_ended():
    """Session Ended."""
    goodbye_msg = render_template('goodbye')
    return statement(goodbye_msg)


if __name__ == '__main__':
    app.run(debug=True)
