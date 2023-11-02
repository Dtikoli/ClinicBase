#!/usr/bin/python3
""" Handle the user session routes """

from dashboards.auth import bp_auth
from flask import (request, redirect, url_for, flash,
                   render_template, session, current_app)
from flask_login import login_user, logout_user, current_user
from dashboards.auth.utils import custom_authentication, check_inactivity
from models.optometrist import Optometrist
from models.receptionist import Receptionist


@bp_auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ handles session login """
    if current_user.is_authenticated:
        if isinstance(current_user, Receptionist):
            return redirect(url_for('receptionist.recep'))
        elif isinstance(current_user, Optometrist):
            return redirect(url_for('optometrist.optom'))
        else:
            return redirect(url_for('admin.admin'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = custom_authentication(current_app, email, password)

        if isinstance(user, Receptionist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('recep.recep'))
        elif isinstance(user, Optometrist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('optom.optom'))
        elif user:
            user = session.get('custom_user')
            flash('Login successful.', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')


@bp_auth.route('/logout', strict_slashes=False)
def logout():
    if 'custom_user' in session:
        session.pop('custom_user')
    else:
        logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.home'))


@bp_auth.before_request
def before_request():
    if check_inactivity('custom_user'):
        return redirect(url_for('auth.login'))
