from flask import Flask, render_template, url_for, request,session,redirect
from flask_oauth import OAuth



'''
Create the Flask app variable. Pass this around whenever we want to access info about the server
'''
app = Flask(__name__)



@app.route("/")
def homepage():
    return render_template("index.html")


# Create login manager object
# login_manager = LoginManager()
# login_manager.init_app(app)

# Config for debug, take out before completion
app.config["Debug"]= True


#Facebook authentication
FACEBOOK_APP_ID = '1021233904603127'
FACEBOOK_APP_SECRET= 'b6f1714960da91b07d83900f1a8130cc'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
                            base_url = 'https://graph.facebook.com',
                            request_token_url=None,
                            access_token_url='/oauth/access_token',
                            authorize_url='https://www.facebook.com/dialog/oauth',
                            consumer_key=FACEBOOK_APP_ID,
                            consumer_secret=FACEBOOK_APP_SECRET,
                            request_token_params={'scope': ('email, ')}
                            )


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook token')


def pop_login_session():
    session.pop('logged in', None)
    session.pop('facebook_token', None)


@app.route('/facebook_login')
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized', next = request.args.get('next'), _external=True))


@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authroized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in']=True
    session['faceboook_token']=(resp['access_token'], '')

    return redirect(next_url)


@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))
'''
Flask-login functionality

@login_manager.user_loader
def load_user(userid):
    user =User.query.get(init(userid))
    if user:
        return user



Set up OAuth
App_ID: 1021233904603127


oauth = OAuth()

facebook =oauth.get_remote('facebook',
            base_url='https://graph.facebook.com/',
            request_token=None,
            access_token_url='oauth/token_access',
            authorize_url='https://www.facebook.com/dialog/oauth',
            consumer_key= '1021233904603127',
            consumer_secret="b6f1714960da91b07d83900f1a8130cc",
            request_token_params = {'scope': 'email'}
)



#Setting up token getter
@facebook.tokengetter
def get_facebook_token():
    return session.get('oauth_token')



@app.route("/login")
def login():
    next_url =request.args.get('next') or url_for('index')
    return facebook.authorize(callback=url_for('facebook_authorized', next= next_url,_external=True))

#authorization handler
@app.route("/login/authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'There was a problem logging in.')
        return redirect(next_url)
    session['oauth_token']=(resp['access_token'], '')
    user_data = facebook.get("/me").data
    user = User.query.filter(User.email == user_data['email']).first()
    if user is None:
        new_user = User(email = user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'])
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
    else login_user(user)
    return redirect(next_url)

'''

# @app.route("/verified")
# def verified():
#     return render_template("verified.html")


@app.route("/listings3")
def listings3():
    return render_template("listings3.html")

if __name__ == "__main__" :
    app.run(host='0.0.0.0')