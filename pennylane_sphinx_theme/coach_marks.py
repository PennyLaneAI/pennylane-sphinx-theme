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
# the real QOSS survey link, and replace "Date XX, 2026" in `body` with
# the actual survey end date.
COACH_MARK_TOAST = {
    "enabled": True,
    "title": "The QOSS 2026 Survey",
    "body": [
        "Take the Unitary Foundation's ",
        {
            "type": "link",
            "text": "(QOSS) Survey",
            # TODO: Update to the real QOSS survey link.
            "href": "https://unitary.foundation",
            "gaLabel": "toast_qoss_survey",
            "isExternal": True,
        },
        " for a chance to win prizes. Live until Date XX, 2026!",
    ],
    "icon": "megaphone",
    "delayMs": 3000,
}
# pylint: enable=fixme
