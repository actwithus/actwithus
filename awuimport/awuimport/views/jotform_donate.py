"""Donation form importer.

new awucontacts.Contact
    tags = jotform, donor, 2011

awucontacts.Change
    user = NULL
    timestamp = now
    message = "Imported from JotForm"

First Name ->
Last Name ->
    awucontacts.Contact
        name = {First Name} {Last Name}

Street Address ->
Street Address Line 2 ->
City ->
State / Province ->
Postal / Zip Code ->
Country ->
    awucontacts.Address
        address =
            {Screet Address}
            {Street Address Line 2}
            {City}, {State / Province} {Postal / Zip Code}
            {Country}
        postal_code = {Postal / Zip Code}
        added = {Submission Date}

Phone Number ->
    awucontacts.Phone
        number = {Phone Number}
        added = {Submission Date}

E-mail ->
    awucontacts.Email
        email = {E-mail}
        added = {Submission Date}

Submission Date ->
    awucontacts.Change
        user = NULL
        timestamp = {Submission Date}
        message = "PayPal donation"

Occpation ->
Employer ->
Donation -> (extract donation amount from HTML)
Statement of Compliance ->
    awufundraiser.Donation
        amount = {Donation}
        payment_method = PayPal
        compliance_information = { occupation: {occupation}
                                 , employer: {employer}
                                 , compliance_statement: true
                                 }
        timestamp = {Submission Date}
"""
