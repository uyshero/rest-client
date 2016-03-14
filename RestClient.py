#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2



class RestClient:

    def get(self,url,header): 
        req = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(req)
        return response.read()

    def post(self,url,para,header):
        #value = urllib.urlencode(para)
        req = urllib2.Request(url,para,header)
        response = urllib2.urlopen(req)
        return response.read()
    
    def put(self,url,header):
        req = urllib2.Request(url,headers=header)
        req.get_method = lambda:'PUT'
        try:
            response = urllib2.urlopen(req)
            return response.getcode()
        except:
            return 410

    def delete(self,url,header):
        req = urllib2.Request(url,headers=header)
        req.get_method = lambda:'DELETE'
        try:
            response = urllib2.urlopen(req)
            return response.getcode()
        except:
            return 410

    def list(self,url,header):
        req = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(req)
        return response.read()


if __name__== '__main__':

    client = RestClient()
    url = "https://servicediscovery.ng.bluemix.net/api/v1/instances"
    url2 = "https://servicediscovery.ng.bluemix.net/api/v1/services/my_service01"
    url3 = "https://servicediscovery.ng.bluemix.net/api/v1/instances/ac71465238bd19ec/heartbeat"
    url4 = "https://servicediscovery.ng.bluemix.net/api/v1/instances/ac71465238bd19ec"
    url5 = "https://servicediscovery.ng.bluemix.net/api/v1/services"
    header = {'Authorization':' Bearer 15fd7abctsh88j6o82jqkee5h2s6m23vvsnaknr3kjg7r5oang7o','Content-Type':' application/json'}
    header_put = {'Authorization':' Bearer 15fd7abctsh88j6o82jqkee5h2s6m23vvsnaknr3kjg7r5oang7o','Content-Length':'0'}
    header_delete = {'Authorization':' Bearer 15fd7abctsh88j6o82jqkee5h2s6m23vvsnaknr3kjg7r5oang7o'}
    para = {"service_name":"my_service01", "endpoint": {"type":"tcp", "value":"192.168.1.32:80"}, "status":"UP", "ttl":300, "metadata":{"key":"value"}} 
    #print client.post(url,json.dumps(para),header)
    #print client.get(url2,header)
    #print client.put(url3,header_put)
    #print client.delete(url4,header_delete)
    print client.list(url5,header_delete)
