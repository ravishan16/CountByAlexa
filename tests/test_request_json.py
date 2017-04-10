#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for countbyalexa request body."""

launch_body = {
    "request": {
        "locale": "en-US",
        "requestId": "amzn1.echo-api.request",
        "timestamp": "2017-04-08T21:53:03Z",
        "type": "LaunchRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": True,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
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
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

help_body = {
    "request": {
        "intent": {
            "name": "AMAZON.HelpIntent"
        },
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
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
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

no_body = {
    "request": {
        "intent": {
            "name": "AMAZON.NoIntent"
        },
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
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
                    "value": "1"
                },
                "count_order": {
                    "name": "count_order",
                    "value": "forward"
                },
                "count_limit": {
                    "name": "count_limit",
                    "value": "10000"
                }
            }
        },
        "locale": "en-US",
        "requestId": "amzn1.echo-api.request",
        "timestamp": "2017-04-08T21:51:18Z",
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

count_body_zero = {
    "request": {
        "intent": {
            "name": "CountIntent",
            "slots": {
                "count_by_inc": {
                    "name": "count_by_inc",
                    "value": "0"
                },
                "count_order": {
                    "name": "count_order",
                    "value": "reverse"
                }
            }
        },
        "locale": "en-US",
        "requestId": "amzn1.echo-api.request",
        "timestamp": "2017-04-08T21:51:18Z",
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

count_string_body = {
    "request": {
        "intent": {
            "name": "CountIntent",
            "slots": {
                "count_by_inc": {
                    "name": "count_by_inc",
                    "value": "awesome"
                },
                "count_order": {
                    "name": "count_order",
                    "value": "forward"
                },
                "count_limit": {
                    "name": "count_limit",
                    "value": "10000"
                }
            }
        },
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

count_reverse_body = {
    "request": {
        "intent": {
            "name": "CountIntent",
            "slots": {
                "count_by_inc": {
                    "name": "count_by_inc",
                    "value": "1"
                },
                "count_order": {
                    "name": "count_order",
                    "value": "reverse"
                },
                "count_limit": {
                    "name": "count_limit",
                    "value": "100000"
                }
            }
        },
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
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
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}

count_error_body = {
    "request": {
        "intent": {
            "name": "CountIntent",
            "slots": {
                "count_by_inc": {
                    "name": "count_by_inc",
                    "value": "10"
                },
                "count_order": {
                    "name": "count_order",
                    "value": "reverse"
                },
                "count_limit": {
                    "name": "count_limit",
                    "value": "1"
                }
            }
        },
        "type": "IntentRequest"
    },
    "session": {
        "application": {
            "applicationId": "amzn1.ask.skill"
        },
        "new": False,
        "sessionId": "amzn1.echo-api.session",
        "user": {
            "userId": "amzn1.ask.account"
        }
    },
    "version": "1.0"
}
