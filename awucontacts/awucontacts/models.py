import django.db.models as m

from taggit.managers import TaggableManager


class Contact(m.Model):
    """Contact information about a person or business."""

    name = m.CharField(max_length=200, null=True)
    last_contacted = m.DateTimeField(null=True)
    interests = m.ManyToManyField('Interest')
    tags = TaggableManager()

    def __unicode__(self):
        return self.name


class Change(m.Model):

    contact = m.ForeignKey("Contact", related_name='changes')
    user = m.ForeignKey("auth.User", null=True)
    timestamp = m.DateTimeField(auto_now_add=True)
    message = m.CharField(max_length=250)


class Address(m.Model):

    TYPE_CHOICES = [
        ('H', 'Home'),
        ('W', 'Work'),
        ]

    contact = m.ForeignKey("Contact", related_name='addresses')
    type = m.CharField(max_length=1, choices=TYPE_CHOICES, null=True)
    address = m.TextField()
    postal_code = m.CharField(max_length=20, null=True)
    lat = m.DecimalField(max_digits=7, decimal_places=4, null=True)
    lon = m.DecimalField(max_digits=7, decimal_places=4, null=True)
    added = m.DateTimeField(auto_now_add=True)


class Phone(m.Model):

    TYPE_CHOICES = [
        ('H', 'Home'),
        ('W', 'Work'),
        ('M', 'Mobile'),
        ]

    contact = m.ForeignKey("Contact", related_name='phones')
    type = m.CharField(max_length=1, choices=TYPE_CHOICES, null=True)
    number = m.CharField(max_length=20)
    added = m.DateTimeField(auto_now_add=True)
    validated = m.DateTimeField(null=True)


class Email(m.Model):

    TYPE_CHOICES = [
        ('P', 'Personal'),
        ('W', 'Work'),
        ]

    contact = m.ForeignKey("Contact", related_name='emails')
    email = m.EmailField()
    type = m.CharField(max_length=1, choices=TYPE_CHOICES, null=True)
    added = m.DateTimeField(auto_now_add=True)
    validated = m.DateTimeField(null=True)


class Relationship(m.Model):

    who = m.ForeignKey("Contact", related_name='relationship_whos')
    whom = m.ForeignKey("Contact", related_name='relationship_whoms')
    tag = m.CharField(max_length=50)
    added = m.DateTimeField(auto_now_add=True)


class Interest(m.Model):

    name = m.CharField(max_length=100)
