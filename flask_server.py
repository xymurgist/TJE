from flask import Flask, render_template, url_for, redirect
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

import datetime as dt

from db_select_za4_weapons import select_za4_weapons
from db_select_za4_blog import select_za4_blog
from db_insert_za4_blog import insert_post


# Variables
today = dt.datetime.today()
year = today.year


# Start the Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Routes
@app.route('/')
def home():
    return render_template('index.html', year=year)


@app.route('/about')
def about():
    return render_template("about.html", year=year)


@app.route('/contact')
def contact():
    return render_template("contact.html", year=year)


@app.route("/za4_weapons")
def za4_weapons():
    weapons_props = select_za4_weapons()
    return render_template('za4_weapons.html', props=weapons_props, year=year)


@app.route('/za4_blog')
def za4_blog():
    blog_posts = select_za4_blog()
    return render_template("za4_blog.html", posts=blog_posts, year=year)


@app.route('/za4_show_post/<int:id>')
def za4_show_post(id):
    requested_post = None
    blog_posts = select_za4_blog()
    for post in blog_posts:
        if post.id == id:
            requested_post = post
    return render_template("za4_show_post.html", post=requested_post, year=year)


@app.route('/za4_create_post', methods=["GET", "POST"])
def za4_create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        insert_post(form.data)
        return redirect(url_for('za4_blog'))
    return render_template("za4_create_post.html", form=form, year=year)


# @app.route('/za4_edit_post/<int:id>')
# def za4_edit_post(id):
#     requested_post = None
#     for post in posts_list:
#         if post["id"] == id:
#             requested_post = post
#     return render_template("za4_post.html", post=requested_post, post_id=post["id"], year=year)


if __name__ == "__main__":
    app.run(debug=True)
