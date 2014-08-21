#-*- coding:utf-8 -*-
from application import app
from flask import redirect, request, url_for, session, render_template
from application.models.user_manager import *
from application.models.post_manager import *


@app.route('/delete_post/<int:post_id>')
def delete_post(post_id) :
	post = get_post(post_id)
	if session['user_id'] == post.user_id :
		post_delete(post_id)
		return redirect(url_for('wall', wall_id=session['wall_id']))
	else :
		return "You can't delete it"


# 하나로 합치자
@app.route('/delete_comment/<int:comment_id>')
def delete_comment(comment_id):
	comment = get_comment(comment_id)
	if session['user_id'] == comment.user_id :
		comment_delete(comment_id)
	return redirect(url_for('read', wall_id=session['wall_id'], id=session['post_id']))

# 포스트만 받게! get byebye : OK
@app.route('/modify_post/<int:post_id>', methods=['POST'])
def modify_post(post_id):
	post = get_post(post_id)
	if session['user_id'] == post.user_id:
		post_modify(post_id, request.form['body'])
		return redirect(url_for('wall', wall_id=session['wall_id']))
	return render_template('modify.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404