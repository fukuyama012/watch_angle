# -*- coding: utf-8 -*- 

import requests
from config import config

class LineNotify(object):
    """NotifyClass for LINE"""
    NOTIFY_API_URL = "https://notify-api.line.me/api/notify"
    
    def __init__(self, api_url = NOTIFY_API_URL, authority = config.AUTHORITY_TOKEN):
        self.apiUrl = api_url
        self.headers = {"Authorization" : "Bearer "+ authority}
        
        
    def notify(self, message):
        payload = {"message" :  message}
        #payload = {"message" :  message, 'stickerPackageId': 2, 'stickerId': 144}
        return self._post(payload)
        
        
    def _post(self, payload):
        return requests.post(self.apiUrl, headers = self.headers, data = payload, files = "")
    