from flask import render_template, request, redirect, url_for
from . import main


@main.route('/index.html')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Pitch"

    return render_template('index.html', title=title)

# @main.route('/login.html')
# def login():
#     '''
#     View login page function that returns the login page and its data
#     '''
#     return render_template('login.html')

@main.route('/signup.html')
def signup():
    '''
    View signup page function that returns the sign up page and its data
    ''' 
    return render_template('signup.html')

@main.route('/userpage.html')
def userpage():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 
    return render_template('userpage.html')
