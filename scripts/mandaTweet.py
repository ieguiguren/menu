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
from links import *

def follow_followers(api):
    '''Lee followers'''
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
#        follower.follow()
        followers.append(follower.screen_name)
    return followers

def get_api(authTwitter):
  auth = tweepy.OAuthHandler(authTwitter['consumer_key'], authTwitter['consumer_secret'])
  auth.set_access_token(authTwitter['access_token'], authTwitter['access_token_secret'])
  return tweepy.API(auth)

def send_menu(api, user = ''):
    photoPath = datapath  + "manana.jpg"
    status = ''
    if os.path.exists( photoPath ):
        if user:
          status = '@' + user + ' '
        status += u'Menú del cole para el ' + tomorrow  + ' de ' + mes[int(tmonth[:2])]
        solution = api.update_with_media(photoPath, status=status)


def main():
    crealinks()
    api = get_api(authTwitter)
    followers = follow_followers(api)
    for follower in followers:
        send_menu(api,follower)
        nap = random.randint(1, 60)
        time.sleep(nap)

if __name__ == "__main__":
  main()

