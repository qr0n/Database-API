from flask import Flask, request, render_template  # Imports
from db import db, render
import os
from updates import logging
from auth import MD, auth


app = Flask('app')  # Create our app

password = os.environ["password"]


@app.route('/')
def hello_world():
  try:
    return f"""<meta property=\"og:description\" content=\"active: [{len(render.online())}]\nscripts : [{len(render.scripts())}]>
    Currently online DB's : {render.online()}
    Currently completed scripts : {render.scripts()}
    """
  except Exception:
    return f"""<meta property=\"og:description\" content=\"active: [{len(render.online())}]\nscripts : [{len(render.scripts())}]>
    Currently online DB's : {render.online()}
    Currently completed scripts : {render.scripts()}
    """
    pass
    


@app.route('/api/<_pass>/store', methods=["GET"]
           )  # GET is not secure, you should use POST in production.
def store(_pass):
    if _pass == password:
        db.save(k=request.args.get("key"),
                v=request.args.get("value"),
                f=request.args.get("file"))
        return db.index(k=request.args.get("key"), f=request.args.get("file"))


@app.route('/api/<_pass>/get', methods=["GET"]
           )  # GET is not secure, you should use POST in production.
def get(_pass):
    if _pass == password:
        return db.index(k=request.args.get("key"), f=request.args.get("file"))


@app.route('/api/<_pass>/del', methods=["GET"])
def delete(_pass):
    if _pass == password:
        try:
            db.delete(k=request.args.get("key"), f=request.args.get("file"))
            return "True"
        except KeyError:
            return "False"


@app.route('/api/<_pass>/list')
def _get(_pass):
    if _pass == password:
        return db.show(f=request.args.get("file"))

@app.route('/api/<_pass>/create_db')
def create_db(_pass):
    if _pass == password:
        return db.create_database(fn=request.args.get("file"))

@app.route('/api/<_pass>/delete_db')
def delete_db(_pass):
    if _pass == password:
        return db.delete_database(fn=request.args.get("file"))

@app.route('/packages')
def packager():
  try:
    print("pulling pack.")
    return db.fork(pack=request.args.get("p"), id="Demo")
    
  except Exception as E:
    print("terminating pack.")
    return "#NO"
    
@app.route('/js/<script>')
def scriptjs(script):
  try:
    with open(f"scripts/{script}", "r") as E:
      return E.read()
  except Exception as E:
    return f"""
    console.log('Script caused an internal error: {E}')
    """

@app.route('/auth/<app>')
def _auth(app):
  if auth.check(name=app):
    return "hi"
  else:
    return "bye"

app.run(host='0.0.0.0', port=8080)
