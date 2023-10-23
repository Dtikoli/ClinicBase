#!/usr/bin/python3
""" login and authentication utils """

from clinic_app import bcrypt, login_manager
from models import storage
from flask import current_app, session
# from models import User

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
        session['custom_user'] = custom_admin
        return custom_admin

    user = dbsesion.query(User).filter_by(email=user_email).first()
    if user and bcrypt.check_password_hash(user.password, user_pass):
        return user
    return None


@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)
