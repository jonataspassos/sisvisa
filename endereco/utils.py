import base64
from django.core.exceptions import ValidationError

class Endereco:
    def __init__(self,logradouro,numero=None,complemento=None,bairro=None,cidade=None,estado=None,cep=None):
        if numero == None:
            try:
                end = self.parse(logradouro)
                self.logradouro = end.logradouro
                self.numero = end.numero
                self.complemento = end.complemento
                self.bairro = end.bairro
                self.cidade = end.cidade
                self.estado = end.estado
                self.cep = end.cep
            except:
                raise ValidationError(_("Invalid input for a Endereco instance"))
        elif numero==None or bairro==None or cidade==None or estado==None:
            raise ValidationError(_("Invalid input for a Endereco instance"))
        else:
            self.logradouro = logradouro
            self.numero = numero
            self.complemento = complemento
            self.bairro = bairro
            self.cidade = cidade
            self.estado = estado
            self.cep = cep
    
    def parse(string):
        """Takes a string of endereco and splits into a full endereco."""
        fields = string.split(' ')
        fields = [base64.b64decode(f.encode('utf-8')).decode("utf-8") for f in fields]
            
        if len(fields) != 7:
            raise ValidationError(_("Invalid input for a Endereco instance"))
        return Endereco(*fields)
    
    def __str__(self):
        return ', '.join(self.tolist())
    def __repr__(self) -> str:
        return self.logradouro[:10] + ' ... ' + self.numero +' ' + self.complemento + ', '+ self.bairro[:10]
    
    def tostr(self):
        return ' '.join([base64.b64encode(f.encode('utf-8')).decode("utf-8") for f in self.tolist()])
    def tolist(self):
        return [
            self.logradouro,
            self.numero,
            self.complemento,
            self.bairro,
            self.cidade,
            self.estado,
            self.cep
        ]