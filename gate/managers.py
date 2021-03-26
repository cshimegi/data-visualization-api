from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager

class ModelManager(BaseUserManager):
    '''
    Model manager interface

    Extend model's methods
    '''
    def get_one_or_none(self, **kwargs):
        '''Get one if object exists; otherwise, return None
        
        Args:
            kwargs (dict): field1 = value1, field2 = value2, ...

        Returns:
            The return value. self.model if exists, None otherwise.
        '''
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None