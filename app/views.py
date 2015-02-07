from app import app
import socket

@app.route('/')
@app.route('/index')
def index():
	host = socket.gethostname()
	ip = socket.gethostbyname(host)
	output = "Hello %s from %s" % (host, ip)
	return output
