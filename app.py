from flask import Flask, jsonify, abort, make_response, request, url_for, render_template, redirect
from flask.ext.pymongo import PyMongo
from api.signup import signup_api
from api.forms import LoginForm

app = Flask(__name__)
app.register_blueprint(signup_api)
#app.config.from_object('config')
mongo = PyMongo(app, config_prefix='Mongo')

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}),404)

@app.route('/')
def hello():
	return "Hello world!"

#@app.route('/home')
#def home():
#	online_users = mongo.db.users.find({'online': True})
#	return "Hello bye bye {}!".format(online_users)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	user = {'nickname':'mkmde'}
	if form.validate_on_submit():
		return redirect('/index')
	return render_template('login.html',title='Sign IN', user=user, form=form)

@app.route('/index')
def index():
	user={'nickname':'daddy'}
	return render_template('index.html',title='home', user=user)

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)
