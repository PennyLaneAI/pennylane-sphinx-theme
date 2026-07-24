"""
This module registers the PennyLane Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""

from pathlib import Path

from xanadu_sphinx_theme import templates_dir

from ._version import __version__
from .coach_marks import COACH_MARK_TOAST
from .footer import FOOTER
from .navbar import NAVBAR_LEFT, NAVBAR_RIGHT


def _set_theme_default(app, key, value):
    """Set a theme option when it is missing or empty in theme.conf."""
    if not app.config["html_theme_options"].get(key):
        app.config["html_theme_options"][key] = value


def _set_theme_default_unset(app, key, value):
    """Set a theme option only when it is entirely absent from
    ``html_theme_options``, unlike ``_set_theme_default``. This is needed for
    options (e.g. booleans) where an explicit falsy value, such as
    ``False``, is a meaningful override that must not be clobbered.
    """
    if key not in app.config["html_theme_options"]:
        app.config["html_theme_options"][key] = value


def setup(app):
    """See https://www.sphinx-doc.org/en/master/extdev/appapi.html."""
    cwd = Path(__file__).resolve().parent
    app.add_html_theme("pennylane", str(cwd))

    _set_theme_default(app, "navbar_left_links", NAVBAR_LEFT)
    _set_theme_default(app, "navbar_right_links", NAVBAR_RIGHT)

    # Coach marks default to enabled, with PennyLane's launch copy, so that
    # every site using this theme picks them up automatically. Sites can
    # still opt out by explicitly setting "coach_mark_enabled": False.
    _set_theme_default_unset(app, "coach_mark_enabled", True)
    _set_theme_default(app, "coach_mark_toast", COACH_MARK_TOAST)

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
