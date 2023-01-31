#!/usr/bin/python

'''
Through-the-web command line client for mol2chemfig.
Depends only on Python standard library modules.
'''

import sys, http.client, urllib.request, urllib.parse, urllib.error

serverUrl = "localhost:80"
servlet = "/mol2chemfig/test"

def rpc(**data):
    '''
    send rpc request and return response data
    '''
    params = urllib.parse.urlencode(data)
    headers = {"Content-type": "application/x-www-form-urlencoded"}

    conn = http.client.HTTPConnection(serverUrl)
    conn.request("POST", servlet, params, headers)

    response = conn.getresponse()
    result = response.read()
    conn.close()

    return result


# rudimentary input parsing. the full option parsing happens on the server.
progname, rawinput = sys.argv[0], sys.argv[1:]

if not rawinput:
    rawdata = ''
else:
    rawdata = rawinput.pop()

rawoptions = ' '.join(rawinput)

if rawdata and not '-d' in rawoptions and not '--direct-input' in rawoptions:
    try:
        data = open(rawdata).read()
    except IOError:
        sys.exit("Can't read file %s" % rawdata)
else:
    data = rawdata  # use any data directly as input

result = rpc(progname=progname, options=rawoptions, cargo=data)

print(result)

