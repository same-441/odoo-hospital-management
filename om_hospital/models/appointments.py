from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    # as a list of name you want to filter in appointment line
    _rec_names_search = ['reference', 'patient_id']
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", default='New')
    patient_id = fields.Many2one(
        'hospital.patient', string="Patient", required=False, ondelete='restrict')
    date_appointment = fields.Date(string="Date", default=fields.Date.context_today)
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', tracking=True)
    appointment_line_ids = fields.One2many(
        'hospital.appointment.line', 'appointment_id', string="Lines")
    total_qty = fields.Float(
        compute='_compute_total_qty', string="Total Quantity")
    date_of_birth = fields.Date(related='patient_id.date_of_birth', store=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)

    @api.model_create_multi
    def create(self, vals_list):  # inheriting or supering the create method
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code(
                    'hospital.appointment')
        return super().create(vals_list)

    # this tell when to recompute
    @api.depends('appointment_line_ids', 'appointment_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            total_qty = 0
            for line in rec.appointment_line_ids:
                total_qty = total_qty + line.qty
            rec.total_qty = total_qty

    @api.depends('reference', 'patient_id.name')
    def _compute_display_name(self):
        for rec in self:
            # show reference and patient name in dropdowns and search
            rec.display_name = f"[{rec.reference}] {rec.patient_id.name}"

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_send_email(self):
        self.ensure_one()
        if not self.patient_id.email:
            raise UserError(_("Patient %s has no email!", self.patient_id.name))
        template = self.env.ref('om_hospital.email_template_appointment', raise_if_not_found=False)
        if not template:
            raise UserError(_("Email template not found!"))
        template.send_mail(self.id, force_send=True)


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one(
        'hospital.appointment', string="Appointment", ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Product")
    qty = fields.Float(string="Quantity")
