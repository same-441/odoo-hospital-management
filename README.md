# Hospital Management System – Odoo 17 Module

A custom Odoo 17 module for managing patients, appointments and billing in a small hospital or clinic.

Built as a practice project to learn Odoo backend and frontend development: ORM models, views, security, workflows, inheritance and email templates.

## Features

- **Patients**: personal details, tags, minor/guardian logic (guardian required for minors), and protection against deleting patients who have appointments
- **Appointments**: auto-generated references (`HP00001`), status workflow *Draft → Confirmed → Ongoing → Done / Cancelled* with change tracking
- **Appointment lines**: products and quantities per appointment, with a computed total
- **Invoicing integration**: invoices can be linked to an appointment by extending Odoo's `account.move` model and views
- **Email confirmation**: one-click email to the patient using a QWeb mail template
- **Roles**: *Receptionist* and *Doctor* user groups; configuration menus and some fields are visible to doctors only
- **Search and filters**: search by reference or patient, group by patient or gender, side search panels
- **Read-only patient list** for front-desk staff
- **Complaint wizard** opened from the patient form
- **Chatter**: messages, followers and activities on patients and appointments

## Technical overview

| Area | What it shows |
| --- | --- |
| Models | `hospital.patient`, `hospital.appointment`, `hospital.appointment.line`, `patient.tag`, transient `patient.complaint` |
| ORM | Many2one, One2many, Many2many, related and computed fields, `@api.depends`, overriding `create` and `unlink` |
| Inheritance | `_inherit` on `account.move`, XPath view inheritance, `mail.thread` mixin |
| Views | List, form, search, search panel, notebook, statusbar, decorations, multiple views for one model |
| Security | Access rights (`ir.model.access.csv`), user groups, group-restricted menus and fields |
| Data | `ir.sequence` for references, `mail.template` for emails |

## Installation

1. Copy the `om_hospital` folder into your Odoo 17 custom addons directory.
2. Add that directory to `addons_path` in your Odoo config.
3. Restart Odoo, activate **Developer Mode**, and click **Update Apps List**.
4. Search for **Hospital Management System** in Apps and click **Install**.

Dependencies: `base`, `mail`, `product`, `account` (all included in Odoo Community).

## Author

**Sammer** – M.Sc. Automotive Software Engineering, TU Chemnitz
