from flask import Flask, request,session
from flask_restful import Api, Resource, reqparse
from app import app
from models import Shops
from models import Dishs
from models import Dishsorts
import json 

api = Api(app)

class WxEnterRRt(Resource):
	def get(self):
		flowid = request.args.get('flowid')
		shop = Shops.objects(flowid=flowid).first()
		dishsorts = Dishsorts.objects(shopid=shop._id).all()
		sortid=dishsorts[0]._id
		dishes = Dishs.objects(sortid=sortid).all()
		list = [shop.shopname,dishsorts.to_json(),dishes.to_json()]
		return json.dumps(list)
class getDishBySortid(Resource):
	def get(self):
		sortid = request.args.get('sortid') #从前端接受菜的类别的id
		dishes = Dishs.objects(sortid=sortid).all()  #根据菜的id在数据库中查询出所有的菜
		print(dishes.to_json())  
		return json.dumps(dishes.to_json())  #把菜转成字符串传给前端


	

class WxDish(Resource):
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
		
api.add_resource(WxEnterRRt, "/wxenterRRt") # 设置路由
api.add_resource(getDishBySortid, "/getdishBySortid") # 设置路由

