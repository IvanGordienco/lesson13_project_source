from flask import Flask, request, render_template, send_from_directory, abort
from functions import read_json, get_tags, get_posts

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', tags=get_tags(read_json(POST_PATH)))


@app.route("/tag")
def page_tag():
    tag = request.args.get('tag')
    if not tag:
        abort(400)
    data = read_json(POST_PATH)
    posts = get_posts(data, tag)
    return render_template('post_by_tag.html', tag=tag, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
