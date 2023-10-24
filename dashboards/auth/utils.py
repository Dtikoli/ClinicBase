#!/usr/bin/python3
""" login and authentication utils """

from clinic_app import bcrypt, login_manager
from models import storage
from flask import current_app, session, redirect, url_for
from datetime import datetime, timedelta
from models.receptionist import Receptionist
from models.optometrist import Optometrist
from models.custom_user import User

dbsession = storage._DBStorage__session
admin_email = current_app.config.get('ADMIN_EMAIL')
admin_password = current_app.config.get('ADMIN_PASSWORD')


def custom_authentication(user_email, user_pass):
    if user_email == admin_email and user_pass == admin_password:
        custom_admin = User(
            id=current_app.config.get('ADMIN_ID'),
            name=current_app.config.get('ADMIN_NAME'),
            email=admin_email,
            password=admin_password
        )
        session.permanent = True
        session['permanent_session_lifetime'] = timedelta(minutes=30)
        session['custom_user'] = {
                                  'user_data': custom_admin,
                                  'last_activity': datetime.now()
        }
        return custom_admin

    user = dbsession.query(Optometrist, Receptionist)\
        .filter_by(email=user_email).first()
    if user and bcrypt.check_password_hash(user.password, user_pass):
        return user
    return None


def check_inactivity(session_key, max_inactive_minutes=10):
    if session_key in session:
        user_data = session[session_key]['user_data']
        last_activity = session[session_key]['last_activity']
        current_time = datetime.now()
        inactive_minutes = (current_time - last_activity).total_seconds() / 60

        if inactive_minutes > max_inactive_minutes:
            session.pop(session_key)
            return True
    return False


@bp_auth.before_request
def before_request():
    if check_inactivity('custom_user'):
        return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return dbsession.query(Optometrist, Receptionist).get(user_id)
