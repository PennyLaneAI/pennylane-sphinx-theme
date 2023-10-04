PennyLane Sphinx Theme
######################

.. header-start-inclusion-marker-do-not-remove

The **PennyLane Sphinx Theme** is a Sphinx theme used for open-source PennyLane
software projects hosted on https://pennylane.ai. It extends the Xanadu Sphinx Theme
with PennyLane-specific default settings and configurations.

To update the PennyLane navigation bar (navbar) and footer, please see the files
``pennylane_sphinx_theme/footer.py`` and ``pennylane_sphinx_theme/navbar.py``.

For more details, please see the
`Xanadu Sphinx Theme documentation <https://xanadu-sphinx-theme.readthedocs.io/en/latest/>`__.

.. header-end-inclusion-marker-do-not-remove


Installation
============

.. installation-start-inclusion-marker-do-not-remove

The PennyLane Sphinx Theme requires Python 3.7 or later. The latest version of the
theme can be installed directly using ``pip``:

.. code-block:: bash

    pip install pennylane-sphinx-theme


.. installation-end-inclusion-marker-do-not-remove


Getting Started
===============

.. getting-started-start-inclusion-marker-do-not-remove

Once installed, simply add or modify the following variables of your Sphinx
``conf.py`` configuration file to start using the PennyLane Sphinx Theme:

.. code-block:: python

    from pennylane_sphinx_theme import templates_dir
    templates_path = [templates_dir()]

    html_theme = "pennylane"

    html_theme_options = {
        "navbar_name": "Example Project",
        "navbar_active_link": 3
    }

.. getting-started-end-inclusion-marker-do-not-remove

Configuration
=============

.. configuration-start-inclusion-marker-do-not-remove

The PennyLane Sphinx Theme supports the same configration options as
the Xanadu Sphinx Theme. For more details, please see the
`Xanadu Sphinx Theme documentation <https://xanadu-sphinx-theme.readthedocs.io/en/latest/>`__.

.. configuration-end-inclusion-marker-do-not-remove

Directives
==========

.. directives-start-inclusion-marker-do-not-remove

The PennyLane Sphinx Theme provides various directives.

For more details, please see the
`Xanadu Sphinx Theme documentation <https://xanadu-sphinx-theme.readthedocs.io/en/latest/>`__.


.. directives-end-inclusion-marker-do-not-remove

Support
=======

.. support-start-inclusion-marker-do-not-remove

- **Source Code:** https://github.com/XanaduAI/pennylane-sphinx-theme
- **Issue Tracker:** https://github.com/XanaduAI/pennylane-sphinx-theme/issues

If you are having issues, please let us know by posting the issue on our Github
issue tracker.

.. support-end-inclusion-marker-do-not-remove

License
=======

.. license-start-inclusion-marker-do-not-remove

The PennyLane Sphinx Theme is **free** and **open source**, released under the
`Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_.

.. license-end-inclusion-marker-do-not-remove
