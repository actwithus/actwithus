"""'West Complete' membership list importer.


new awucontacts.Contact
    tags = west complete, volunteer, 2010

awucontacts.Change
    user = NULL
    timestamp = now
    message = "Imported from West Complete"

Add Date ->
    if empty:
        Add Date = now
        awucontacts.Change
            user = NULL
            timestamp = now
            message = "Note: No 'Add Date' in West Complete"


fullname ->
fname ->
lname ->
    if fullname:
        awucontacts.Contact
            name = {fullname}
        if fname or lname:
            awucontacts.Change
                user = NULL
                timestamp = {Add Date}
                message = "Note: first name '{fname}' and last name '{lname}' in West Complete"
    elif fname or lname:
        name = {fname} {lname}
    else:
        awucontacts.Change
            user = NULL
            timestamp = {Add Date}
            message = "Note: no name given in West Complete"


ADDRESS ->
CITY ->
ZIP ->
COUNTY ->
    awucontacts.Address
        address =
            {ADDRESS}
            {CITY}, WA {ZIP}
            {COUNTY} county
        postal_code = {ZIP}
        added = {Add Date}

PHONE ->
    awucontacts.Phone
        number = {PHONE}
        added = {Add Date}

email ->
    awucontacts.Email
        email = {email}
        added = {Add Date}

NOTES ->
    comments.Comment
        content_object = contact
        user_name = Google Docs: West Complete
        submit_date = {Add Date}
        is_public = True
        comment =
            {NOTES}
"""
