# coding: utf-8
from werkzeug.contrib.fixers import ProxyFix
from flask import redirect
from zerqu import create_app
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/topic/<int:tid>')
def redirect_topic(tid):
    return redirect('/t/%d' % tid, code=301)


@app.route('/node/')
def redirect_node_list():
    return redirect('/c/', code=301)


@app.route('/node/<slug>')
def redirect_node(slug):
    return redirect('/c/%s' % slug, code=301)


@app.route('/user/<name>')
@app.route('/user/<name>/topics')
def redirect_user(name):
    return redirect('/u/%s' % name, code=301)
