from flask import Flask, jsonify, abort, make_response, request, url_for, Blueprint
from flask.ext.pymongo import MongoClient

signup_api = Blueprint('signup_api',__name__)

# curl -i -H "Content-Type: application/json" -X PUT -d '{"email":"akjshdkas", "password":"auhsiduahi"}' http://localhost:5000/api/user/register
@signup_api.route('/api/user/register',methods=['PUT'])
def register():
	client = MongoClient()
	db = client.app_users
	email = request.json.get('email', None)
	password = request.json.get('password', None)
	cred = {"email":email,"password":password}
	post = db.users
	posted_id = post.insert_one(cred).inserted_id
	return jsonify({'success': True, 'email': email, 'password': password})
