# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
        {"fieldname": "car", "label": "Car", "fieldtype": "Link", "options": "Car", "reqd": 1},
        {"fieldname": "maintenance_date", "label": "Maintenance Date", "fieldtype": "Date", "reqd": 1},
        {"fieldname": "description", "label": "Description", "fieldtype": "Data"},
        {"fieldname": "cost", "label": "Cost", "fieldtype": "Currency", "reqd": 1},
        {"fieldname": "maintenance_type", "label": "Maintenance Type", "fieldtype": "Data"},
        {"fieldname": "follow_up_date", "label": "Follow-up Date", "fieldtype": "Date"},
        {"fieldname": "service_center", "label": "Service Center", "fieldtype": "Data"},
        {"fieldname": "service_provider", "label": "Service Provider", "fieldtype": "Data"},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data"},
        # {"fieldname": "notes", "label": "Notes"}
    ]
	data = frappe.db.get_all('Maintanance',fields = ['car','maintenance_date','description','description','cost','maintenance_type','follow_up_date','service_center','service_provider','status'])
	return columns, data