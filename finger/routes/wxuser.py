from flask import Flask, request,session
from flask_restful import Api, Resource, reqparse
from app import app
from models import Users
api = Api(app)


class WxUser(Resource):
	def get(self):
		print('调用get')
		print(request.args)
		print(request.args.to_dict())
		print(request.args.get('email'))
		print(request.args.get('pwd'))
		return {'hello': 'world'}
	def post(self):
		print('调用post')
		#req = parser.parse_args(strict=True)
		#json_data = parser.parse_args(force=True)

		# print(request.form.get('email'))
		email=request.get_json()['email']
		pwd=request.get_json()['pwd']
		u = Users.objects(email=email,pwd=pwd).first()
		if u!=None:
			loginbean = {'id':str(u._id),'nicheng':u.nicheng,'role':u.role,'msgnum':u.msgnum}
			session['loginbean']=loginbean
			print(session['loginbean'])
			return loginbean
			# return redirect('/home')
			# return '登录成功'
		else:
			return '账号/密码错误'
		
api.add_resource(WxUser, "/wxuser") # 设置路由
