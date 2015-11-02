#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys, tweepy, time, random
hostname = os.uname()[1]
if hostname == "server1":
    prepath = "/opt"
elif hostname == "octopussy":
    prepath = "/home/xir/dev"
sys.path.append(os.path.abspath(prepath + "/menu/conf/"))
from menuconf import *
from auth import *
sys.path.append(os.path.abspath( path + "/lib/"))
from database import *
from libmails import *
from links import *

def follow_followers(api):
    '''Lee followers'''
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower.screen_name)
    return followers

def get_api(authTwitter):
  auth = tweepy.OAuthHandler(authTwitter['consumer_key'], authTwitter['consumer_secret'])
  auth.set_access_token(authTwitter['access_token'], authTwitter['access_token_secret'])
  return tweepy.API(auth)

def send_menu(api, user = ''):
    photoPath = datapath  + "hoy.jpg"
    status = ''
    if os.path.exists( photoPath ):
        if user:
          status = '@' + user + ' '
        status += u'Menú del cole para el ' + today + ' de ' + mes[int(month[:2])]
        solution = api.update_with_media(photoPath, status=status)


def main():
    crealinks()
    api = get_api(authTwitter)
    followers = follow_followers(api)
    send_menu(api)

if __name__ == "__main__":
  main()

