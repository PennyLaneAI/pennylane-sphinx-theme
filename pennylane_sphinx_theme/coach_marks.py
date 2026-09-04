"""
This module contains the common PennyLane coach mark data.

Coach marks are dismissible toast prompts shown near the top of the page,
used to promote time-boxed campaigns (e.g. surveys). Copy here is kept in
sync by hand with the portal's shared-content package; see
https://github.com/XanaduAI/pennylane.ai-react/blob/master/packages/shared-content/README.md#coach-marks
for the source of truth and the editing workflow. When updating the toast
copy for a campaign, update both places together.
"""

# pylint: disable=fixme
# TODO: before launch, replace the placeholder survey `href` below with
# the real QOSS survey link.
COACH_MARK_TOAST = {
    "enabled": True,
    "title": "Have your say!",
    "body": [
        "Enjoying PennyLane? Take the ",
        {
            "type": "link",
            "text": "2026 Unitary Foundation Quantum Open Source Software Survey",
            # TODO: Update to the real QOSS survey link.
            "href": "https://unitary.foundation",
            "gaLabel": "toast_qoss_survey",
            "isExternal": True,
        },
        " now.",
    ],
    "icon": "megaphone",
    "delayMs": 3000,
}
# pylint: enable=fixme
