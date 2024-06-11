from django.db import models
from abc import ABC,abstractmethod
from .utils import ClassSerial

# Create your models here.
class FieldSerial(models.Field,ABC):

    def __init__(self,classSerial:ClassSerial,max_length, *args, **kwargs):
        self.T = classSerial
        kwargs["max_length"] = max_length
        super().__init__(*args, **kwargs)
    
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.T.parse(value)

    def to_python(self, value):
        if isinstance(value, self.T):
            return value

        if value is None:
            return value

        return self.T.parse(value)    
    
    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None and value != '':
            return value.tostr()
        return None

    # def formfield(self, **kwargs):
    #     return super().formfield(form_class=self.T,**kwargs)

    def get_internal_type(self):
        return "CharField"
    
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return value.tostr()

class ModelSerial(models.Model,ABC):
    @abstractmethod
    def ObjectClass(self)->ClassSerial:
        pass        
    @abstractmethod
    def ObjectField(*args,**kwargs)->FieldSerial:
        pass