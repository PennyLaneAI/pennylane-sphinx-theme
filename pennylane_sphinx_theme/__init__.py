"""
This module registers the PennyLane Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""

from pathlib import Path

from xanadu_sphinx_theme import templates_dir

from ._version import __version__
from .footer import FOOTER
from .navbar import NAVBAR_LEFT, NAVBAR_RIGHT


def setup(app):
    """See https://www.sphinx-doc.org/en/master/extdev/appapi.html."""
    cwd = Path(__file__).resolve().parent
    app.add_html_theme("pennylane", str(cwd))

    # set default left navbar links
    if "navbar_left_links" not in app.config["html_theme_options"]:

        active_link = app.config["html_theme_options"].get("navbar_active_link", None)

        if active_link is not None:
            NAVBAR_LEFT[active_link]["active"] = True

        app.config["html_theme_options"]["navbar_left_links"] = NAVBAR_LEFT

    # set default right navbar links
    if "navbar_right_links" not in app.config["html_theme_options"]:
        app.config["html_theme_options"]["navbar_right_links"] = NAVBAR_RIGHT

    # set default footer sections
    for section in ["about", "policies", "links", "social_icons", "taglines"]:
        if f"footer_{section}" not in app.config["html_theme_options"]:
            app.config["html_theme_options"][f"footer_{section}"] = FOOTER[f"footer_{section}"]
