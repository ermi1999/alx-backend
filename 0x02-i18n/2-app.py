#!/usr/bin/env python3
"""Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Flask babel configs"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determines the best match for selected languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """renders a template"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
