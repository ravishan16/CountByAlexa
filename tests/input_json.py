#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for countbyalexa request body."""

launch_body = {
    "request": {
        "type": "LaunchRequest"
    },
    "version": "1.0"
}

sess_end_body = {
    "request": {
        "type": "SessionEndedRequest"
    },
    "version": "1.0"
}

stop_body = {
    "request": {
        "intent": {
            "name": "AMAZON.StopIntent"
        },
        "type": "IntentRequest"
    },
    "version": "1.0"
}

cancel_body = {
    "request": {
        "intent": {
            "name": "AMAZON.CancelIntent"
        },
        "type": "IntentRequest"
    },
    "version": "1.0"
}

count_body = {
    "request": {
        "intent": {
            "name": "CountIntent",
            "slots": {
                "count_by_inc": {
                    "name": "count_by_inc",
                    "value": "2"
                }
            }
        },
        "type": "IntentRequest"
    },
    "version": "1.0"
}

yes_body = {
    "request": {
        "intent": {
            "name": "AMAZON.YesIntent"
        },
        "type": "IntentRequest"
    },
    "version": "1.0"
}
