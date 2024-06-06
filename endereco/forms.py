from django.forms import CharField, MultiValueField
from django.core.validators import RegexValidator
from .utils import Endereco as EnderecoClass

class EnderecoField(MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            "required": "There are fields required empty", 
            "invalid": "Enter valid values to the fields",
            "incomplete": "Enter a complete location."
        }
        # Or define a different message for each field.
        fields = (
            CharField(label="logradouro",error_messages={"required":"Enter a 'logradouro'.","invalid":"Enter a valid 'logradouro'","incomplete":"Enter a complete 'logradouro'"},required=True),
            CharField(label="numero",error_messages={"required":"Enter a 'numero'.","invalid":"Enter a valid 'numero'","incomplete":"Enter a complete 'numero'"},required=True),
            CharField(label="complemento",error_messages={"required":"Enter a 'complemento'.","invalid":"Enter a valid 'complemento'","incomplete":"Enter a complete 'complemento'"},required=False),
            CharField(label="bairro",error_messages={"required":"Enter a 'bairro'.","invalid":"Enter a valid 'bairro'","incomplete":"Enter a complete 'bairro'"},required=True),
            CharField(label="cidade",error_messages={"required":"Enter a 'cidade'.","invalid":"Enter a valid 'cidade'","incomplete":"Enter a complete 'cidade'"},required=True),
            CharField(label="estado",error_messages={"required":"Enter a 'estado'.","invalid":"Enter a valid 'estado'","incomplete":"Enter a complete 'estado'"},required=True),
            CharField(label="cep",error_messages={"required":"Enter a 'cep'.","invalid":"Enter a valid 'cep'","incomplete":"Enter a complete 'cep'"},validators=[RegexValidator(r"^[0-9]{2}[\.\- ]?[0-9]{3}[\.\- ]?[0-9]{3}$", "Enter a valid cep.")],required=False),
        )
        super().__init__(
            error_messages=error_messages,
            fields=fields,
            require_all_fields=False,
            **kwargs
        )

        self.widget.decompress = self.decompress
        

    def compress(self, data_list):
        return EnderecoClass(*data_list)
    
    def decompress(self,value):
        return value.tolist()