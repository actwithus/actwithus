from django.contrib import admin

import awucontacts.models as m

# class FooAdmin(admin.ModelAdmin):
#     ...

# admin.site.register(m.Foo, FooAdmin)
# admin.site.register(m.Bar)
# ...


class AddressInline(admin.StackedInline):

    model = m.Address


class ContactAdmin(admin.ModelAdmin):

    inlines = [
        AddressInline,
        ]


admin.site.register(m.Contact, ContactAdmin)
admin.site.register(m.Business)
admin.site.register(m.Volunteer)
admin.site.register(m.Supporter)
admin.site.register(m.Endorser)
admin.site.register(m.Prospect)
admin.site.register(m.Relationship)
admin.site.register(m.AreaOfInterest)
