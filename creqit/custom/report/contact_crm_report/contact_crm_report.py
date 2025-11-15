# Copyright (c) 2024, creqit Technologies and contributors
# For license information, please see license.txt

import creqit
from creqit import _

def execute(filters=None):
    if not filters:
        filters = {}
    
    columns = get_columns()
    data = get_data()
    
    return columns, data

def get_columns():
    return [
        {
            "label": _("Contact Name"),
            "fieldname": "name_surname",
            "fieldtype": "Link",
            "options": "Contact_CRM",
            "width": 200
        },
        {
            "label": _("Title"),
            "fieldname": "title",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Account"),
            "fieldname": "linkaccount",
            "fieldtype": "Link",
            "options": "Account",
            "width": 200
        },
        {
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Last Activity"),
            "fieldname": "lastactivity",
            "fieldtype": "Datetime",
            "width": 150
        },
        {
            "label": _("Email"),
            "fieldname": "email_contact",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("Phone"),
            "fieldname": "phone_contact",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Mobile Phone"),
            "fieldname": "mobilephone",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Fax"),
            "fieldname": "fax",
            "fieldtype": "Data",
            "width": 120
        }
    ]

def get_data():
    return creqit.db.sql("""
        SELECT 
            c.name_surname,
            c.title,
            c.linkaccount,
            c.department,
            c.lastactivity,
            c.email AS email_contact,
            c.phone AS phone_contact,
            c.mobilephone,
            c.fax 
        FROM `tabContact_CRM` c 
        GROUP BY
            c.name_surname,
            c.title,
            c.linkaccount,
            c.department,
            c.lastactivity,
            c.email,
            c.phone,
            c.mobilephone,
            c.fax
        ORDER BY c.creation DESC
    """, as_dict=1) 