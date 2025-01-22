# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RentalBooking(Document):
    pass
    # def validate(self):
    #     self.calculate_booking_charges()
        
    # def calculate_booking_charges(self):
    #     if not self.vehicle:
    #         throw(_("Please select a vehicle for the booking."))
    #     vehicle_details = frappe.get_doc("Vehicle Registration", self.vehicle)
    #     hourly_rate = vehicle_details.hourly_rate or 0
    #     start_datetime = datetime.strptime(self.start_date, "%Y-%m-%d %H:%M:%S")
    #     end_datetime = datetime.strptime(self.end_date, "%Y-%m-%d %H:%M:%S")
    #     duration_hours = (end_datetime - start_datetime).total_seconds() / 3600
        
        
    #     self.total_hours = round(duration_hours, 2)
    #     self.total_amount = round(self.total_hours * hourly_rate, 2)
    
