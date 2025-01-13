# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Booking(Document):
    def validate(self):
        self.calculate_total_price()
        self.validate_dates()

    def after_save(self):
       
        car = frappe.get_doc("Car", self.car)
        if self.status == "Rented":
            car.availability = "Rented"
        elif self.status == "Returned":
            car.availability = "Available"
        car.save()

    def calculate_total_price(self):
        
        if not self.start_date or not self.end_date:
            frappe.throw("Please set both Start Date and End Date.")
        
        if not self.car:
            frappe.throw("Please select a Car for the booking.")
        
        
        car = frappe.get_doc("Car", self.car)
        daily_rental_rate = car.daily_rental_rate

        
        duration = frappe.utils.date_diff(self.end_date, self.start_date)
        if duration < 1:
            frappe.throw("End Date must be after Start Date.")

        self.total_price = daily_rental_rate * duration

    def validate_dates(self):
        
        overlapping_bookings = frappe.get_all(
            "Booking",
            filters={
                "car": self.car,
                "status": "Rented",
                "name": ["!=", self.name],
                "start_date": ["<=", self.end_date],
                "end_date": [">=", self.start_date],
            },
            fields=["name"]
        )
        if overlapping_bookings:
            frappe.throw(
                f"The selected car is already booked for the another dates. Booking ID: {overlapping_bookings[0]['name']}"
            )