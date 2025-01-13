import frappe
from frappe.utils import date_diff

def execute(filters=None):
    columns = [
        {
            "label": "Car Name", 
            "fieldname": "car_name", 
            "fieldtype": "Data", 
            "width": 150
        },
        {
            "label": "Model Name",
            "fieldname": "model_name", 
            "fieldtype": "Data", 
            "width": 150
        },
        {
            "label": "Total Rental Days", 
            "fieldname": "total_rental_days", 
            "fieldtype": "Int", 
            "width": 120
        },
        {
            "label": "Availability", 
            "fieldname": "availability_status", 
            "fieldtype": "Select", 
            "width": 120
        },
        {
            "label": "Revenue Generated", 
            "fieldname": "revenue_generated", 
            "fieldtype": "Currency", 
            "width": 150
        },
        {
            "label": "Insurance Expiry Date",
            "fieldname": "insurance_expiry_date", 
            "fieldtype": "Date", 
            "width": 150
        },
    ]

    cars = frappe.get_all(
        "Car",
        fields=[
            "name as car_name",
            "model_name",
            "availability",
            "insurance_expiry_date",
            "daily_rental_rate"
        ]
    )

    data = []


    for car in cars:
        total_rental_days = 0
        revenue_generated = 0

        bookings = frappe.get_all(
            "Booking",
            filters={"car": car["car_name"]},
            fields=["start_date", "end_date"]
        )

  
        for booking in bookings:
            if booking["start_date"] and booking["end_date"]:
               
                rental_days = date_diff(booking["end_date"], booking["start_date"]) + 1
                total_rental_days += rental_days
               
                revenue_generated += rental_days * car["daily_rental_rate"]

      
        data.append({
            "car_name": car["car_name"],
            "model_name": car["model_name"],
            "total_rental_days": total_rental_days,
            "availability_status": car["availability"],
            "revenue_generated": revenue_generated,
            "insurance_expiry_date": car["insurance_expiry_date"],
        })

    return columns, data
