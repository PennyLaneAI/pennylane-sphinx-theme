"""
Shared URL helpers and constants for the PennyLane Sphinx theme content.
"""

PENNYLANE_WEBSITE = "https://pennylane.ai"


def pl_url(path):
    """Return an absolute pennylane.ai URL for website paths."""
    if path.startswith("http"):
        return path
    return f"{PENNYLANE_WEBSITE}{path}"
