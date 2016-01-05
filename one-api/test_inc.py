import urllib2, json
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/one/api/v1.0/points/1', data='{"points": 1}')
request.add_header('Content-Type', 'application/json')
request.get_method = lambda: 'PUT'
response = urllib2.urlopen(request)
print(response.read())

