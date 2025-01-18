# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class Bookings(Document):
    def validate(self):
        self.calculate_total_amount()
        
        
    def calculate_total_amount(self):
        total_amount = 0
        for row in self.booking_cars:
            if not(row.car and row.start_date and row.end_date):
                frappe.throw("Please select Car, Start Date and End Date in row {}".format(row.idx))
            
            model_name=frappe.db.get_value("Car",row.car,"model_name")
            daily_rent_rate = frappe.db.get_value("Model Name", model_name, "daily_rent_rate")
            
            if not daily_rent_rate:
                frappe.throw("Daily Rent Rate not found for Car {model_name}.")
            
            rental_days = date_diff(row.end_date,row.start_date) +1
            if rental_days < 0:
                frappe.throw("End Date cannot be before Start Date.")
            
            row.total_rate= rental_days * daily_rent_rate
            total_amount += row.total_rate
            
        self.total_amount = total_amount
        