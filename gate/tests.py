from django.test import TestCase
from .factories import UserFactory
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    ''' Test User model

    '''
    def test_create_or_get_user(self):
        ''' Test for creating a user if not existed or getting user

        '''
        user = UserFactory.create(id=3)
        actual_user = User.objects.get_one_or_none(pk = user.pk)
        self.assertEqual(user, actual_user)