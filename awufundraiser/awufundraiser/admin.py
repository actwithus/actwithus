from django.contrib import admin

import awufundraiser.models as m


r = admin.site.register
r(m.Donation)
