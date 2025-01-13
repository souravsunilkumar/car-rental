# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe
def execute(filters=None):
    

    
    columns = [
        {"fieldname": "car_name", "label": "Car Name", "fieldtype": "Data", "width": 120},
        {"fieldname": "model_name", "label": "Model Name", "fieldtype": "Data", "width": 120},
        {"fieldname": "total_revenue", "label": "Total Revenue", "fieldtype": "Currency", "width": 120},
        {"fieldname": "total_maintenance_cost", "label": "Total Maintenance Cost", "fieldtype": "Currency", "width": 120},
        {"fieldname": "profit", "label": "Profit", "fieldtype": "Currency", "width": 120},
    ]

   
    cars = frappe.get_all(
        "Car",
        fields=["name", "car_name", "model_name"]
    )
    


    

    bookings = frappe.get_all(
        "Booking",
        
        fields=["car", "total_price"]
    )

    

    maintenance_records = frappe.get_all(
        "Maintanance",  
        
        fields=["car", "maintenance_cost"]  
    )

    
    revenue_data = {}
    for booking in bookings:
        car = booking["car"]
        revenue_data.setdefault(car, {"total_revenue": 0, "total_maintenance_cost": 0})
        revenue_data[car]["total_revenue"] += booking["total_price"]

    for record in maintenance_records:
        car = record["car"]
        revenue_data.setdefault(car, {"total_revenue": 0, "total_maintenance_cost": 0})
        revenue_data[car]["total_maintenance_cost"] += record["maintenance_cost"]

    
    data = []
    for car in cars:
        car_data = revenue_data.get(car["name"], {"total_revenue": 0, "total_maintenance_cost": 0})
        total_revenue = car_data["total_revenue"]
        total_maintenance_cost = car_data["total_maintenance_cost"]
        profit = total_revenue - total_maintenance_cost

        data.append({
            "car_name": car["car_name"],
            "model_name": car["model_name"],
            "total_revenue": total_revenue,
            "total_maintenance_cost": total_maintenance_cost,
            "profit": profit
        })

    return columns, data
