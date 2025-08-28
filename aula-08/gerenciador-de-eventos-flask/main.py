from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from config import app, db
from models import User, Evento
from formulario import FormularioEvento
from forms import RegisterForm, LoginForm

"""
pip install flask, flask-wtf
flask_sqlalchemy, flask_login

"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data
        
        usu_ex = User.query.filter_by(username=usu).first()

        if usu_ex:
            pass  # Usuário já existe
        else:
            novo_usuario = User(username=usu)
            novo_usuario.set_password(sen)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('register.html', form=formulario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    formulario = LoginForm()
    
    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data
        
        user = User.query.filter_by(username=usu).first()
        
        if user and user.check_password(sen):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            pass  # Usuário ou senha inválidos
    
    return render_template('login.html', form=formulario)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    eventos = Evento.query.filter_by(id_usuario=current_user.id).all()
    eventos_todos = Evento.query.all()
    return render_template('dashboard.html', eventos=eventos, eventos_todos=eventos_todos)

@app.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    formulario = FormularioEvento()

    if formulario.validate_on_submit():
        nome = formulario.nome.data
        desc = formulario.descricao.data
        dat = formulario.data.data

        novoEvento = Evento(nome=nome, descricao=desc, dataEvento=dat, id_usuario=current_user.id)
        db.session.add(novoEvento)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('create_event.html', form=formulario)

@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    evento = Evento.query.get_or_404(event_id)
    
    if evento.id_usuario != current_user.id:
        return redirect(url_for('dashboard'))
    
    formulario = FormularioEvento()
    
    if formulario.validate_on_submit():
        evento.nome = formulario.nome.data
        evento.descricao = formulario.descricao.data
        evento.dataEvento = formulario.data.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    # Preencher formulário com dados existentes
    formulario.nome.data = evento.nome
    formulario.descricao.data = evento.descricao
    formulario.data.data = evento.dataEvento
    
    return render_template('edit_event.html', form=formulario, evento=evento)

@app.route('/delete_event/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    evento = Evento.query.get_or_404(event_id)
    
    if evento.id_usuario != current_user.id:
        return redirect(url_for('dashboard'))
    
    db.session.delete(evento)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/events')
def events():
    eventos = Evento.query.all()
    return render_template('events.html', eventos=eventos)

@app.route('/perfil')
@login_required
def perfil():
    meus_eventos = Evento.query.filter_by(id_usuario=current_user.id).all()
    return render_template('perfil.html', usuario=current_user.username, eventos=meus_eventos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
