#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CountByAlexa App."""
import logging

from flask import Flask, render_template
from flask_ask import (
    Ask, statement, question
)

app = Flask(__name__)
ask = Ask(app, '/')
log = logging.getLogger('flask_ask').setLevel(logging.DEBUG)


def countby_inc(incr):
    """Count By Function."""
    number_list = list(range(0, 101 * incr, incr))
    return number_list


@ask.launch
def welcome_msg():
    """Welcome Message."""
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('AMAZON.YesIntent')
def count_by():
    """Count By Function."""
    numbers = countby_inc(1)
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.intent("CountIntent", convert={'count_by_inc': int})
def count_by_inc(incr):
    """Count By Function."""
    numbers = countby_inc(incr)
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.session_ended
def session_ended():
    """Session Ended."""
    return "", 200


@ask.intent("AMAZON.StopIntent")
def stop():
    """Stop Intent."""
    goodbye_msg = render_template('goodbye')
    return statement(goodbye_msg)


@ask.intent("AMAZON.CancelIntent")
def cancel():
    """Cancel Intent."""
    goodbye_msg = render_template('goodbye')
    return statement(goodbye_msg)


if __name__ == '__main__':
    app.run(debug=True)
