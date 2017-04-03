# CountByAlexa
Alexa skill using Flask Ask
[![Build Status](https://travis-ci.org/ravishan16/CountByAlexa.svg?branch=master)](https://travis-ci.org/ravishan16/CountByAlexa)
[![Code Climate](https://codeclimate.com/github/ravishan16/CountByAlexa/badges/gpa.svg)](https://codeclimate.com/github/ravishan16/CountByAlexa)


Developed this Skill to help my Son Count

- Start skill by saying "Start Count By"
- Alexa will count by 1,2,5,10

## Flask-Ask (Reference)

[Tutorial](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)
[Link](https://github.com/johnwheeler/flask-ask/tree/master/samples)


## Deployment Using Zappa

```python

virtualenv venv
venv\Scripts\activate
pip install flask-ask zappa awscli
zappa init
zappa deploy dev

```

-[Blog](https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa)
-[ZappaGit](https://github.com/Miserlou/Zappa)

## Checking Logs

```python

zappa tail dev

```

## Pushing Update To Code

```python

zappa update dev

```
