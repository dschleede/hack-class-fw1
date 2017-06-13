#!/usr/bin/python
# The following lines require manual changes 
username = "secretvcsuser" # enter your username
password = "reallyreallysecret1234" # enter your password 
# This example establishes a https connection, but doesn't provide the server certificate validation. 
# Production code should implement certificate validation.
# -------------------------------------------------
import httplib
import base64 

# create HTTP basic authentication string, this consists of 
# "username:password" base64 encoded 
auth = base64.encodestring("%s:%s"%(username,password))[:-1]
webservice = httplib.HTTPSConnection("my.devicecloud.com")

# to what URL to send the request with a given HTTP method
webservice.putrequest("GET", "/ws/v1/streams")

# add the authorization string into the HTTP header
webservice.putheader("Authorization", "Basic %s"%auth)

webservice.endheaders()

# get the response
response = webservice.getresponse()
statuscode = response.status
statusmessage = response.reason
response_body = response.read()

# print the output to standard out
print (statuscode, statusmessage)
print response_body
