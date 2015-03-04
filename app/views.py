from app import app
from flask import Flask, render_template

# HOMEPAGE
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

# LOGIN
@app.route('/login')
def login():
  return render_template('login.html')

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
@app.route('/host')
def host():
	return render_template('video-host-setup.html')

# COMING SOON
@app.route('/cs')
@app.route('/comingsoon')
def comingsoon():
  return render_template('comingsoon.html')


