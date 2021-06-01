from flask import render_template, session, request, url_for, redirect, flash


from loja import app, db, bycrpt
from .formulario import RegistrationForm, LoginFormulario
from .models import User
import os


@app.route('/')
def home ():
    return render_template('admin/index.html', title='Pagina Administrativa')
    
    

@app.route('/carrinho')
def admin():
    if 'email' not in session:
        flash('Fazer primeiro o login no sistema ou registrese', 'danger')
        return redirect(url_for('login'))
    return render_template('admin/carrinho.html', title='Pagina Administrativa')


@app.route('/registrar', methods=['GET','POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():        
        hash_password = bycrpt.generate_password_hash(form.password.data)        
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password= hash_password)        
        db.session.add(user)
        db.session.commit()
        flash(f'obrigado {form.name.data} por registrar', 'success')
        return redirect(url_for('home'))  
    else: 
        return render_template('admin/registrar.html', form=form , title="Pagina de registro")


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bycrpt.check_password_hash(user.password, form.password.data):
            session['email']= form.email.data
            flash(f'Ola {form.email.data} , voce esta logado', 'success')
            return redirect(request.args.get('next')or url_for('admin'))
        else:
            flash('Nao foi possivel logar no sistema')
    return render_template('admin/login.html', form=form, title='Pagina Login')

