#!/usr/bin/env python3
"""Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Dict, Union


class Config:
    """Flask babel configs"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    _id = request.args.get('login_as', '').strip()
    if not _id or not users.get(int(_id)):
        return None
    return users.get(int(_id))


@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@babel.localeselector
def get_locale() -> str:
    """determines the best match for selected languages"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """renders a template"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
