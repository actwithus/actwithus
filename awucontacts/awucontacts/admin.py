from django.contrib import admin

import awucontacts.models as m


class AddressInline(admin.TabularInline):

    model = m.Address


class PhoneInline(admin.TabularInline):

    model = m.Phone


class EmailInline(admin.TabularInline):

    model = m.Email


## This is not allowed since `who` and `whom` both point to `Contact`

# class RelationshipInline(admin.TabularInline):
#
#     model = m.Relationship


class ContactAdmin(admin.ModelAdmin):

    inlines = [
        EmailInline,
        PhoneInline,
        AddressInline,
        # RelationshipInline,
        ]


r = admin.site.register
r(m.Contact, ContactAdmin)
