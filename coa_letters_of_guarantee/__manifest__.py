# -*- coding: utf-8 -*-
{
    'name': "COA Letters of Guarantee | Bank Guarantee Management",
    'summary': "Comprehensive management for Bid Bonds, Performance Bonds, Advance Payment, and Maintenance Guarantees with automated accounting entries",
    'description': """
COA Letters of Guarantee Management System for Odoo 19 / 18 / 17
================================================================
Enterprise bank letters of guarantee and financial bonding management system:
- Bid Bonds (Preliminary Guarantees for Public/Private Tenders).
- Performance Bonds (Final Guarantees ensuring contract delivery).
- Advance Payment Guarantees (Securing advance project disbursements).
- Maintenance & Warranty Bonds (Post-completion defect liability).
- Automated double-entry accounting (Bank Cash Margin, Bank Commissions & Expenses, Main Bank).
- Expiration tracking, extension management, and proactive maturity alerts.
- Automated release logic with cash cover margin refund to bank account.
- Complete chatter audit trail and status tracking from draft to release/liquidation.
    """,
    'author': "Community of accountants (COA-Egypt)",
    'website': "https://www.coa-egy.com",
    'category': 'Accounting/Accounting',
    'version': '19.0.1.0.0',
    'price': 49.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bid_bond.xml',
        'views/performance_bond.xml',
        'views/advance_payment_guarantee.xml',
        'views/res_config_settings.xml',
        'views/maintenance_bond.xml',
        'views/account_move.xml',
        'wizard/check_lg_accounts.xml',
        'views/menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/01_bid_bonds_list.png',
        'static/description/02_bid_bond_form.png',
        'static/description/03_performance_bonds_list.png',
        'static/description/04_performance_bond_form.png'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

