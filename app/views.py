from app import app
from app.models import *
from flask import Flask, render_template
from flask import url_for, redirect, request, flash
from .forms import RegistrationForm
from config import config, interface
import random
from random import randint

# HOMEPAGE
@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
@app.route('/')
def login():
    error = None
    if request.method == 'POST':
        # dummy until we get the user database working
        current_user = User.query.filter_by(username = request.form['username']).first()
        if current_user.psw != request.form['password']:
            error = 'Invalid username or password. Please try again.'
        else:
            return redirect(url_for('dashboard')) # once logged in go to payment page
    return render_template('login.html', error=error)
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

# DASHBOARD
# -login dependent
@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

# JOIN STREAM
@app.route('/join')
def join():
    return render_template('joinable-streams.html')

# HOST STREAM
@app.route('/host', methods=['GET', 'POST'])
def host():
    if request.method == 'POST':
        r = randint(100,1000000000)
        s = StreamHosts(start_time=datetime(2015,4,5,1,30),end_time=datetime(2015,4,5,2,30),stream_price=request.form['price'],stream_number=r,stream_name=request.form['streamname'],description=request.form['description'],embed_url=request.form['url'],host_id=1)
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

# testing the payment capability
# @app.route('/soytest')
# def soytest():
#    return render_template('soytest.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

# will need to make this variable for different price classes
@app.route('/paypal/redirect/<string:amount>')
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
def paypal_confirm():
    getexp_response = interface.get_express_checkout_details(token=request.args.get('token', ''))

    if getexp_response['ACK'] == 'Success':
        return render_template('paymentconfirm.html', token=getexp_response['TOKEN'])
    else:
        return render_template('paymenterror.html', error=getexp_response['ACK'])

@app.route("/paypal/do/<string:token>")
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
def paypal_status(token):
    checkout_response = interface.get_express_checkout_details(token=token)

    if checkout_response['CHECKOUTSTATUS'] == 'PaymentActionCompleted':
        return redirect(url_for('live'))
    else:
        return render_template('paymenterror.html', error=checkout_response['CHECKOUTSTATUS'])

@app.route("/paypal/cancel")
def paypal_cancel():
    return redirect(url_for('index'))

@app.route("/live/<int:streamno>")
def live(streamno):
    s = StreamHosts.query.filter(StreamHosts.stream_number==streamno).first()
    return render_template('livestream.html',url=s.embed_url)

@app.route("/addcredits/<string:username>", methods = ['GET', 'POST'])
def add_credits(username):
    if username is None:
        return redirect('/login')
    user=User.query.filter(User.username==username).first()
    if user is None:
        return redirect('/register')
    if user.credit is None:
        user.credit=0
        db.session.commit()

    if request.method == 'POST':
        addcredits=request.form['amount']
        return redirect(url_for('paypal_redirect', amount=addcredits))

    return render_template('credits.html', currentcredits=user.credit)






