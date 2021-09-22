from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Pitch"

    return render_template('index.html', title=title)



@main.route('/userpage', methods = ['GET', 'POST'])
@login_required
def userpage():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 
    return render_template('userpage.html')
