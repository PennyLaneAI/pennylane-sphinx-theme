"""
This module contains the common PennyLane footer data.
"""

import textwrap

from .urls import PENNYLANE_WEBSITE, pl_url

PENNYLANE_LOGO = "https://assets.cloud.pennylane.ai/pennylane_website/generic/pennylane-logo.png"
XANADU_LOGO = "https://assets.cloud.pennylane.ai/pennylane_website/generic/xanadu-logo.png"


FOOTER = {
    "footer_newsletter": {
        "title": "Never miss a milestone",
        "description": "Get the latest quantum updates delivered to your inbox.",
        "href": "https://bit.ly/4u6rEfT",
        "cta": "Join the list",
    },
    "footer_about": {
        "title": "PennyLane",
        "icon": PENNYLANE_LOGO,
        "href": PENNYLANE_WEBSITE,
        "description": textwrap.dedent(
            """\
            PennyLane is an open-source quantum software platform for quantum computing,
            quantum machine learning, and quantum chemistry. Create meaningful quantum
            algorithms, from inspiration to implementation.
            """
        ).strip(),
        "created_by": 'Created with ❤️ by <a href="https://xanadu.ai/">Xanadu</a>.',
    },
    "footer_xanadu": {
        "title": "Xanadu",
        "icon": XANADU_LOGO,
        "href": "https://xanadu.ai",
    },
    "footer_copyright": {
        "tensorflow_notice": (
            "TensorFlow, the TensorFlow logo and any related marks are " "trademarks of Google Inc."
        ),
    },
    "footer_policies": [
        {
            "text": "Privacy policy",
            "href": pl_url("/privacy"),
        },
        {
            "text": "Terms of service",
            "href": pl_url("/terms"),
        },
        {
            "text": "Cookies policy",
            "href": pl_url("/cookies"),
        },
        {
            "text": "Code of conduct",
            "href": pl_url("/conduct"),
        },
    ],
    "footer_links": [
        {
            "title": "Research",
            "links": [
                {
                    "name": "Research",
                    "href": pl_url("/research"),
                },
                {
                    "name": "Performance",
                    "href": pl_url("/performance"),
                },
                {
                    "name": "Hardware and simulators",
                    "href": pl_url("/devices"),
                },
                {
                    "name": "Demos library",
                    "href": pl_url("/demonstrations"),
                },
                {
                    "name": "Compilation hub",
                    "href": pl_url("/compilation"),
                },
                {
                    "name": "Quantum datasets",
                    "href": pl_url("/datasets"),
                },
            ],
        },
        {
            "title": "Education",
            "links": [
                {
                    "name": "Teach",
                    "href": pl_url("/education"),
                },
                {
                    "name": "Learn",
                    "href": pl_url("/learn"),
                },
                {
                    "name": "Codebook",
                    "href": pl_url("/codebook"),
                },
                {
                    "name": "Coding challenges",
                    "href": pl_url("/challenges"),
                },
                {
                    "name": "Videos",
                    "href": pl_url("/videos"),
                },
                {
                    "name": "Glossary",
                    "href": pl_url("/glossary"),
                },
            ],
        },
        {
            "title": "Software",
            "links": [
                {
                    "name": "Install",
                    "href": pl_url("/install"),
                },
                {
                    "name": "Features",
                    "href": pl_url("/features"),
                },
                {
                    "name": "PennyLane documentation",
                    "href": "https://docs.pennylane.ai",
                },
                {
                    "name": "Catalyst documentation",
                    "href": "https://docs.pennylane.ai/projects/catalyst/en/stable/",
                },
                {
                    "name": "Development guide",
                    "href": "https://docs.pennylane.ai/en/stable/development/guide.html",
                },
                {
                    "name": "How-to guides",
                    "href": pl_url("/search/?contentType=DEMO&categories=how-to&sort=publication_date"),
                },
                {
                    "name": "API",
                    "href": "https://docs.pennylane.ai/en/stable/code/qp.html",
                },
                {
                    "name": "GitHub",
                    "href": "https://github.com/PennyLaneAI/pennylane",
                    "external": True,
                },
            ],
        },
    ],
    "footer_social_icons": [
        {
            "name": "linkedin",
            "icon": "bxl bx-linkedin",
            "href": "https://www.linkedin.com/company/pennylaneai/",
        },
        {
            "name": "github",
            "icon": "bxl bx-github",
            "href": "https://github.com/PennyLaneAI/pennylane",
        },
        {
            "name": "youtube",
            "icon": "bxl bx-youtube",
            "href": "https://www.youtube.com/@pennylaneai/",
        },
        {
            "name": "twitter",
            "icon": "bxl bx-twitter-x",
            "href": "https://twitter.com/PennyLaneAI",
        },
        {
            "name": "discord",
            "icon": "bxl bx-discord",
            "href": "https://discord.com/invite/gnySM3nrN3",
        },
        {
            "name": "slack",
            "icon": "bxl bx-slack",
            "href": "https://join.slack.com/t/xanadu-quantum/shared_invite/zt-1i8v8v49d-S76QxXm3OKCm9g0bvWvDpg",
        },
        {
            "name": "discourse",
            "icon": "bxl bx-discourse",
            "href": "https://discuss.pennylane.ai",
        },
    ],
    "footer_taglines": [],
}
