import os
from flask import render_template,request,session,redirect
from app import app
from flask_uploads import UploadSet, configure_uploads, IMAGES,patch_request_class,secure_filename
from models import Shops
from models import Dishsorts
from models import Dishs

# UPLOAD_FOLDER=os.getcwd()+r'\static\photos\idcards'
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF'])

photos = UploadSet('photos', IMAGES) #创建UploadSet 拿到UploadSet对象 并设置文件类型为image


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/sortmanager',methods=['GET']) 
def sortmanager():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		myshops = Shops.objects(uid=loginbean['id'],flag=1).first()		#多个商店为all()
		sortList = Dishsorts.objects(shopid=myshops._id).all()
		return render_template('dish/sortmanager.html',loginbean=loginbean,shopid=myshops._id,sortList=sortList,flowid=myshops.flowid)
	else:
		return '<script>alert("session过期,请重新 登录");location.href="/";</script>'



@app.route('/addSort',methods=['POST']) 
def addSort():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		ds = Dishsorts()
		ds.shopid = request.form.get('shopid')
		ds.uid = loginbean['id']
		ds.sortname = request.form.get('sortname')
		ds.save()
		return redirect('/sortmanager')
	else:
		return '<script>alert("session过期,请重新 登录");location.href="/";</script>'


@app.route('/updataSort',methods=['POST']) 
def updataSort():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		sortid = request.form.get('sortid')
		sortname = request.form.get('sortname')
		if sortname!='':
			Dishsorts.objects(_id=sortid).update(set__sortname=sortname)
		return redirect('/sortmanager')
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'

@app.route('/deletesort',methods=['GET']) 
def deletesort():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		sortid = request.args.get('sortid')
		# print(sortid)
		sortname = Dishsorts.objects(_id=sortid)  #根据菜品类别的流水id和前端传过来的sortid进行对比，如果一致就拿出来
		# print(sortname)
		sortname.delete()  #删除
		return redirect('/sortmanager')
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'


@app.route('/dishmanager',methods=['GET']) 
def dishmanager():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		myshops = Shops.objects(uid=loginbean['id'],flag=1).first()		#多个商店为all()
		dishList = Dishsorts.objects(shopid=myshops._id).all()
		sortid=dishList[0]._id
		if request.args.get('sortid')!=None:
			sortid = request.args.get('sortid')
		ds=Dishs.objects(sortid=sortid).all()
		return render_template('dish/dishmanager.html',loginbean=loginbean,shopid=myshops._id,dishList=dishList,ds=ds)
	else:
		return '<script>alert("session过期,请重新 登录");location.href="/";</script>'

@app.route('/addDish',methods=['POST']) 
def addDish():
	if 'loginbean' in session:
		loginbean = session['loginbean']	
		d = Dishs()
		shopid=request.form.get('shopid')
		sortid=request.form.get('sortid')
		print(sortid)
		d['uid'] = loginbean['id']
		d['dishname'] = request.form.get('dishname')
		d['price'] = float(request.form.get('price'))
		d['sortid'] = request.form.get('sortid')
		
		app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+ '/static/dishimgs' # 文件储存地址
		configure_uploads(app, photos) #使用configure_uploads()方法注册并完成相应的配置
		if 'photo' in request.files:
			f = request.files['photo']
			if f and allowed_file(f.filename):
				filename = photos.save(request.files['photo'])
				d['photo']='/static/dishimgs/'+filename
		d.save()
		
		return redirect('./dishmanager?sortid='+d.sortid)
	else:
		return '<script>alert("session过期,请重新 登录");location.href="/";</script>'

@app.route('/updataDish',methods=['POST']) 
def updataDish():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		dishid = request.form.get('dishid')
		dishname = request.form.get('dishname')
		if dishname!='':
			Dishsorts.objects(_id=dishid).update(set__dishname=dishname)
		return redirect('/dishmanager')
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'


@app.route('/deletedish',methods=['GET']) 
def deletedish():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		dishid = request.args.get('dishid')
		dishname = Dishs.objects(_id=dishid)
		dishname.delete()
		return redirect('/dishmanager')
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'

