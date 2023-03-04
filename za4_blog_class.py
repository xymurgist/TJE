import json
from datetime import date

today = date.today()
full_today = today.strftime("%B %d, %Y")


# class Blog:
#     def __init__(self, **kw):
#         self.date = kw.get('date', f'{full_today}')
#         self.author = kw.get('author', 'n/a')
#         self.title = kw.get('title', 'n/a')
#         self.subtitle = kw.get('subtitle', 'n/a')
#         self.img_url = kw.get('img_url', 'n/a')
#         self.body = kw.get('body', 'n/a')
        

#     def set_blog_props():
#         with open('blog-data.json', 'r') as file:
#             blog_posts = json.load(file)
#         for key in blog_posts:
#             props = blog_posts[key]
#             yield Blog(**props)

# may need to use the following to be able to submit from form instead of a json file
# class BlogPost(post):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)

# BlogPost(
#     title=form.title.data,
#     subtitle=form.subtitle.data,
#     body=form.body.data,
#     img_url=form.img_url.data,
#     author=form.author.data,
#     date=date.today().strftime("%B %d, %Y")
# )
