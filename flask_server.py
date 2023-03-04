from flask import Flask, render_template, url_for, request, redirect
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

import requests
import datetime as dt

import db_select_za4_weapons as weapons_data
import db_insert_za4_blog as insert_post
import db_select_za4_blog as blog_data


# Variables
today = dt.datetime.today()
year = today.year

weapon_props = weapons_data.data_obj
blog_posts = blog_data.data_obj

posts_list = requests.get('https://api.npoint.io/4dd63b3f272cf31cc86f').json()


# Start the Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


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
    return render_template('za4_weapons.html', props=weapon_props, year=year)


@app.route('/za4_blog')
def za4_blog():
    if request.method == 'POST':
        data = request.form.get('ckeditor')
    return render_template("za4_blog.html", posts=blog_posts, year=year)


@app.route('/za4_show_post/<int:id>')
def za4_show_post(id):
    requested_post = None
    for post in posts_list:
        if post["id"] == id:
            requested_post = post
    return render_template("za4_show_post.html", post=requested_post, year=year)


@app.route('/za4_create_post', methods=["GET", "POST"])
def za4_create_post():
    form = CreatePostForm()
    # working on this from code below
    # if form.validate_on_submit():

    #     return redirect(url_for("get_all_posts"))
    return render_template("za4_create_post.html", form=form, year=year)


# may need to use some of the following to replace what I currently have in order to submit a post from form
# @app.route("/new-post", methods=["GET", "POST"])
# def add_new_post():
#     form = CreatePostForm()
#     if form.validate_on_submit():
#         new_post = BlogPost(
#             title=form.title.data,
#             subtitle=form.subtitle.data,
#             body=form.body.data,
#             img_url=form.img_url.data,
#             author=form.author.data,
#             date=date.today().strftime("%B %d, %Y")
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for("get_all_posts"))
#     return render_template("make-post.html", form=form)
##########

# @app.route('/za4_edit_post/<int:id>')
# def za4_edit_post(id):
#     requested_post = None
#     for post in posts_list:
#         if post["id"] == id:
#             requested_post = post
#     return render_template("za4_post.html", post=requested_post, post_id=post["id"], year=year)


if __name__ == "__main__":
    app.run(debug=True)
