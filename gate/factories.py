import factory
from .models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('id',)
    
    id = 3
    username = 'alanalan'
    email = factory.LazyAttribute(lambda e: '%s@hotmail.com' % e.username)
    authority = User.GENERAL