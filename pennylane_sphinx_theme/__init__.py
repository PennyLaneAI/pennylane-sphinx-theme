"""
This module registers the Xanadu Sphinx Theme. For more information, see
https://www.sphinx-doc.org/en/master/development/theming.html
"""
from pathlib import Path

from ._version import __version__


def setup(app):
    """See https://www.sphinx-doc.org/en/master/extdev/appapi.html."""
    cwd = Path(__file__).resolve().parent
    app.add_html_theme("pennylane", str(cwd))

    # set default left navbar links
    if "navbar_left_links" not in app.config["html_theme_options"]:
        app.config["html_theme_options"]["navbar_left_links"] = NAVBAR_LEFT

    # set default right navbar links
    if "navbar_right_links" not in app.config["html_theme_options"]:
        app.config["html_theme_options"]["navbar_right_links"] = NAVBAR_RIGHT

    # set default footer sections
    for section in ["about", "links", "socials", "tagline"]:
        if f"footer_{section}" not in app.config["html_theme_options"]:
            app.config["html_theme_options"][f"footer_{section}"] = FOOTER[f"footer_{section}"]


NAVBAR_LEFT = [
    {
        "name": "Quantum machine learning",
        "href": "https://pennylane.ai/qml/",
    },
    {
        "name": "Demos",
        "href": "https://pennylane.ai/qml/demonstrations.html",
    },
    {
        "name": "Install",
        "href": "https://pennylane.ai/install.html",
    },
    {
        "name": "Plugins",
        "href": "https://pennylane.ai/plugins.html",
    },
    {
        "name": "Documentation",
        "href": "index.html",
        "active": True,
    },
    {
        "name": "Blog",
        "href": "https://pennylane.ai/blog/",
    },
]


NAVBAR_RIGHT = [
    {
        "name": "FAQ",
        "href": "https://pennylane.ai/faq.html",
        "icon": "fas fa-question",
    },
    {
        "name": "Support",
        "href": "https://discuss.pennylane.ai/",
        "icon": "fab fa-discourse",
    },
    {
        "name": "GitHub",
        "href": "https://github.com/PennyLaneAI/pennylane",
        "icon": "fab fa-github",
    },
]


FOOTER = {
    "footer_about": {
        "title": "Xanadu",
        "description": """\
        Located in the heart of downtown Toronto, we've brought together
        exceptional minds from around the world to build quantum computers
        that are useful and available to people everywhere.
        """,
    },
    "footer_links": [
        {
            "title": "PennyLane",
            "links": [
                {
                    "name": "Home",
                    "href": "https://pennylane.ai/",
                },
                {
                    "name": "Learn",
                    "href": "https://pennylane.ai/qml",
                },
                {
                    "name": "Demonstrations",
                    "href": "https://pennylane.ai/qml/demonstrations.html",
                },
                {
                    "name": "Documentation",
                    "href": "https://docs.pennylane.ai/",
                },
                {
                    "name": "GitHub",
                    "href": "https://github.com/PennyLaneAI/pennylane",
                },
                {
                    "name": "Twitter",
                    "href": "https://twitter.com/pennylaneai",
                },
                {
                    "name": "Blog",
                    "href": "https://pennylane.ai/blog",
                },
            ],
        },
        {
            "title": "Strawberry Fields",
            "links": [
                {
                    "name": "Home",
                    "href": "https://strawberryfields.ai/",
                },
                {
                    "name": "Photonics",
                    "href": "https://strawberryfields.ai/photonics",
                },
                {
                    "name": "Demonstrations",
                    "href": "https://strawberryfields.ai/photonics/demonstrations.html",
                },
                {
                    "name": "Documentation",
                    "href": "https://strawberryfields.readthedocs.io/",
                },
                {
                    "name": "GitHub",
                    "href": "https://github.com/XanaduAI/strawberryfields",
                },
            ],
        },
        {
            "title": "Xanadu",
            "links": [
                {
                    "name": "Home",
                    "href": "https://xanadu.ai/",
                },
                {"name": "About", "href": "https://xanadu.ai/about/"},
                {
                    "name": "Hardware",
                    "href": "https://xanadu.ai/photonics",
                },
                {"name": "Careers", "href": "https://xanadu.ai/careers/"},
                {"name": "Cloud", "href": "https://cloud.xanadu.ai"},
                {
                    "name": "Forum",
                    "href": "https://discuss.pennylane.ai/",
                },
                {
                    "name": "Blog",
                    "href": "https://xanadu.ai/blog",
                },
            ],
        },
    ],
    "footer_socials": [
        {"icon": "fab fa-twitter", "href": "https://twitter.com/xanaduai"},
        {"icon": "fab fa-github", "href": "https://github.com/XanaduAI"},
        {"icon": "fab fa-linkedin-in", "href": "https://linkedin.com/company/xanaduai/"},
        {"icon": "fab fa-discourse", "href": "https://discuss.pennylane.ai"},
        {
            "icon": "fab fa-slack",
            "href": "https://u.strawberryfields.ai/slack",
        },
        {"icon": "fas fa-rss", "href": "https://xanadu.ai/blog"},
    ],
    "footer_tagline": {
        "text": "Stay updated with our newsletter",
        "href": "https://xanadu.us17.list-manage.com/subscribe?u=725f07a1d1a4337416c3129fd&id=294b062630",
    },
}
