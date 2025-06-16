# HMS - Hospital Management System for Odoo 18

A comprehensive Hospital Management System module for Odoo 18 that provides complete patient management, staff administration, CRM integration, security controls, and professional reporting capabilities.

## 🏥 Overview

The HMS (Hospital Management System) module is a production-ready Odoo 18 application designed to streamline hospital operations through integrated patient care, staff management, and administrative workflows. This module implements modern healthcare management practices with robust security controls and comprehensive reporting features.

## ✨ Key Features

### 🩺 Patient Management
- **Complete Patient Records**: First name, last name, email, birth date, blood type, medical history
- **Email Validation**: Unique email addresses with format validation and duplicate prevention
- **Age Auto-Calculation**: Automatic age computation based on birth date
- **State Tracking**: Patient status management (Undetermined, Good, Fair, Serious) with automatic logging
- **PCR Testing**: Automated PCR field checking for patients under 30 with CR ratio requirements
- **Medical History**: Conditional display of history field for patients over 50

### 👨‍⚕️ Staff & Department Management
- **Doctor Management**: Complete doctor profiles with first name, last name, and image
- **Department Administration**: Department capacity management with open/closed status tracking
- **Staff-Patient Linking**: Many-to-many relationships between doctors and patients
- **Capacity Controls**: Department capacity validation and patient assignment restrictions

### 🔗 CRM Integration
- **Customer Linking**: Seamless integration with Odoo CRM for patient-customer relationships
- **Email Conflict Prevention**: Constraints preventing duplicate email assignments across customers
- **Deletion Protection**: Safeguards against deleting customers linked to active patients
- **Tax ID Requirements**: Mandatory tax identification for all CRM customers

### 🔐 Security & Access Control
- **User Groups**: HMS User (limited access) and HMS Manager (full administrative access)
- **Record-Level Security**: Users can only access their own patient records
- **View-Level Restrictions**: Field and menu visibility based on user groups
- **Access Rights Management**: Granular permissions for create, read, update, delete operations

### 📊 Reporting & Analytics
- **Professional PDF Reports**: Comprehensive patient status reports with medical details
- **Log History Tracking**: Complete audit trail of patient state changes
- **QWeb Templates**: Native Odoo reporting framework integration
- **Export Capabilities**: Data export functionality for administrative purposes

## 🏗️ Technical Architecture

### Module Structure

hms/
├── init.py
├── manifest.py
├── models/
│ ├── init.py
│ ├── hms_patient.py # Core patient model
│ ├── hms_department.py # Department management
│ ├── hms_doctor.py # Doctor profiles
│ ├── hms_patient_log.py # Audit logging
│ └── res_partner.py # CRM integration
├── views/
│ ├── hms_patient_views.xml # Patient interface
│ ├── hms_department_views.xml
│ ├── hms_doctor_views.xml
│ ├── res_partner_views.xml # CRM extensions
│ └── hms_menus.xml # Navigation structure
├── security/
│ ├── hms_security.xml # User groups
│ ├── hms_record_rules.xml # Access rules
│ └── ir.model.access.csv # Model permissions
└── reports/
└── hms_patient_report.xml # PDF reporting

text

### Dependencies
- **Base Modules**: `base`, `mail`, `crm`, `contacts`
- **Python Requirements**: Odoo 18.0, Python 3.8+
- **Database**: PostgreSQL with proper user permissions

## 🚀 Installation

### Prerequisites
1. **Odoo 18 Environment**: Ensure Odoo 18 is properly installed and configured
2. **Virtual Environment**: Recommended to use Python virtual environment for dependency management
3. **Database Access**: PostgreSQL database with appropriate user permissions

### Installation Steps

1. **Clone Repository**:

cd /opt/odoo18/odoo18-custom-addons
git clone https://github.com/ayaemx/odoo-hms-module.git

text

2. **Activate Virtual Environment**:

source /opt/odoo18/odoo18-venv/bin/activate

text

3. **Install Dependencies**:

pip install -r requirements.txt

text

4. **Update Odoo Configuration**:
Add the custom addons path to your Odoo configuration file:

addons_path = /opt/odoo18/odoo18/addons,/opt/odoo18/odoo18-custom-addons

text

5. **Restart Odoo Service**:

sudo systemctl restart odoo18

text

6. **Install Module**:
- Navigate to Apps menu in Odoo
- Update Apps List
- Search for "HMS"
- Click Install

## 👥 User Management

### User Groups Configuration

#### HMS User Group
- **Access Level**: Limited access for regular staff
- **Permissions**: 
- Create/read/update own patient records only
- Read-only access to departments and doctors
- Cannot delete patient records
- Doctor fields hidden in patient forms
- Doctors menu item not visible

#### HMS Manager Group  
- **Access Level**: Full administrative access
- **Permissions**:
- Complete CRUD operations on all records
- Full access to patients, doctors, and departments
- Visible doctor fields and menu items
- Report generation capabilities

### Setting Up Users

1. **Navigate to Settings → Users & Companies → Users**
2. **Create New User** or edit existing user
3. **Assign HMS Groups** in the Access Rights tab
4. **Configure Additional Permissions** as needed

## 📋 Usage Guide

### Patient Registration
1. **Access Patient Menu**: Navigate to HMS → Patients
2. **Create New Patient**: Click "New" button
3. **Fill Required Information**: First name, last name, email, birth date, blood type
4. **Set Department**: Select from available open departments
5. **Assign Doctors**: Choose from department-associated doctors (Manager only)
6. **Save Record**: Patient automatically gets "Undetermined" status

### State Management
- **Status Updates**: Use header buttons to change patient status
- **Automatic Logging**: Each state change creates audit log entry
- **Status Options**: Undetermined, Good, Fair, Serious

### Report Generation
1. **Select Patient Record**: Navigate to specific patient
2. **Generate Report**: Use Print → Patient Status Report
3. **PDF Output**: Professional formatted report with complete patient details

## 🔧 Configuration

### Email Settings
- **SMTP Configuration**: Configure outgoing mail server for notifications
- **Email Templates**: Customize patient communication templates

### Department Setup
- **Capacity Management**: Set maximum patient capacity per department
- **Status Control**: Enable/disable department availability

### Security Configuration
- **Access Rules**: Configure record-level access permissions
- **Field Security**: Set field-level visibility based on user groups

## 🛠️ Development

### Extending the Module
The HMS module follows Odoo development best practices and can be extended through inheritance:

class HmsPatientExtended(models.Model):
_inherit = 'hms.patient'

text
custom_field = fields.Char(string='Custom Field')

text

### Custom Reports
Add new reports by creating QWeb templates in the `reports/` directory:
<template id="custom_report_template"> <t t-call="web.html_container"> <!-- Custom report content --> </t> </template> ```
📊 Data Model Relationships
Model	Relationship	Target Model	Description
hms.patient	Many2one	hms.department	Patient department assignment
hms.patient	Many2many	hms.doctor	Patient-doctor relationships
hms.patient	One2many	hms.patient.log	Audit trail logging
res.partner	Many2one	hms.patient	CRM customer linking
🔍 Troubleshooting
Common Issues

    Module Installation Fails:

        Check Odoo log files: /var/log/odoo18/odoo18.log

        Verify all dependencies are installed

        Ensure proper file permissions

    Access Denied Errors:

        Verify user group assignments

        Check record rules configuration

        Review access rights in CSV file

    Report Generation Issues:

        Confirm QWeb templates are properly loaded

        Check report action configuration

        Verify user permissions for report access

📝 License

This project is licensed under the LGPL-3 License - see the LICENSE file for details.
🤝 Contributing

    Fork the repository

    Create feature branch (git checkout -b feature/AmazingFeature)

    Commit changes (git commit -m 'Add AmazingFeature')

    Push to branch (git push origin feature/AmazingFeature)

    Open Pull Request

📞 Support

For support and questions:

    Issues: Create GitHub issue for bug reports

    Documentation: Refer to Odoo 18 official documentation

    Community: Join Odoo community forums for general questions

🎯 Roadmap

    Mobile application integration

    Advanced analytics dashboard

    Appointment scheduling system

    Inventory management integration

    Billing and insurance management

Version: 3.0
Odoo Compatibility: 18.0
Last Updated: June 2025
Status: Production Ready ✅

text

## **Step 3: Save and Exit**

Press `Ctrl + X`, then `Y`, then `Enter` to save the file.

## **Step 4: Add README to Git**

Add the new README.md file to your Git repository:

```bash
git add README.md

Step 5: Commit the README

Create a commit with a descriptive message:

bash
git commit -m "Add comprehensive README.md documentation

📚 Documentation Features:
- Complete module overview and feature descriptions
- Detailed installation and configuration instructions
- User management and security group documentation
- Usage guide with step-by-step instructions
- Technical architecture and development guidelines
- Troubleshooting section with common issues
- Contributing guidelines and support information

🎯 Content Coverage:
- Patient management capabilities
- Staff and department administration
- CRM integration features
- Security and access control
- Reporting and analytics
- Technical implementation details
- Production deployment guidance

✅ Professional documentation ready for GitHub showcase"
