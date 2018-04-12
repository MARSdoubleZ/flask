
from flask import render_template,request,redirect,session
from app import app
import time
from models import Users

@app.route('/login',methods=['POST']) 
def login():
	if request.method == 'POST':
		email=request.form.get('email')
		pwd=request.form.get('pwd')
		u = Users.objects(email=email,pwd=pwd).first()
		if u!=None:
			loginbean = {'id':str(u._id),'nicheng':u.nicheng,'role':u.role,'msgnum':u.msgnum}
			session['loginbean']=loginbean
			return redirect('/home')
			# return '登录成功'
		else:
			return '账号/密码错误'

@app.route('/zhuce',methods=['POST']) 
def zhuce():
	if request.method == 'POST':
		u = Users()
		list = ['email','pwd','nicheng','tel']
		for item in list:
			u[item]=request.form.get(item)
		u.role=1
		u.msgnum=0
		updtime = time.time()
		u.updtime = updtime
		u.createtime = updtime
		try:
			u.save()
			return '<script>alert("注册成功");location.href="/";</script>'
		except Exception as err:
			estr = str(err)
			if estr.find('emailuiq')>0:
				return 'email重复'
			elif estr.find('teluiq')>0:
				return '电话号码重复'
			elif estr.find('nichenguiq')>0:
				return '昵称重复'
			else:
				return '数据库异常'

@app.route('/logout',methods=['GET']) 
def logout():
	if 'loginbean' in session:
		del session['loginbean']
	return redirect('/')

@app.route('/wxlogin',methods=['POST']) 
def wxlogin():
	if request.method == 'POST':
		return '登陆成功'
