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

Submission Date ->
    awucontacts.Change
        user = NULL
        timestamp = {Submission Date}
        message = "PayPal donation"

E-mail ->
    awucontacts.Email
        email = {E-mail}
        added = {Submission Date}

Phone Number ->
    awucontacts.Phone
        number = {Phone Number}
        added = {Submission Date}

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

Interests ->
    Separate by <br>
    awucontacts.Interest -> create or use existing:
        name = {Individual interest}
    add to contact.interests set

Other talents or resources you'd like to offer ->
    comments.Comment
        content_object = contact
        user_name = {First Name} {Last Name}
        user_email = {E-mail}
        submit_date = {Submission Date}
        is_public = True
        comment =
            Other talents or resources I'd like to offer:
            {Other talents or resources you'd like to offer}

Union Name ->
Union Local # ->
    awucontacts.Contact, create or use existing:
        name = {Union Name} Local {Union Local #}
        tags = "union local"
        added = {Submission Date}
    awucontacts.Relationship
        who = person contact
        whom = union contact
        tag = "is member of union"
        added = {Submission Date}
    awucontacts.Relationship
        who = union contact
        whom = person contact
        tag = "has union member"
        added = {Submission Date}
"""
