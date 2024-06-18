from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route('/projects/')
# def projects():
#     return "the projects page"
# @app.route('/about')
# def about():
#     return 'the about page'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post{post_id}'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

# @app.route("/")
# def hello_world():
#     return "<p>hello world<p>"
