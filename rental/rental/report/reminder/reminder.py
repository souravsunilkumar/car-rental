# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe
def execute(filters=None):
    
    columns = [
        {"fieldname": "car_name", "label": "Car Name", "fieldtype": "Data"},
        {"fieldname": "model_name", "label": "Model Name", "fieldtype": "Data"},
        {"fieldname": "vehicle_number", "label": "Vehicle Number", "fieldtype": "Data"},
        {"fieldname": "insurance_expiry_date", "label": "Insurance Expiry Date", "fieldtype": "Date"},
        {"fieldname": "status", "label": "Maintenance Status", "fieldtype": "Select", "options": "Pending\nDone"},
        {"fieldname": "maintanance_date", "label": "Maintenance Date", "fieldtype": "Date"},
        {"fieldname": "type", "label": "Maintenance Type", "fieldtype": "Data"},
    ]

    
    cars = frappe.get_all(
        "Car",
        fields=["name", "car_name", "model_name", "vehicle_number", "insurance_expiry_date"],
    )

    
    maintenance = frappe.get_all(
        "Maintanance",
        fields=["car", "maintanance_date", "status", "type"],
    )

    
    data = []
    for car in cars:
        
        car_maintenance = [ca for ca in maintenance if ca.get("car") == car.get("name")]

        if car_maintenance:
            
            for record in car_maintenance:
                data.append({
                    "car_name": car["car_name"],
                    "model_name": car["model_name"],
                    "vehicle_number": car["vehicle_number"],
                    "insurance_expiry_date": car["insurance_expiry_date"],
                    "status": record["status"],
                    "maintanance_date": record["maintanance_date"],
                    "type": record["type"],
                })
        else:
           
            data.append({
                "car_name": car["car_name"],
                "model_name": car["model_name"],
                "insurance_expiry_date": car["insurance_expiry_date"],
                "status": None,
                "maintanance_date": None,
                "type": None,
            })

    return columns, data