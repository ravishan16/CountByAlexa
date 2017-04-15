#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CountByAlexa App."""
import logging
import os

from flask import Flask, render_template
from flask_ask import (
    Ask, statement, question, convert_errors, session as ask_session
)

app = Flask(__name__)
ask = Ask(app, '/')
log_level = os.getenv("LOG_LEVEL", logging.INFO)
log = logging.getLogger('flask_ask').setLevel(log_level)

NAME_KEY = 'USER_NAME'
DEFAULT_INCR = 1
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT", 20)
MAX_LIMIT = 10000


def new_session():
    """New Session to Set Name Attribute."""
    my_userid = os.getenv("MY_USERID", '')
    if (ask_session.user.userId == my_userid):
        ask_session.attributes[NAME_KEY] = os.getenv("MY_NAME", '')


def countby_inc(incr, limit, reverse=False):
    """Count By Function."""
    if incr == 0:
        number_list = [0]
    else:
        if (limit/incr) > MAX_LIMIT:
            limit = incr*DEFAULT_LIMIT
        number_list = list(range(0, limit+1, incr))
        if reverse:
            number_list = reversed(number_list)
    return number_list


@ask.launch
@ask.intent("AMAZON.HelpIntent")
def welcome_msg():
    """Welcome Message."""
    new_session()
    name = ask_session.attributes.get(NAME_KEY)
    if name is None:
        name = ''
    welcome = render_template('welcome', name=name)
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('AMAZON.YesIntent')
def count_by():
    """Count By Function."""
    numbers = countby_inc(DEFAULT_INCR, DEFAULT_LIMIT, False)
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.intent("CountIntent",
            convert={'count_by_inc': int, 'count_limit': int})
def count_by_inc(count_by_inc, count_order, count_limit):
    """Count By Function."""
    new_session()
    reversed = False
    if convert_errors:
        reprompt = render_template('reprompt')
        return question(reprompt)
    if count_order in ['reverse', 'reversed', 'backwards', 'backwords',
                       'back', 'descending', 'down', 'desc']:
        reversed = True
    if count_by_inc is None:
        count_by_inc = DEFAULT_INCR
    if count_limit is None:
        count_limit = DEFAULT_LIMIT*count_by_inc
    numbers = countby_inc(count_by_inc, count_limit, reversed)
    countby_msg = render_template('countby', numbers=numbers)
    return statement(countby_msg)


@ask.session_ended
def session_ended():
    """Session Ended."""
    return "", 200


@ask.intent("AMAZON.StopIntent")
@ask.intent("AMAZON.CancelIntent")
@ask.intent("AMAZON.NoIntent")
def stop():
    """Stop Intent."""
    name = ask_session.attributes.get(NAME_KEY)
    if name is None:
        name = ''
    goodbye_msg = render_template('goodbye', name=name)
    return statement(goodbye_msg)


if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
