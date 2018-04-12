# -*- coding: utf-8 -*-

from app import app
import routes.index
import routes.user
import routes.home
import routes.admin
import routes.dish
import routes.wxuser
import routes.wxdish
		
if __name__ == '__main__':  
    app.run(host = '0.0.0.0',port=5000,debug=True)