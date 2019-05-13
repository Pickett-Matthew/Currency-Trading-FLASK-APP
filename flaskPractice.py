#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:05:14 2019

@author: matthewpickett
"""
import praw
from flask import Flask, render_template

app = Flask(__name__)

reddit = praw.Reddit(client_id='1ToVPt9fRp43eg', \
                     client_secret='NHnV538JTdO3KSVfja96M3O6wfw', \
                     user_agent='myReddMP', \
                     username='Dount_Cooku', \
                     password='Mmpjordan23')

subreddit = reddit.subreddit("showerthoughts")


@app.route("/")
def swiper():
    return render_template("swiper.html", subreddit=subreddit)



if __name__ =='__main__':
    app.run(debug=True)