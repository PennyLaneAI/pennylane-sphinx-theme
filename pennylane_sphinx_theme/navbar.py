"""
This module contains the common PennyLane navigation bar data.

Icon values are Boxicons CSS classes (e.g. "bx-book-open", "bxs-flask"), since
the theme renders icons with the Boxicons web font. Pick any icon from
https://boxicons.com and use its class name directly.
"""

WHY_PENNYLANE = {
    "name": "Why PennyLane",
    "linkSections": [
        {
            "columns": 1,
            "sections": [
                {
                    "header": "About PennyLane",
                    "items": [
                        {
                            "name": "Features",
                            "href": "https://pennylane.ai/features",
                            "description": "Discover easy-to-use PennyLane features to empower your work.",
                        },
                        {
                            "name": "Performance",
                            "href": "https://pennylane.ai/performance",
                            "description": "Scale up your workflows on GPUs and supercomputers to accelerate simulations.",
                        },
                        {
                            "name": "Hardware and simulators",
                            "href": "https://pennylane.ai/devices",
                            "description": "Explore PennyLane's quantum device ecosystem with 40+ integrated options.",
                        },
                    ],
                },
            ],
        },
        {
            "columns": 1,
            "sections": [
                {
                    "header": "Use Cases & Applications",
                    "items": [
                        {
                            "name": "Research",
                            "href": "https://pennylane.ai/research",
                            "description": "Accelerate your quantum computing research breakthroughs with PennyLane.",
                        },
                        {
                            "name": "Teach",
                            "href": "https://pennylane.ai/education",
                            "description": "Join quantum educators in over 130 universities using PennyLane in the classroom.",
                        },
                        {
                            "name": "Learn",
                            "href": "https://pennylane.ai/learn",
                            "description": "Delve into quantum computing, quantum chemistry, and quantum machine learning.",
                        },
                    ],
                },
            ],
        },
    ],
    "cardSections": [
        {
            "header": "Featured",
            "type": "featured",
            "cards": [
                {
                    "variant": "white",
                    "title": "Research",
                    "description": "Use **the world's largest quantum demo library** to publish breakthrough research.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/why-pennylane-research-small.png",
                    "imageSize": "small",
                    "button": {
                        "text": "Research with PennyLane",
                        "variant": "primary",
                    },
                    "href": "https://pennylane.ai/research",
                },
                {
                    "variant": "white",
                    "title": "Teach",
                    "description": "Elevate your curriculum using **industry-standard tools** that build job-ready skills.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/why-pennylane-teach-small.png",
                    "imageSize": "small",
                    "button": {
                        "text": "Explore educator resources",
                        "variant": "primary",
                    },
                    "href": "https://pennylane.ai/education",
                },
            ],
        },
    ],
}

DOCUMENTATION = {
    "name": "Documentation",
    "linkSections": [
        {
            "columns": 1,
            "sections": [
                {
                    "header": "Documentation",
                    "items": [
                        {
                            "name": "Install",
                            "href": "https://pennylane.ai/install",
                        },
                        {
                            "name": "PennyLane documentation",
                            "href": "https://docs.pennylane.ai/en/stable/",
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
                            "href": "https://pennylane.ai/search/?contentType=DEMO&categories=how-to&sort=publication_date",
                        },
                        {
                            "name": "API",
                            "href": "https://docs.pennylane.ai/en/stable/code/qp.html",
                        },
                        {
                            "name": "GitHub",
                            "href": "https://github.com/PennyLaneAI/pennylane",
                        },
                    ],
                },
            ],
        },
    ],
    "cardSections": [
        {
            "header": "Getting Started",
            "type": "featured",
            "cards": [
                {
                    "variant": "white",
                    "title": "PennyLane Fundamentals",
                    "description": "Begin with a crash course on the basics of PennyLane for quantum practitioners.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/documentation-fundamentals-wide.png",
                    "imageSize": "full",
                    "button": {
                        "text": "Get started",
                        "variant": "secondary",
                    },
                    "href": "https://pennylane.ai/codebook/pennylane-fundamentals",
                },
                {
                    "variant": "white",
                    "title": "Documentation",
                    "description": "Explore our quantum software API references and development guides.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/documentation-documentation-wide.png",
                    "imageSize": "full",
                    "button": {
                        "text": "View documentation",
                        "variant": "primary",
                    },
                    "href": "https://docs.pennylane.ai/en/stable/",
                },
            ],
        },
        {
            "header": "Latest Release",
            "type": "release",
            "cards": {
                "limit": 1,
                "variant": "primary-blue",
                "button": {
                    "text": "New in this release",
                    "variant": "secondary",
                    "icon": "bx-right-arrow-alt",
                },
            },
        },
    ],
}

RESOURCES = {
    "name": "Resources",
    "linkSections": [
        {
            "columns": 2,
            "sections": [
                {
                    "header": "Quantum Computing Resources",
                    "items": [
                        {
                            "name": "Codebook",
                            "href": "https://pennylane.ai/codebook",
                            "icon": "bx-book-open",
                            "description": "Learn quantum computing with PennyLane.",
                        },
                        {
                            "name": "Coding challenges",
                            "href": "https://pennylane.ai/challenges",
                            "icon": "bx-trophy",
                            "description": "Test your skills with quantum coding challenges and earn badges.",
                        },
                        {
                            "name": "Videos",
                            "href": "https://pennylane.ai/videos",
                            "icon": "bx-video",
                            "description": "Sit back and explore our curated selection of expert videos.",
                        },
                        {
                            "name": "Demos library",
                            "href": "https://pennylane.ai/demonstrations",
                            "icon": "bxs-flask",
                            "description": "Explore the quantum landscape with our research-level demos written by experts.",
                        },
                        {
                            "name": "Compilation hub",
                            "href": "https://pennylane.ai/compilation",
                            "icon": "bx-code-block",
                            "description": "Find explanations and implementations of important quantum compilation techniques.",
                        },
                        {
                            "name": "Quantum datasets",
                            "href": "https://pennylane.ai/datasets",
                            "icon": "bx-data",
                            "description": "Speed up research with quantum datasets tailored for use with PennyLane.",
                        },
                    ],
                    "cta": {"text": "Browse all", "href": "https://pennylane.ai/search"},
                },
            ],
        },
    ],
    "cardSections": [
        {
            "header": "Latest Quantum Computing Demos",
            "type": "content",
            "cta": {
                "text": "Explore demos library",
                "href": "https://pennylane.ai/demonstrations",
            },
            "cards": {
                "limit": 2,
                "filters": {
                    "contentType": "DEMO",
                    "sort": "publication_date",
                    "categories": ["quantum computing"],
                },
                "fallbackImageSrc": "https://assets.cloud.pennylane.ai/navbar/pennylane-generic-demo-thumbnail.png",
            },
        },
    ],
}

TOPIC_GUIDES = {
    "name": "Topic Guides",
    "linkSections": [
        {
            "columns": 2,
            "sections": [
                {
                    "header": "Quantum Computing Topic Guides from PennyLane",
                    "items": [
                        {
                            "name": "Fault-tolerant quantum computing",
                            "href": "https://pennylane.ai/topics/fault-tolerant-quantum-computing",
                            "description": "Master the latest advancements in error correcting codes and FTQC.",
                        },
                        {
                            "name": "Hamiltonian simulation",
                            "href": "https://pennylane.ai/topics/hamiltonian-simulation",
                            "description": "Discover Hamiltonian simulation algorithms–from basic to advanced techniques.",
                        },
                        {
                            "name": "Quantum compilation",
                            "href": "https://pennylane.ai/topics/quantum-compilation",
                            "pill": {
                                "text": "New",
                                "variant": "in-progress",
                                # TODO: Update start and expiry dates
                                "startDate": "2026-05-01",
                                "expiryDate": "2026-07-01",
                            },
                            "description": "Explore the definitive PennyLane Guide to quantum compilation techniques.",
                        },
                        {
                            "name": "Quantum gradients",
                            "href": "https://pennylane.ai/topics/quantum-gradients",
                            "description": "Access a curated guide of the different quantum gradient methods.",
                        },
                        {
                            "name": "Quantum hardware",
                            "href": "https://pennylane.ai/topics/quantum-hardware",
                            "description": "View how the modalities stack up in the global race to build a scalable quantum computer.",
                        },
                        {
                            "name": "Quantum machine learning",
                            "href": "https://pennylane.ai/topics/quantum-machine-learning",
                            "description": "Learn the different flavours of quantum machine learning in this curated guide.",
                        },
                    ],
                },
            ],
        },
    ],
    "cardSections": [
        {
            "header": "Featured PennyLane Topic Guides",
            "type": "featured",
            "cards": [
                {
                    "variant": "white",
                    "title": "Fault-tolerant quantum computing",
                    "description": "Master the latest advancements in error correcting codes and FTQC.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/topic-guides-ftqc-wide.png",
                    "imageSize": "full",
                    "button": {
                        "text": "Demystify FTQC",
                        "variant": "secondary",
                    },
                    "href": "https://pennylane.ai/codebook/pennylane-fundamentals",
                },
                {
                    "variant": "white",
                    "title": "Quantum compilation",
                    "description": "Explore the definitive PennyLane Guide to quantum compilation techniques.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/topic-guides-compilation-wide.png",
                    "imageSize": "full",
                    "button": {
                        "text": "Explore quantum compilation",
                        "variant": "secondary",
                    },
                    "href": "https://docs.pennylane.ai/en/stable/",
                    "pill": {
                        "text": "New",
                        "variant": "in-progress",
                        # TODO: Add start and expiry dates
                    },
                },
            ],
        },
    ],
}

COMMUNITY_SUPPORT = {
    "name": "Community & Support",
    "pill": {
        "text": "New",
        "variant": "info",
        # TODO: Add start and expiry dates
    },
    "linkSections": [
        {
            "columns": 1,
            "sections": [
                {
                    "header": "Community & Support",
                    "items": [
                        {
                            "name": "PennyLane blog",
                            "href": "https://pennylane.ai/blog?page=1",
                        },
                        {
                            "name": "FAQs",
                            "href": "https://pennylane.ai/faq",
                        },
                        {
                            "name": "Discussion forum",
                            "href": "https://discuss.pennylane.ai",
                        },
                        {
                            "name": "Submit a demo",
                            "href": "https://pennylane.ai/demos_submission",
                        },
                        {
                            "name": "Get involved",
                            "href": "https://pennylane.ai/get-involved",
                        },
                    ],
                },
                {
                    "header": "From Xanadu",
                    "items": [
                        {
                            "name": "Xanadu blog",
                            "href": "https://xanadu.ai/blog",
                        },
                        {
                            "name": "Xanadu press and news",
                            "href": "https://xanadu.ai/press",
                        },
                    ],
                },
            ],
        },
    ],
    "cardSections": [
        {
            "header": "Latest Blog Post",
            "type": "content",
            "cta": {"text": "View all", "href": "https://pennylane.ai/blog?page=1"},
            "cards": {
                "limit": 1,
                "filters": {
                    "contentType": "BLOG",
                    "sort": "publication_date",
                },
                "fallbackImageSrc": "https://assets.cloud.pennylane.ai/navbar/pennylane-generic-blog-thumbnail.png",
            },
        },
        {
            "header": "Help & Support",
            "type": "featured",
            "cards": [
                {
                    "variant": "white",
                    "title": "Join the PennyLane discussion forum",
                    "description": "Get expert help and connect with the global PennyLane community.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/community-forum-small.png",
                    "imageSize": "small",
                    "button": {
                        "text": "Go to forum",
                        "variant": "secondary",
                        "icon": "bx-link-external",
                    },
                    "href": "https://discuss.pennylane.ai",
                },
            ],
        },
        {
            "header": "PennyLane newsletter",
            "type": "featured",
            "cards": [
                {
                    "variant": "primary-blue",
                    "title": "PennyLane newsletter",
                    "description": "Want to get the latest quantum updates delivered to your inbox? Join the list.",
                    "imageSrc": "https://assets.cloud.pennylane.ai/navbar/newsletter-small.png",
                    "imageSize": "small",
                    "button": {
                        "text": "Subscribe now",
                        "variant": "secondary",
                        "icon": "bx-right-arrow-alt",
                    },
                    "href": "https://bit.ly/434uPcQ",
                    "pill": {
                        "text": "New",
                        "variant": "info",
                        # TODO: Add start and expiry dates
                    },
                },
            ],
        },
    ],
}


NAVBAR_LEFT = [
    WHY_PENNYLANE,
    DOCUMENTATION,
    RESOURCES,
    TOPIC_GUIDES,
    COMMUNITY_SUPPORT,
]


NAVBAR_RIGHT = [
    {
        "name": "Install",
        "href": "https://pennylane.ai/install",
    },
]
