# -*- coding:UTF-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine
app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db'    : 'figer',
    'host'  : 'localhost',
    'port'  : 27017
}

#创建mongo原型
mdb = MongoEngine()
mdb.init_app(app)

# print(dir(mdb))

# 类名定义 collection
class Users(mdb.Document):
    _id = mdb.ObjectIdField()
    email = mdb.StringField()
    pwd = mdb.StringField()
    nicheng = mdb.StringField()
    tel = mdb.StringField()
    role = mdb.IntField()			#1表普通用户,2表店铺审核中,3表商家
    msgnum = mdb.IntField()
    updtime = mdb.FloatField()
    createtime = mdb.FloatField()

class Admins(mdb.Document):
    _id = mdb.ObjectIdField()
    email = mdb.StringField()
    pwd = mdb.StringField()
    role = mdb.IntField()

#商家表
class Shops(mdb.Document):
	_id = mdb.ObjectIdField()
	uid = mdb.ObjectIdField()
	shopname = mdb.StringField()
	address = mdb.StringField()
	lng	= mdb.FloatField()
	lat = mdb.FloatField()
	tel = mdb.StringField()
	idcard = mdb.StringField()			#身份证照片地址
	ownercard = mdb.StringField()		#手持身份证照片地址
	blicense = mdb.StringField()		#营业执照照片地址
	hlicense = mdb.StringField()		#卫生许可证照片地址
	updtime = mdb.FloatField()
	createtime = mdb.FloatField()
	flag = 	mdb.IntField()		#-2表强制终止,-1表驳回,0表审核中,1表审核通过
	flowid = mdb.LongField()    #店铺流水id

#商家流水id表 
class Shopflow(mdb.Document):
	_id = mdb.ObjectIdField()
	flowid = mdb.LongField()

#消息表
class Msgs(mdb.Document):
	_id = mdb.ObjectIdField()
	sendflag = 	mdb.IntField()	#0表管理员,1表普通用户
	sendid = mdb.ObjectIdField()
	sendname = mdb.StringField()
	recflag = mdb.IntField()		#0表管理员,1表普通用户
	recid = mdb.ObjectIdField()
	# recname = mdb.StringField()
	msg = mdb.StringField()
	createtime = mdb.FloatField()

#菜谱分类表
class Dishsorts(mdb.Document):
	_id = mdb.ObjectIdField()
	shopid = mdb.ObjectIdField()
	uid = mdb.ObjectIdField()
	sortname = mdb.StringField()

#菜品表
class Dishs(mdb.Document):
	_id = mdb.ObjectIdField()
	shopid = mdb.ObjectIdField()
	uid = mdb.ObjectIdField()
	sortid = mdb.ObjectIdField()
	dishname = mdb.StringField()
	photo = mdb.StringField()   #照片地址
	price = mdb.FloatField()   #价格
	curprice = mdb.IntField() #当前价格
	flag = mdb.IntField()   #0表上架，1表下架