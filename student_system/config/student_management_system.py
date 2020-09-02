from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
            {
                "label":_("Library"),
                "icon":"octicon octicon-briefcase",
                "items":[
                    {
                        "type":"doctype",
                        "name":"Article",
                        "label":_("Article"),
                        "description":_("Articles which members issue are rturn."),
                    },
                    {
                        "type":"doctype",
                        "name":"Library Member",
                        "label":_("Library Member"),
                        "description":_("People who have enrolled for membership in the Library"),
                    },
                    {
                        "type":"doctype",
                        "name":"Library Membership",
                        "label":_("Library Membership"),
                        "description":_("People who have taken membership for the library"),
                    },
                    {
                        "type":"doctype",
                        "name":"Library Transaction",
                        "label":_(""),
                        "description":_("Issuing an article or returning an article are the transaction taking place."),
                    }
                ]
            }
        ]
