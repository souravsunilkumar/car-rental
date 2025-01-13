# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Car(Document):
    def validate(self):
        self.update_booking_status()

    def update_booking_status(self):
        
        if self.availability == "Available":
            booking = frappe.get_all(
                "Booking",
                filters={"car": self.name, "status": "Rented"},
                fields=["name"],
                limit=1,
            )
            if booking:
                booking_doc = frappe.get_doc("Booking", booking[0].name)
                booking_doc.status = "Returned"
                booking_doc.save()