from app import app, db, models
from flask import Flask, render_template, flash, redirect, url_for, request
from .forms import SubmitForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    print(request.method)
    if request.method == 'GET':
        return render_template('submit.html',title='Submit your protocol!', form=SubmitForm())
    if request.method == 'POST':
        p = models.Protocol(title=request.form['title'],protocol_description=request.form['bodytext'])
        db.session.add(p)
        db.session.commit()
        return redirect("/protocol/" + str(p.id))


@app.route('/protocol/<id>')
def protocol(id):
    prot = models.Protocol.query.get(int(id))
    if prot == None:
        flash('Protocol %s not found.' % id)
        return redirect(url_for('index'))
    return render_template('protocol.html',
                           protocol=prot)

@app.route('/directory/<n>')
def directory(n):
    perPage = 10
    n = int(n)
    prots = [models.Protocol.query.get(i) for i in xrange(n * perPage,n * perPage + perPage)]
    prots = [p for p in prots if (p != None)]
    return render_template('directory.html',protocols=prots)

@app.route('/directory')
def firstPageDirectory():
    return directory(0)


def aftersubmit(resp):
    prot = Protocol(title=resp.title, protocol_description=resp.protocol_description)
    db.session.add(prot)
    db.session.commit()
    return firstPageDirectory()
