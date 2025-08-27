# Sistema de Gerenciamento de Eventos

Sistema completo de gerenciamento de eventos com autenticação de usuários, desenvolvido em Flask.

## Funcionalidades

### ✅ Usuários
- **Registro**: Criar nova conta com username e senha
- **Login/Logout**: Autenticação segura com sessões
- **Senhas criptografadas**: Usando Werkzeug

### ✅ Eventos
- **Criar**: Adicionar novos eventos com nome, data e descrição
- **Visualizar**: Dashboard mostra todos os eventos do usuário
- **Editar**: Modificar eventos existentes (apenas do próprio usuário)
- **Excluir**: Remover eventos (apenas do próprio usuário)

## Como Executar

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o aplicativo:**
   ```bash
   python3 main.py
   ```

3. **Acessar no navegador:**
   ```
   http://127.0.0.1:5000
   ```

## Estrutura do Projeto

```
Metade/
├── config.py          # Configuração Flask e SQLAlchemy
├── models.py          # Modelos User e Evento
├── forms.py           # Formulários de login/registro
├── formulario.py      # Formulário de eventos
├── main.py            # Rotas e lógica principal
├── requirements.txt   # Dependências
├── templates/         # Templates HTML
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── create_event.html
│   └── edit_event.html
└── instance/          # Banco SQLite (criado automaticamente)
    └── event_manager.db
```

## Tecnologias Utilizadas

- **Flask**: Framework web
- **SQLAlchemy**: ORM para banco de dados
- **Flask-Login**: Sistema de autenticação
- **Flask-WTF**: Formulários web
- **SQLite**: Banco de dados
- **Bootstrap**: Interface responsiva

## Rotas Disponíveis

- `/` - Página inicial
- `/register` - Registro de usuário
- `/login` - Login
- `/logout` - Logout
- `/dashboard` - Dashboard principal (requer login)
- `/create_event` - Criar evento (requer login)
- `/edit_event/<id>` - Editar evento (requer login)
- `/delete_event/<id>` - Deletar evento (requer login)

## Segurança

- ✅ Senhas criptografadas com hash
- ✅ Sessões seguras
- ✅ Proteção CSRF nos formulários
- ✅ Validação de permissões (usuário só acessa seus próprios eventos)
- ✅ Validação de dados nos formulários
