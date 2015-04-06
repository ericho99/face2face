from app import app, lm
from app.models import *
from flask import Flask, render_template
from flask import url_for, redirect, request, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import RegistrationForm, LoginForm
from config import config, interface
import random, math
from random import randint

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

# HOMEPAGE
@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        user = User.query.filter(User.username==username).first()
        if user!=None and user.psw == form.password.data:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            error="Username or password incorrect"

    return render_template('login.html', form=form, error=error)
# @app.route('/user/<username>')
# def profile(username):
#     pass
@app.route('/register', methods=['GET', 'POST'])
def register():
    # need to take info from the form and create a user databse
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        added_user = User(username = form.username.data, email = form.email.data, 
            psw = form.password.data, credit = 0, paypal_username = "")
        db.session.add(added_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# DASHBOARD
# -login dependent
@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dashboard.html')

# JOIN STREAM
@app.route('/join')
def join():
    return render_template('joinable-streams.html')

# HOST STREAM
@app.route('/host', methods=['GET', 'POST'])
@login_required
def host():
    if request.method == 'POST':
        r = randint(100,1000000000)
        s = StreamHosts(start_time=datetime(2015,4,5,1,30),end_time=datetime(2015,4,5,2,30),stream_price=request.form['price'],stream_number=r,stream_name=request.form['streamname'],description=request.form['description'],embed_url=request.form['url'],host_id=current_user.id)
        db.session.add(s)
        db.session.commit()
        return redirect('/live/'+str(r))
    return render_template('video-host-setup.html')

# HOST STREAM
@app.route('/about')
def about():
    return render_template('about.html')

# TEAM PAGE
@app.route('/team')
def team():
    return render_template('team.html')

# COMING SOON
@app.route('/cs')
@app.route('/comingsoon')
def comingsoon():
  return render_template('comingsoon.html')

@app.route("/live/<int:streamno>")
@login_required
def live(streamno):
    s = StreamHosts.query.filter(StreamHosts.stream_number==streamno).first()
    return render_template('livestream.html',url=s.embed_url)

@app.route("/addcredits", methods = ['GET', 'POST'])
@login_required
def add_credits():
    user=User.query.filter(User.username==current_user.username).first()
    if user is None:
        return redirect('/register')
    if user.credit is None:
        user.credit=0
        db.session.commit()

    if request.method == 'POST':
        addcredits=request.form['amount']
        return redirect(url_for('paypal_redirect', amount=addcredits))

    return render_template('credits.html', currentcredits=user.credit)

# paypal recharge credits
@app.route('/paypal/redirect/<string:amount>')
@login_required
def paypal_redirect(amount):
    kw = {
        'amt': amount,
        'currencycode': 'USD',
        'returnurl': url_for('paypal_confirm', _external=True),
        'cancelurl': url_for('paypal_cancel', _external=True),
        'paymentaction': 'Sale'
    }

    setexp_response = interface.set_express_checkout(**kw)
    return redirect(interface.generate_express_checkout_redirect_url(setexp_response.token))

@app.route('/paypal/confirm')
@login_required
def paypal_confirm():
    getexp_response = interface.get_express_checkout_details(token=request.args.get('token', ''))

    if getexp_response['ACK'] == 'Success':
        return render_template('paymentconfirm.html', token=getexp_response['TOKEN'], amount=getexp_response['AMT'])
    else:
        return render_template('paymenterror.html', error=getexp_response['ACK'])

@app.route("/paypal/do/<string:token>")
@login_required
def paypal_do(token):
    getexp_response = interface.get_express_checkout_details(token=token)
    kw = {
        'amt': getexp_response['AMT'],
        'paymentaction': 'Sale',
        'payerid': getexp_response['PAYERID'],
        'token': token,
        'currencycode': getexp_response['CURRENCYCODE']
    }
    interface.do_express_checkout_payment(**kw)   

    return redirect(url_for('paypal_status', token=kw['token']))

@app.route("/paypal/status/<string:token>")
@login_required
def paypal_status(token):
    checkout_response = interface.get_express_checkout_details(token=token)

    if checkout_response['CHECKOUTSTATUS'] == 'PaymentActionCompleted':
        user=User.query.filter(User.username==current_user.username).first()
        addcredit=float(checkout_response['AMT'])
        user.credit=user.credit+addcredit
        db.session.commit()

        return redirect(url_for('dashboard'))
    else:
        return render_template('paymenterror.html', error=checkout_response['CHECKOUTSTATUS'])

@app.route("/paypal/cancel")
@login_required
def paypal_cancel():
    return redirect(url_for('index'))





