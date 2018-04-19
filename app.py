from flask import Flask
from extensions import login_manager
from extensions import db,migrate
from extensions import ma
#blueprints
from blueprints.pages import pages
from blueprints.user import user
from blueprints.post import post

#app setup
app=Flask(__name__,instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py',silent=True)
#blueprints
app.register_blueprint(pages)
app.register_blueprint(user)
app.register_blueprint(post)

#initialize extensions
db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)

from flask import jsonify,request,session
from blueprints.user.models import Token


# @app.before_request
def authcheck():
    # get the owner of the token,check if the user exists and set the user id in session
    token=request.headers.get('Auth')
    if token:
        tk=Token.query.filter_by(api_token=token).first()
        if not tk:
            return jsonify(code=0,message="The user does not exists")
        else:
            #set the user id in session
            session['user_id']=tk.user_id
    else:
        return jsonify(code=0,message="An error occured")



#app run
if __name__=='__main__':
    app.run()
