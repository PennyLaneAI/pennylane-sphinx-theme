"""
This module contains the common PennyLane coach mark data.

Coach marks are dismissible toast prompts shown near the top of the page,
used to promote time-boxed campaigns (e.g. surveys). Copy here is kept in
sync by hand with the portal's shared-content package; see
https://github.com/XanaduAI/pennylane.ai-react/blob/master/packages/shared-content/README.md#coach-marks
for the source of truth and the editing workflow. When updating the toast
copy for a campaign, update both places together.
"""

COACH_MARK_TOAST = {
    "enabled": True,
    "title": "Have your say!",
    "body": [
        "Enjoying PennyLane? Take the ",
        {
            "type": "link",
            "text": "2026 Unitary Foundation Quantum Open Source Software Survey",
            "href": "https://www.surveymonkey.com/r/QOSSSurvey26",
            "gaLabel": "qoss_survey",
            "isExternal": True,
        },
        " now.",
    ],
    "icon": "megaphone",
    "delayMs": 3000,
    # October 30, 2026 at 9:00 AM ET
    "expiryDateTime": "2026-10-30T13:00:00Z",
}
