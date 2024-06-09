
Protocolos - Documentações Ex.: Certificado de Inspeção Sanitária
    n/n Ordem de serviço
    Pode ser originado
        Entrada da empresa
        Denúncia

Fiscal
Empresa
Veículo -> Empresa
Endereço
Usuários
    CRU_ empresas
    

Denúncia
    Data
    Motivo
    Empresa* / Endereço
    Relato
    Pessoa/Ouvidoria

Ordem de serviço
    quem criou a ordem de serviço
    Fiscal
    Observação
    Parecer

Termo de Intimação
    Empresa
    Data
    Motivo
    Ordem de serviço gerada

* consulta OS
    Resumo OS anteriores (data, observação) (mesmo processo/protocolo)
    Infrações anteriores 
    Multas (status)

Resultados da ordem de serviço
    Ordem de serviço de origem
    Vistoriado

    Termo de Intimação -> revistoriar 15
    Auto de Infração -> tramite(revistoriar 15 *)
    Auto de Multa -> tramite(revistoriar 15 *)
    Interdição (fecha o protocolo *)
    Não Localizado (Entra em contato com a empresa) -> revistoriar 15
    Certificado(Cis) Liberado (fecha o protocolo)
        Processo arquivado
        Emissão do documento

Documentos
        Certificado de Inspeção Sanitária
        Licença de Veículo
        Termo de Licença Sanitária
    Empresa/Veículo
    Fiscal
    Validade
    Tipo




bairros
estado
municipio

roteiro
usuarios
validade

tabmul multa
tabinf infração
tabint intimação
tabden denuncia

tabcis certificado
tablve licença
tabtls termo de licença





tabrec RECLAMACAO