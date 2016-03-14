#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2



class RestClient:

    def get(self,url,headers): 
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        return response.read()

    def post(self,url,para,headers):
        #value = urllib.urlencode(para)
        req = urllib2.Request(url,para,headers)
        response = urllib2.urlopen(req)
        return response.read()
    
    def put(self,url,headers):
        req = urllib2.Request(url,headers=headers)
        req.get_method = lambda:'PUT'
        try:
            response = urllib2.urlopen(req)
            return response.getcode()
        except:
            return 410

    def delete(self,url,headers):
        req = urllib2.Request(url,headers=headers)
        req.get_method = lambda:'DELETE'
        try:
            response = urllib2.urlopen(req)
            return response.getcode()
        except:
            return 410



if __name__== '__main__':

    client = RestClient()
    url = "https://myservername.cn/api/v1/instances"
    headers= {'Authorization':' Bearer 15fd7abctsh88j6o82j}
    para = {"service_name":"my_service01"} 
    print client.post(url,json.dumps(para),headers)
    print client.get(url,headers)
    print client.put(url,headers)
    print client.delete(url,headers)
