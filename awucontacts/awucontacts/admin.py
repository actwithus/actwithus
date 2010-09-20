from django.contrib import admin
from django.contrib.contenttypes import generic

import awucontacts.models as m


class AddressInline(generic.GenericTabularInline):

    model = m.Address


class PhoneInline(generic.GenericTabularInline):

    model = m.Phone


class EmailInline(generic.GenericTabularInline):

    model = m.Email


## This is not allowed since `who` and `whom` both point to `Contact`

# class RelationshipInline(admin.TabularInline):
#
#     model = m.Relationship


class PersonAdmin(admin.ModelAdmin):

    inlines = [
        EmailInline,
        PhoneInline,
        AddressInline,
        # RelationshipInline,
        ]


class OrganizationAdmin(admin.ModelAdmin):

    inlines = [
        EmailInline,
        PhoneInline,
        AddressInline,
        # RelationshipInline,
        ]


r = admin.site.register
r(m.Person, PersonAdmin)
r(m.Organization, OrganizationAdmin)
