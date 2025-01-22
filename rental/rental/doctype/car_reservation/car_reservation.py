# Copyright (c) 2025, sourav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import _, throw

class CarReservation(Document):
    pass
    # def validate(self):
    #     """
    #     Perform validations before saving the car reservation document.
    #     """
    #     self.validate_dates()
    #     self.validate_vehicle_availability()

    # def validate_dates(self):
    #     """
    #     Ensure reservation dates are valid.
    #     """
    #     if not self.start_date or not self.end_date:
    #         throw(_("Start Date and End Date are required."))

    #     if self.start_date >= self.end_date:
    #         throw(_("End Date must be later than Start Date."))
            
	# def validate_vehicle_availability(self):
    #     overlapping_reservations = frappe.db.sql(
    #         """
    #         SELECT name FROM `tabCar Reservation`
    #         WHERE vehicle = %s AND docstatus < 2
    #         AND (
    #             (%s BETWEEN start_date AND end_date) OR
    #             (%s BETWEEN start_date AND end_date) OR
    #             (start_date BETWEEN %s AND %s)
    #         )
    #         """,
    #         (self.vehicle, self.start_date, self.end_date, self.start_date, self.end_date),
    #     )

    #     if overlapping_reservations:
    #         throw(_("The selected vehicle is already reserved for the given time period."))
