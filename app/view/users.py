from . import view
from app.models import User
from datetime import datetime
from werkzeug.security import check_password_hash
from flask import render_template, request, session, redirect


@view.route('/admin', methods=['GET','POST'])
def admin():
    login =session.get('login')
    if login:
        time = session.get('time')
        now = datetime.now().strftime('%Y-%m-%d')
        if time != now:
            return redirect('/logout')
        elif login:
            return redirect('/')
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            current = datetime.now().strftime('%Y-%m-%d')
            session['login'] = True
            session['username'] = user.username
            session['time'] = current
            return redirect('/')
        elif user:
            message = 'password salah'
        else:
            message = 'username tidak ditemukan'
    return render_template('admin.html', message=message)

@view.route('/logout', methods=['GET'])
def logout():
    session.pop('login', None)
    session.pop('username', None)
    session.pop('time', None)
    return redirect('/')
