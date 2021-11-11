from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post, Comment, Favourite
from blog.forms import RegistrationForm, LoginForm, CommentForm, FavouriteForm
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_

@app.route("/")
@app.route("/home")
def home():
  posts=Post.query.order_by(Post.date.desc())
  sidebar=Post.query.all()
  return render_template('home.html',posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/post/<int:post_id>")
def post(post_id):
  post = Post.query.get_or_404(post_id)
  comments = Comment.query.filter(Comment.post_id==post.id)
  form = CommentForm()
  form2 = FavouriteForm()
  return render_template('post.html',post=post,comments=comments,form=form, form2=form2)

@app.route('/post/<int:post_id>/favourite', methods=['GET', 'POST']) 
@login_required 
def add_favourite(post_id): 
  post = Post.query.get_or_404(post_id)
  form2 = FavouriteForm() 
  if form2.validate_on_submit():
    db.session.add(Favourite(post_id=post.id, user_id=current_user.id))
    db.session.commit() 
    return redirect(f'/post/{post.id}')
  return render_template('post.html',post=post,comments=comments,form=form, form2=form2)

@app.route('/post/<int:post_id>/comment', methods=['GET', 'POST']) 
@login_required 
def post_comment(post_id): 
  post = Post.query.get_or_404(post_id) 
  form = CommentForm() 
  if form.validate_on_submit(): 
    db.session.add(Comment(content=form.comment.data, post_id=post.id, author_id=current_user.id))
    db.session.commit() 
    flash("Your comment has been added to the post", "success") 
    return redirect(f'/post/{post.id}')
  comments = Comment.query.filter(Comment.post_id == post.id)
  return render_template('post.html', post=post, comments=comments, form=form)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('Login successful!')
      return redirect(url_for('home'))
    flash('Invalid email address or password.') 
     
    return render_template('login.html',title='Login',form=form)

  return render_template('login.html',title='Login',form=form)

@app.route("/search",methods=['GET','POST'])
def search():
  query = request.args.get('q')
  if len(query)>0:
    results = Post.query.filter(or_(Post.title.contains(query),Post.content.contains(query)))
    return render_template('results.html', results=results)


@app.route("/logout")
def logout():
  logout_user()
  flash('Logout successful!')
  return redirect(url_for('home'))

@app.route("/allPostsDesc")
def allPostsDesc():
  posts=Post.query.order_by(Post.date.desc())
  return render_template('allPostsDesc.html',posts=posts)

@app.route("/allPostsAsc")
def allPostsAsc():
  posts=Post.query.order_by(Post.date.asc())
  return render_template('allPostsAsc.html',posts=posts)


@app.route("/favourite")
def favourite():
  if current_user.is_authenticated:
    post_ids = Favourite.query.filter_by(user_id = current_user.id).all()
    ids = [ post.post_id for post in post_ids ]
    results = Post.query.filter(Post.id.in_(ids)).all()
    return render_template('favourite.html',posts=results)
  return render_template('login.html')
