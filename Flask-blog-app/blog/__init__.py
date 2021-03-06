from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RedactedForGit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'RedactedForGit'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin 
from blog.views import AdminView 
from blog.models import User, Post, Comment 
admin = Admin(app, name='Admin panel', template_mode='bootstrap3') 
admin.add_view(AdminView(User, db.session)) 
admin.add_view(AdminView(Post, db.session)) 
admin.add_view(AdminView(Comment, db.session))