import django.db.models as m


class Contact(m.Model):
    """Contact information about a person or business."""

    name = m.CharField(max_length=200)
    last_contacted = m.DateTimeField(null=True)

    def __unicode__(self):
        return self.name


class Address(m.Model):

    contact = m.ForeignKey("Contact", related_name='addresses')
    type = m.CharField(max_length=20)
    address = m.TextField()
    lat = m.DecimalField(max_digits=7, decimal_places=4)
    lon = m.DecimalField(max_digits=7, decimal_places=4)
    added = m.DateTimeField(auto_now_add=True)

    # TODO: Add geographic information.


class PhoneNumber(m.Model):

    contact = m.ForeignKey("Contact", related_name='phone_numbers')
    type = m.CharField(max_length=20)
    number = m.CharField(max_length=20)
    added = m.DateTimeField(auto_now_add=True)
    validated = m.DateTimeField(null=True)


class EmailAddress(m.Model):

    contact = m.ForeignKey("Contact", related_name='email_addresses')
    type = m.CharField(max_length=20)
    email = m.CharField(max_length=20)
    added = m.DateTimeField(auto_now_add=True)
    validated = m.DateTimeField(null=True)


class Business(m.Model):

    contact = m.OneToOneField("Contact")
    last_endorsement = m.DateField(null=True)


class Volunteer(m.Model):

    contact = m.OneToOneField("Contact")
    since = m.DateField()
    areas_of_interest = m.ManyToManyField('AreaOfInterest')


class Supporter(m.Model):

    contact = m.OneToOneField("Contact")
    since = m.DateField()


class Endorser(m.Model):

    contact = m.OneToOneField("Contact")
    since = m.DateField()


class Prospect(m.Model):

    contact = m.OneToOneField("Contact")
    type = m.CharField(max_length=20)   # Business, Volunteer, Supporter, Endorser
    since = m.DateField()


class Relationship(m.Model):

    who = m.ForeignKey("Contact", related_name='relationship_whos')
    whom = m.ForeignKey("Contact", related_name='relationship_whoms')
    tag = m.CharField(max_length=50)


class AreaOfInterest(m.Model):

    name = m.CharField(max_length=100)
