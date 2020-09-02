# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "student_system"
app_title = "Student Management System"
app_publisher = "Sherif A"
app_description = "App for managing student Information"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "aabdulraheemsherif@gmail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/student_system/css/student_system.css"
# app_include_js = "/assets/student_system/js/student_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/student_system/css/student_system.css"
# web_include_js = "/assets/student_system/js/student_system.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "student_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "student_system.install.before_install"
# after_install = "student_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "student_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"student_system.tasks.all"
# 	],
# 	"daily": [
# 		"student_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"student_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"student_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"student_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "student_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "student_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "student_system.task.get_dashboard_data"
# }

