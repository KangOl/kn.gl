#!/usr/bin/env python
"""
    kn.gl website
    Copyright Christophe Simonis
"""

__all__ = ['app']

from collections import defaultdict
from operator import attrgetter
import os

from flask import Flask, render_template, jsonify, abort

from .services import get_all_services, get_service
from .util import rowify

app = Flask('kngl')

app.config.from_pyfile('config.py')
if 'KNGL_SETTINGS' in os.environ:
    app.config.from_envvar('KNGL_SETTINGS')

app.jinja_env.filters['rowify'] = rowify


@app.route('/')
def index():
    bycat = defaultdict(list)
    for s in get_all_services():
        bycat[s.category].append(s)

    weight = attrgetter('weight')
    cats = sorted(bycat.keys(), key=weight)
    services = [(cat, sorted(bycat[cat], key=weight)) for cat in cats]

    return render_template('index.html', services_by_category=services)

@app.route('/service/<name>.json')
def service(name):
    s = get_service(name)
    if s is None:
        abort(404)
    return jsonify(s.to_dict())
