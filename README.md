

# CountByAlexa


Count By is a simple and interactive Alexa skill aimed at making learning to skip count fun. Skill helps reinforce the concept of counting in increments.

[![Build Status](https://travis-ci.org/ravishan16/CountByAlexa.svg?branch=master)](https://travis-ci.org/ravishan16/CountByAlexa)
[![Code Climate](https://codeclimate.com/github/ravishan16/CountByAlexa/badges/gpa.svg)](https://codeclimate.com/github/ravishan16/CountByAlexa)
[![Test Coverage](https://codeclimate.com/github/ravishan16/CountByAlexa/badges/coverage.svg)](https://codeclimate.com/github/ravishan16/CountByAlexa/coverage)
[![Issue Count](https://codeclimate.com/github/ravishan16/CountByAlexa/badges/issue_count.svg)](https://codeclimate.com/github/ravishan16/CountByAlexa)


Documentation
===============

These resources will get you up and running quickly:

* `Amazon Dev Blog <https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development>`_
* `Flask-Ask Reference <https://alexatutorial.com/flask-ask/>`_
* `Flask-Ask samples <https://github.com/johnwheeler/flask-ask/tree/master/samples>`_
* `JSON Interface Reference <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference>`_
* `Deploying a Sample Custom Skill as a Web Service <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/deploying-a-sample-skill-as-a-web-service>`_


Configuration
-------------

The following are set as environment variables in Lambda Function:

MY_USERID & MY_NAME are added to make it special for my son, the skill greets him with his name.

- ``LOG_LEVEL``: LOG_LEVEL is set to default ``INFO`` this can be overridden by adding the env variable.
- ``MY_USERID``: Env variable set  to my ``Alexa User Id`` that comes as part of the request. This is optional.
- ``MY_NAME``: Env variable set  to any text\name that will be added as part of the launch intent/ stop intent greeting



Deployment
-------------

Deployment involves two steps:

- `Registering Skill in Developer Portal <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/registering-and-managing-alexa-skills-in-the-developer-portal>` : This step involves configuring skill providing intent schema, sample utterance, custom slots.. and linking to the Flask-Ask API endpoint.
- `Flask-Ask Deployment`: Deploying the Flask-Ask App. Which involves deploying AWS Lambda Function and AWS API Gateway. Zappa makes this step a breeze. It does all the mundane task.
- `Deploying  Server Less Micro-services using Zappa <https://gun.io/blog/serverless-microservices-with-zappa-and-flask/>`
-[Blog](https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa)
-[ZappaGit](https://github.com/Miserlou/Zappa)

```python

virtualenv venv
venv\Scripts\activate
pip install flask-ask zappa awscli
zappa init
zappa deploy dev

```

## Checking Logs

```python

zappa tail dev

```

## Pushing Update To Code

```python

zappa update dev

```
