from flask import render_template,request,session,redirect
from app import app
from models import Admins
from models import Shops
from models import Users
from models import Msgs
from models import Shopflow
import time

@app.route('/adminLogin',methods=['POST']) 
def adminLogin():
	if request.method == 'POST':
		email=request.form.get('email')
		pwd=request.form.get('pwd')
		u = Admins.objects(email=email,pwd=pwd).first()
		if u!=None:
			adminbean = {'id':str(u._id),'email':u.email,'role':u.role}
			session['adminbean']=adminbean
			return redirect('/applyList')
			# return '登录成功'
		else:
			return '账号/密码错误'

@app.route('/adminhome',methods=['GET']) 
def adminhome():
	if 'adminbean' in session:
		adminbean = session['adminbean'] 
		return render_template('admin/adminhome.html',adminbean=adminbean)
	else:
		return '<script>alert("session过期，请重新登陆");location.href="/";</script>'

@app.route('/adminlogout',methods=['GET']) 
def adminlogout():
	if 'adminbean' in session:
		del session['adminbean'] 
	return render_template('index.html')


@app.route('/applyList',methods=['GET']) 
def applyList():
	if 'adminbean' in session:
		adminbean = session['adminbean']
		applist = Shops.objects(flag=0).all()
		return render_template('admin/applyList.html',applist=applist)
	else:
		return '<script>alert("session过期，请重新登陆");location.href="/";</script>'

@app.route('/shopinfo',methods=['GET']) 
def shopinfo():
	#检验session
	#接收shopid
	#查库，结果集rs
	#渲染到页面
	if 'adminbean' in session:
		adminbean = session['adminbean']
		shopid = request.args.get('shopid')
		rs = Shops.objects(_id=shopid).first()
		return render_template('admin/shopinfo.html',rs=rs)
	else:
		return '<script>alert("session过期，请重新登陆");location.href="/";</script>'

@app.route('/refuseShopApply',methods=['POST']) 
def refuseShopApply():
	if 'adminbean' in session:
		adminbean = session['adminbean']
		shopid=request.form.get('shopid')
		uid=request.form.get('uid')
		msg=request.form.get('msg')
		
		u = Users.objects(_id=uid).update(set__role=1)
		rs = Shops.objects(_id=shopid).update(set__flag=-1)
		m = Msgs()
		m.sendflag=0
		m.sendid=adminbean['id']
		m.sendname='管理员'
		m.recflag=1
		m.recid=uid
		m.msg=msg
		m.createtime=time.time()
		m.save()


		return redirect('/applyList')
	else:
		return '<script>alert("session过期，请重新登陆");location.href="/";</script>'

@app.route('/agreeShopApply',methods=['GET']) 
def agreeShopApply():
	if 'adminbean' in session:
		adminbean = session['adminbean']
		#接参
		#修改users,shops,插入msgs表
		shopid=request.args.get('shopid')
		uid=request.args.get('uid')

		Shopflow.objects().update(inc__flowid=1)
		shopflow=Shopflow.objects().first()
		rs = Shops.objects(_id=shopid).update(set__flag=1,set__flowid=shopflow.flowid)

		u = Users.objects(_id=uid).update(set__role=3)
		m = Msgs()
		m.sendflag=0
		m.sendid=adminbean['id']
		m.sendname='管理员'
		m.recflag=1
		m.recid=uid
		m.msg='您的商家申请已通过考核'
		m.createtime=time.time()
		m.save()

		return redirect('/applyList')
	else:
		return '<script>alert("session过期，请重新登陆");location.href="/";</script>'

