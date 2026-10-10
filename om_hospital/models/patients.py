from odoo import models, fields, _
from odoo.exceptions import ValidationError,UserError
class HospitalPatient(models.Model):
    _name='hospital.patient'
    _rec_name='name'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Patient Master'

    name=fields.Char(string="Name"  , help='Enter the full name of the patient.' , required=True , tracking=True)
    date_of_birth =fields.Date(string="DOB", tracking=True)
    email=fields.Char(string="Email", tracking=True)
    gender= fields.Selection([('male', 'Male'),('female','Female')] ,string="Gender")
    tag_ids=fields.Many2many('patient.tag' , 'patient_tag_rel','patient_id','tag_ids',string="Tags")
     #defining the newly created table name with column name
    is_minor=fields.Boolean(string="Minor")
    guardian_name=fields.Char(string="Guardian")


 #inheriting the uplink method to delte a record
    def unlink(self):
     for rec in self:
        domain = [('patient_id', '=', rec.id)]#search filter where patients id equals to current id
        appointments = self.env['hospital.appointment'].search(domain)#actually runs that search,query the model directly
        if appointments:
            raise UserError(_("You cannot delete the patient now.\nAppointments existing for this patient: %s", rec.name))
     return super().unlink()

   #defininig the open complaint method to open the complaint form view 
    def action_open_complaint(self):
       return{
          'type' : 'ir.actions.act_window',
          'name' : _('Complaint'),
          'view_mode' : 'form',
          'res_model' : 'patient.complaint',
          'target' : 'new',
       }