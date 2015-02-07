from app import app
import socket

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Chris'} #Fake user
	return '''
<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
		<h1>Hello, ''' + user['nickname'] + '''</h1>
	</body>
</html>
'''
