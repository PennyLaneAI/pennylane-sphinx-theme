"""
This module registers the PennyLane Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""

from pathlib import Path

from xanadu_sphinx_theme import templates_dir

from ._version import __version__
from .footer import FOOTER
from .navbar import NAVBAR_LEFT, NAVBAR_RIGHT


def _set_theme_default(app, key, value):
    """Set a theme option when it is missing or empty in theme.conf."""
    if not app.config["html_theme_options"].get(key):
        app.config["html_theme_options"][key] = value


def setup(app):
    """See https://www.sphinx-doc.org/en/master/extdev/appapi.html."""
    cwd = Path(__file__).resolve().parent
    app.add_html_theme("pennylane", str(cwd))

    _set_theme_default(app, "navbar_left_links", NAVBAR_LEFT)
    _set_theme_default(app, "navbar_right_links", NAVBAR_RIGHT)

    for section in [
        "about",
        "policies",
        "links",
        "social_icons",
        "newsletter",
        "xanadu",
        "copyright",
    ]:
        _set_theme_default(app, f"footer_{section}", FOOTER.get(f"footer_{section}"))
