import os
from flask import render_template,request,session,redirect
from app import app
from flask_uploads import UploadSet, configure_uploads, IMAGES,patch_request_class,secure_filename
import time
from models import Shops
from models import Msgs
from models import Users

# UPLOAD_FOLDER=os.getcwd()+r'\static\photos\idcards'
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF'])

app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+ '/static/photos' # 文件储存地址
photos = UploadSet('photos', IMAGES) #创建UploadSet 拿到UploadSet对象 并设置文件类型为image
configure_uploads(app, photos) #使用configure_uploads()方法注册并完成相应的配置

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/home',methods=['GET']) 
def home():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		msglist = Msgs.objects(recflag=1,recid=loginbean['id']).all()
		return render_template('home/home.html',loginbean=loginbean,msglist=msglist)
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'

@app.route('/shopapply',methods=['GET']) 
def shopapply():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		shopRs=Shops.objects(uid=loginbean['id'],flag=-1).first()
		return render_template('home/shopapply.html',loginbean=loginbean,shopRs=shopRs)		
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'


@app.route('/subapply',methods=['POST']) 
def subapply():
	if 'loginbean' in session:
		loginbean = session['loginbean']
		if request.method == 'POST':			
			shopid=request.form.get('shopid')
			if shopid==None:
				shop = Shops()
			else:
				shop = Shops.objects(_id=shopid,uid=loginbean['id']).first()
			shop['uid'] = loginbean['id']
			shop['shopname'] = request.form.get('shopname')
			shop['address'] = request.form.get('address')
			shop['lng'] = float(request.form.get('lng'))
			shop['lat'] = float(request.form.get('lat'))
			shop['tel'] = request.form.get('tel')
			app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+ '/static/photos' # 文件储存地址
			configure_uploads(app, photos) #使用configure_uploads()方法注册并完成相应的配置

			fArr = ('idcard','ownercard','blicense','hlicense')
			for item in fArr:
				if item in request.files:
					f = request.files[item]
					print(f)
					if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
						filename = photos.save(request.files[item])
						# print(filename)
						shop[item]='/static/photos/'+filename

			updtime = time.time()
			shop.updtime = updtime
			shop.flag=0
			if shopid==None:
				shop.createtime = updtime
			shop.save()
		#--------修改users表中role=2(审核中)-------
			u = Users.objects(_id=shop.uid).update(set__role=2)
			# print(u)
			loginbean['role']=2
			session['loginbean']=loginbean
		return redirect('/home')
	else:
		return '<script>alert("session过期,请重新登录");location.href="/";</script>'

