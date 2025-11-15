# Copyright (c) 2024, creqit Technologies and contributors
# License: MIT. See LICENSE

import creqit
from creqit import _

def create_account_dashboard():
    if not creqit.db.exists("Dashboard", "Account Statistics"):
        dashboard = creqit.new_doc("Dashboard")
        dashboard.dashboard_name = "Account Statistics"
        dashboard.is_default = 1
        
        # Add Leads card
        dashboard.append("cards", {
            "label": "Leads",
            "type": "Number Card",
            "color": "#7cd6fd",
            "document_type": "Lead",
            "filters": '{"account": "{{ filters.account }}"}'
        })
        
        # Add Opportunities card
        dashboard.append("cards", {
            "label": "Opportunities",
            "type": "Number Card",
            "color": "#5e64ff",
            "document_type": "Opportunity",
            "filters": '{"account": "{{ filters.account }}"}'
        })
        
        # Add Contacts card
        dashboard.append("cards", {
            "label": "Contacts",
            "type": "Number Card",
            "color": "#743ee2",
            "document_type": "Contact",
            "filters": '{"account": "{{ filters.account }}"}'
        })
        
        dashboard.insert()
        creqit.db.commit()
        return dashboard
    return creqit.get_doc("Dashboard", "Account Statistics")

# Create dashboard on install
def on_install():
    create_account_dashboard() 