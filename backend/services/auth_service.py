"""Serviço de autenticação e autorização."""
from flask import session
<<<<<<< HEAD:backend/services/auth_service.py
from database import db
=======
from db import db, Cliente, Barber
>>>>>>> parent of 3a293ed (correção de bugs e adição de estilo):services/auth_service.py
from werkzeug.security import generate_password_hash, check_password_hash


def authenticate_user(email, password):
    """Autentica um usuário (cliente ou barbeiro)."""
    # Tentar como cliente
    cliente = db.get_client_by_email(email)
    if cliente and check_password_hash(cliente['senha'], password):
        return {**cliente, "tipo": "cliente"}
    
<<<<<<< HEAD:backend/services/auth_service.py
    # Tentar como profissional
    profissional = db.get_professional_by_email(email)
    if profissional and check_password_hash(profissional['senha'], password):
        # Retornar como 'barbeiro' para compatibilidade com o frontend
        return {**profissional, "tipo": "barbeiro"}
=======
    # Tentar como barbeiro
    barber = Barber.query.filter_by(email=email).first()
    if barber and check_password_hash(barber.senha, password):
        return {**barber.to_dict(), "tipo": "barbeiro"}
>>>>>>> parent of 3a293ed (correção de bugs e adição de estilo):services/auth_service.py
    
    return None


def register_user(nome, email, password, tipo="cliente", telefone=None):
    """Registra um novo usuário."""
    # Verificar se email já existe
<<<<<<< HEAD:backend/services/auth_service.py
    if db.get_client_by_email(email) or db.get_professional_by_email(email):
=======
    if Cliente.query.filter_by(email=email).first() or Barber.query.filter_by(email=email).first():
>>>>>>> parent of 3a293ed (correção de bugs e adição de estilo):services/auth_service.py
        return False
    
    senha_hash = generate_password_hash(password)
    
<<<<<<< HEAD:backend/services/auth_service.py
    if tipo in ["barbeiro", "profissional"]:
        # Criar profissional
        user_data = {
            'nome': nome,
            'email': email,
            'senha': senha_hash,
            'telefone': telefone,
            'categoria': categoria or "Barbeiro",
            'especialidades': servicos or [],
            'ativo': True,
            'avaliacao': 5.0,
            'total_avaliacoes': 0,
            'preco_base': 0.0,
            'disponibilidade': []
        }
        result = db.create_professional(user_data)
    else:
        # Criar cliente
        user_data = {
            'nome': nome,
            'email': email,
            'senha': senha_hash,
            'telefone': telefone
        }
        result = db.create_client_user(user_data)
=======
    if tipo == "barbeiro":
        user = Barber(nome=nome, email=email, senha=senha_hash, telefone=telefone)
    else:
        user = Cliente(nome=nome, email=email, senha=senha_hash, telefone=telefone)
>>>>>>> parent of 3a293ed (correção de bugs e adição de estilo):services/auth_service.py
    
    return result is not None


def exigir_login(tipo_requerido=None):
    """Verifica se o usuário está logado. Opcionalmente verifica o tipo."""
    if "usuario_email" not in session:
        return False
    
    if tipo_requerido and session.get("usuario_tipo") != tipo_requerido:
        return False
    
    return True


def usuario_atual():
    """Retorna os dados do usuário atual da sessão."""
    if not exigir_login():
        return None
    
    email = session.get("usuario_email")
    tipo = session.get("usuario_tipo")
    
    if tipo == "barbeiro":
<<<<<<< HEAD:backend/services/auth_service.py
        user = db.get_professional_by_email(email)
=======
        user = Barber.query.filter_by(email=email).first()
>>>>>>> parent of 3a293ed (correção de bugs e adição de estilo):services/auth_service.py
    else:
        user = db.get_client_by_email(email)
    
    return user if user else None
