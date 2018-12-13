# -*- coding: utf-8 -*-

import os, sys
import hashlib
import datetime
import json
from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)

message_list = ('Your machine has been activated.', 
                'Your session has ended.')
g_resp_info ='''
{
	"success":{
		"idInstall":"Kf9OL9e20mIGrxQewB2k873wzsa138QliOPhNqCM",
		"idSession":"z0Fb3ybc4H9SsvTn6Y1Yhxrsj2xp0TuAQ1OwWIoX",
		"info":{
			"canCheckout":0,
			"expirationDate":"2018-12-22",
			"heartRate":1,
			"installationsUsed":1,
			"licenseCode":"qZctdkhGoKXdRtuR",
			"licenseType":"Trial",
			"licenseTypeCode":2,
			"numberOfConcurrentUses":1,
			"numberOfDaysWithoutHeartbeat":15,
			"numberOfInstalls":1,
			"offlineCode":"",
			"singleUse":null
		},
		"killCode":0,
		"message":"Your machine has been activated.",
		"statusCode":200
	}
}
'''

def parse_args(form_info):
    '''POST Args '''
    return form_info

def prepare_result(licenseCode):
    ''''''
    json_ret =  json.loads(g_resp_info)
    print json_ret
    json_ret['success']['info']['expirationDate'] = '2100-12-30'
    json_ret['success']['info']['licenseCode'] = licenseCode
    json_ret['success']['info']['licenseType'] = 'Commercial'
    json_ret['success']['info']['licenseTypeCode'] = 5
    return json.dumps(json_ret)

@app.route('/api/v1/start', methods=['POST'])
def api_start() :
    ''' start api'''
    if request.method != 'POST':
        return "Hehe , Get"
    req_info = parse_args(request.form)
    if req_info.has_key('idProduct'):
        print  req_info['idProduct']
    if req_info.has_key('idMachine'):
        print  req_info['idMachine']
    if req_info.has_key('nameMachine'):
        print  req_info['nameMachine']
    if req_info.has_key('licenseCode'):
        print  req_info['licenseCode']

    ret =  prepare_result(req_info)
    print "*** HTTP Return : ", ret
    return ret

@app.route('/api/v1/quit', methods=['POST'])
def api_quit() :
    if request.method != 'POST':
        return "Hehe , Get"
    req_info = parse_args(request.form)
    ret = prepare_result(req_info)
    print "*** HTTP Return : ", ret
    return ret

@app.route('/api/v1/getTrial', methods=['POST'])
def api_getTrial() :
    if request.method != 'POST':
        return "Hehe , Get"
    req_info = parse_args(request.form)
    ret = prepare_result(req_info)
    print "*** HTTP Return : ", ret
    return ret

@app.route('/api/v1/register', methods=['POST'])
def api_register() :
    if request.method != 'POST':
        return "Hehe , Get"
    req_info = parse_args(request.form)
    ret = prepare_result(req_info)
    print "*** HTTP Return : ", ret
    return ret

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5200, debug=True, threaded=True, use_reloader=False)