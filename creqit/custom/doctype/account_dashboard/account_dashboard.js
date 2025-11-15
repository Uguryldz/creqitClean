// Copyright (c) 2024, creqit Technologies and contributors
// For license information, please see license.txt

creqit.pages['dashboard-view'].on_page_load = function(wrapper) {
    creqit.ui.make_app_page({
        parent: wrapper,
        title: __("Account Dashboard"),
        single_column: true
    });

    let page = wrapper.page;
    page.account_dashboard = new creqit.AccountDashboard({
        wrapper: wrapper,
        page: page
    });
};

creqit.AccountDashboard = class AccountDashboard extends creqit.Dashboard {
    setup_defaults() {
        return super.setup_defaults().then(() => {
            this.page_title = __("Account Dashboard");
            this.dashboard_settings = creqit.get_user_settings("Account Dashboard")["dashboard_settings"] || null;
        });
    }

    setup() {
        this.setup_dashboard();
        this.setup_filters();
        this.refresh();
    }

    setup_dashboard() {
        this.container = $('<div class="dashboard-container"></div>').appendTo(this.wrapper);
    }

    setup_filters() {
        this.filters = {
            account: null
        };

        // Account filtresi ekle
        this.filter_area = $('<div class="filter-area" style="margin-bottom: 20px;"></div>').appendTo(this.container);
        
        this.account_field = new creqit.ui.form.Link({
            parent: this.filter_area,
            label: __("Account"),
            fieldname: "account",
            options: "Account",
            change: () => {
                this.filters.account = this.account_field.value;
                this.refresh();
            }
        });
    }

    refresh() {
        if (!this.filters.account) {
            return;
        }

        // Update filters for all cards
        this.dashboard_settings = {
            filters: {
                account: this.filters.account
            }
        };

        // Refresh dashboard
        this.dashboard.refresh();
    }
}; 