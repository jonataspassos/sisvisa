from abc import ABC,abstractmethod
import base64

class ClassSerial(ABC):
    @abstractmethod
    def parse(string):
        """Takes a string of SerialObject and splits into a Object"""
        # fields = string.split(' ')
        # fields = [base64.b64decode(f.encode('utf-8')).decode("utf-8") for f in fields]
            
        # if len(fields) != 7:
            # raise ValidationError(_("Invalid input for a Endereco instance"))
        # return Endereco(*fields)
        pass
    
    def __str__(self):
        return ', '.join(self.tolist())
    
    @abstractmethod
    def __repr__(self) -> str:
        # return self.logradouro[:10] + ' ... ' + self.numero +' ' + self.complemento + ', '+ self.bairro[:10]
        pass
    
    def tostr(self):
        return ' '.join([base64.b64encode(f.encode('utf-8')).decode("utf-8") for f in self.tolist()])
    
    @abstractmethod
    def tolist(self):
        pass