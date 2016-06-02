#!flask/bin/python
from app import app
from flask import Flask, render_template
app.run(debug = True, host="0.0.0.0", port=8080)
