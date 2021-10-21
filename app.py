import pprint
from config.apiKey import apiKeys, apiHost, urls
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from flask import Flask, redirect, url_for, render_template, request
from selenium import webdriver
import time
import os
import requests

app = Flask(__name__)


@app.route("/coins")
def rende_home_page():
    try:

        url = urls

        headers = {
            'x-rapidapi-key': apiKeys,
            'x-rapidapi-host': apiHost
        }

        response = requests.request("GET", url, headers=headers)

        dataName = json.loads(response.text)

        pprint.pprint(dataName)

        return render_template('index.html', len=len(dataName), dataName=dataName)

        if __name__ == '__main__':
            app.run()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


@app.route("/coins/<id>")
def rende_details_page(id):
    try:

        url = urls

        headers = {
            'x-rapidapi-key': apiKeys,
            'x-rapidapi-host': apiHost
        }

        response = requests.request("GET", url, headers=headers)

        dataName = json.loads(response.text)

        pprint.pprint(dataName)

        user_info = database.query.filter_by(id=id).first()

        return render_template('details.html', information=user_info, len=len(dataName), dataName=dataName)

        if __name__ == '__main__':
            app.run()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
