"""
This module contains the common PennyLane navigation bar data.
"""

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
        "href": "https://docs.pennylane.ai",
    },
    {
        "name": "Blog",
        "href": "https://pennylane.ai/blog/",
    },
]


NAVBAR_RIGHT = [
    {
        "name": "<img src='data:image/png;base64,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' width='18px'/> QHack",
        "href": "https://qhack.ai",
        "icon": "",
    },
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
