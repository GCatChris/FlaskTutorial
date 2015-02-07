from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Chris'} #Fake user
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'Fred'},
			'body': 'Beautiful Day in my living room!'
		},
		{
			'author': {'nickname': 'Doug'},
			'body': 'The new Max Martin song kicks ass!'
		}
		]
	return render_template('index.html',
				title='Home',
				user=user,
				posts=posts)
