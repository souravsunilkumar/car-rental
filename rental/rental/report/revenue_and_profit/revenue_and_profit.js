// Copyright (c) 2025, sourav and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue and Profit"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": "",
			"reqd": 0
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": "",
			"reqd": 0
		}
	]
};