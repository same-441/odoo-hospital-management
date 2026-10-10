from odoo import models,fields



class PatientComplaint(models.TransientModel):
    _name="patient.complaint"
    _description="Patient Complaint"


    patient_id=fields.Many2one("hospital.patient", string="Patient")
    complaint=fields.Text(string="Complaint")