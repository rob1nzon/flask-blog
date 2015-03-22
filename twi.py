#!/usr/bin/env python
# -*- coding: utf-8 -*-
import twitter

def get_twit():
  #import twitter
  api = twitter.Api(consumer_key='2e0ahJ9GxVPTO0QOyQuFjA',consumer_secret='PKGCA5GRxIWsB4FisVOmA2CtfhQBOaNXWJ5yHYfZ5w',access_token_key='16490437-Mq2fsXvQ426bRlJmKn1ppbmcGPWcm84hKLsT07Xg',access_token_secret='Jy5WbooPnIaM2oEEGCPGD3nh8rvNlXUSQvH3eKYrU4')
  print api.VerifyCredentials()
  statuses = api.GetUserTimeline(screen_name='rob1nzon')
  return [s.text for s in statuses]

#print get_twit()
