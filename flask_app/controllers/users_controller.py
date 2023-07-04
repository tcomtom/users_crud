from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users_model import User #importing the class here
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)

# Get all users
@app.route('/')
def get_all():
    return render_template('dashboard.html', users = User.get_all())

# Route to find user and redirect to show details page
@app.route('/show/<int:user_id>')
def user_details(user_id):
    print(user_id)
    session['one_user'] = User.get_one(user_id)
    return redirect('/show')

# Display user details page
@app.route('/show')
def show_user():
    return render_template('user.html')

# Display add user form
@app.route('/new', methods=['GET']) #Post request route
def user_form():
    return render_template('new.html')

# Add new uaer
@app.route('/new_user', methods=['POST'])
def add_user():
    print(request.form)
    result = User.insert_user(request.form)
    return redirect('/')

# Find user info to edit. 
@app.route('/edit_user/<int:user_id>')
def get_user(user_id):
    session['one_user'] = User.get_one(user_id)
    return redirect('/edit_user')

# Display user edits page
@app.route('/edit_user')
def user_edit_page():
    return render_template('edit.html')

# Updated user info
@app.route('/edit_user/process', methods=['POST'])
def update_user():
    data = {
        'id':request.form['id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    print(data)
    result = User.edit_one(data)
    return redirect('/')

# Delete user
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    result = User.delete_user(data)
    return redirect('/')




