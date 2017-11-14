# _*_ coding: utf-8 _*_
# Author: "ConanSoloman"

from datetime import datetime
import urllib2 as url
import urllib
import cookielib
import re
import string
# from urllib.parse import urlencode
# from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from lxml import html
# import time
# from itertools import product

import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from GLOBAL_VAR import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# msg = 'Why,Oh why!'
def send_email():
    '''
    sent email, the information is stored in GLOBAL_VAR
    :return:
    '''
    msg = MIMEMultipart()

    msg['Subject'] = SUBJECT
    body = BODY
    msg.attach(MIMEText(body, 'plain'))
    msg['From'] = FROMADDR
    msg['To'] = TOADDRS

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(MAILUSER, MAILPASS)
    text = msg.as_string()
    server.sendmail(FROMADDR, TOADDRS, text)
    server.quit()

# send_email()


def crawling_job_info():
    # record the date
    date = datetime.now().date()
    date = datetime.strftime(date, '%m/%d/%Y')

    req = url.Request('https://secure.indeed.com/account/login?service=my&hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F')
    response = url.urlopen(req)
    the_page = response.read()

    soup = BeautifulSoup(the_page, 'html.parser')
    print soup


# crawling_job_info()


def login_website():
    session_requests = requests.session()
    login_url = 'https://www.linkedin.com/jobs/'
    login_response = session_requests.get(login_url)
    login = BeautifulSoup(login_response.text, 'lxml')

    # print login.section
    # print
    # Get hidden form inputs
    inputs = login.find('form', {'name': 'login'}).findAll('input', {'type': ['hidden', 'submit']})

    # print inputs
    # Create POST data
    # post = {input.get('name'): input.get('value') for input in inputs}
    # post['session_key'] = USERNAME
    # post['session_password'] = PASSWD

    # Post login
    # post_response = session_requests.post('https://www.linkedin.com/uas/login-submit', data=post)
    #
    # # Get home page
    # home_response = session_requests.get('http://www.linkedin.com/nhome')
    # home = BeautifulSoup(home_response.text, 'lxml')
    # print home

# login_website()

    # payload = {
    #     "username": 'zhytford@gmail.com',
    #     "password": 'zhyt1987',
    #     "authenticity_token": authenticity_token
    # }
    #
    # result = session_requests.post(login_url, data=payload, headers=dict(referer=login_url))
    #
    # result = session_requests.get('https://twitter.com/?lang=en',
    #                               headers=dict(referer='https://twitter.com/?lang=en'))
    # print result.content
    #
    # tree = html.fromstring(result.content)
    # print tree

# login_website()

