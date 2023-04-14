import pandas
import requests
import uuid
import datetime
import math
from dateutil import parser

SHEET_ID = '1kC-mPQm-Fvk8q6sxUW27CgHeNIWY__mFTiQ66jtKsYs'
SHEET_NAME = 'sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

# Importamos el excel a un DataFrame
df = pandas.read_csv(url)

# Aseguramos igual cantidad de rows/columns
df = df.reset_index()

# Para cada Row extraemos las columnas,
#               generamos un QuestionnaireResponse
#               lo validamos
#               si es valido lo POSTeamos al servidor FHIR

for index, row in df.iterrows():
    Questionario = row['Questionario']
    Codigo = row['Codigo']
    Status = row['Status']
    Descricao = row['Descricao']
    Proposito = row['Proposito']
    PaisOrigem = row['Pais Origem (http://paho.org/esavi/ValueSet/CodPaises)']
    NomeOrganizacaoNotificadora = row['Nome Organizacao Notificadora (string)']
    CodigoEnderecoOrganizacao = row[
        'Codigo Endereco Organizacao (http://paho.org/esavi/ValueSet/DirOrgNotiVS)']
    NomeEnderecoOrganizacao = row['Nome Endereco Organizacao']
    CodigoProfissionalNotificador = row[
        'Codigo Profissional Notificador (http://paho.org/esavi/ValueSet/ProfesionalNotificadorVS)']

    DataConsulta = row['Data consulta']
    try:
        DataConsulta = parser.parse(DataConsulta)
    except:
        continue

    DataNotificacao = row['Data notificação']
    try:
        DataNotificacao = parser.parse(DataNotificacao)
    except:
        continue

    DataPreenchimento = row['Data preenchimento']
    try:
        DataPreenchimento = parser.parse(DataPreenchimento)
    except:
        continue

    DataPreenchimentoBaseNacional = row['Data preenchimento base nacional']
    try:
        DataPreenchimentoBaseNacional = parser.parse(
            DataPreenchimentoBaseNacional)
    except:
        continue

    NumeroCaso = row['Numero caso']
    IdPaciente = row['Id paciente']
    EnderecoPaciente = row['Endereco paciente (http://paho.org/esavi/ValueSet/DirOrgNotiVS)']
    NomeEnderecoPaciente = row['Nome endereco paciente']
    SexoPaciente = row['Sexo paciente']

    DataNascimento = row['Data nascimento']
    try:
        DataNascimento = parser.parse(DataNascimento)
    except:
        continue

    Etnia = row['Etnia']
    ParticipouEnsaioClinicoCOVID = row['Participou ensaio clinico COVID']
    DoencaPrevia = row['Doenca previa']
    CodigoMedraPrevio = row['Codigo Medra Previo (http://paho.org/esavi/ValueSet/CodigoMedDRAEnfPreviaVS)']
    OutrosCodigosPrevios = row['Outros codigos previos (http://paho.org/esavi/ValueSet/EnfermedadesPreviasCodificacionVS)']
    EventoAdversoSimNao = row['Evento adverso Sim ou Nao (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']
    AlergiaMedicamento = row['Alergia medicamento (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']
    AlergiaOutras = row['Alergia outras vacinas (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']
    DiagnosticoPrevio = row['Diagnostico previo COVID (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']
    AssintomaticoSARS = row['Assintomatico SARS (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']

    DataSintomaCOVID = row['Data sintoma COVID']
    try:
        DataSintomaCOVID = parser.parse(DataSintomaCOVID)
    except:
        print('WARN: Não foi informada uma data de sintoma de COVID')

    TipoConfirmacaoCOVID = row['Tipo confirmacao COVID']

    DataAmostraCOVID = row['Data Amostra COVID']
    try:
        DataAmostraCOVID = parser.parse(DataAmostraCOVID)
    except:
        print('WARN: Não foi informada uma data de amostra coletada de COVID')

    GestanteDuranteVacinacao = row['Gestante durante vacinacao (boolean)']
    GestanteDuranteNotificacao = row['Gestante durante notificacao (boolean)']

    DataUltimaMenstruacao = row['Data ultima menstruacao']
    try:
        DataUltimaMenstruacao = parser.parse(DataUltimaMenstruacao)
    except:
        print('WARN: Não foi informada uma data de menstruação')

    DataParto = row['Data parto']
    try:
        DataParto = parser.parse(DataParto)
    except:
        print('WARN: Não foi informada uma data de parto')

    IdadeGestacional = row['Idade gestacional']
    CodigoMonitoreoPosteriorVacuna = row['codigoMonitoreoPosteriorVacuna']
    NomeMedicamento = row['Nome medicamento']
    SistemaMedicamento = row['Sistema medicamento (URI)']
    CodigoMedicamento = row['Codigo medicamento']
    FormaFarmaceutica = row['Forma farmaceutica']
    CodigoFormaFarmaceutica = row[
        'Codigo forma farmaceutica (http://paho.org/esavi/ValueSet/FormaFarmaceuticaVS)']
    NomeViaAdministracao = row['Nome via administracao']
    CodigoViaAdministracao = row['Codigo via administracao (http://paho.org/esavi/ValueSet/ViaAdminMedicamentoVS)']
    NomeVacina = row['Nome vacina']
    SistemaVacina = row['Sistema vacina (http://paho.org/esavi/ValueSet/SistemasDeCodificacionVS)']
    IdentificadorVacina = row['Identificador vacina']
    CodigoVacina = row['Codigo vacina (http://paho.org/esavi/ValueSet/CodigoWhoVacunaVS)']
    CodigoVacinaOutro = row['Codigo vacina outro']
    NomeFabricante = row['Nome fabricante']
    CodigoFabricante = row['Codigo fabricante WHO (http://paho.org/esavi/ValueSet/CodigoWhoFabricanteVS)']
    DoseVacina = row['Dose vacina']
    Lote = row['Lote']

    DataVencimento = row['Data vencimento']
    try:
        DataVencimento = parser.parse(DataVencimento)
    except:
        print('WARN: Não foi informada uma data de vencimento do ')

    NomeDiluente = row['Nome diluente']

    DataVencimentoDiluente = row['Data vencimento diluente']
    try:
        DataVencimentoDiluente = parser.parse(DataVencimentoDiluente)
    except:
        print('WARN: Não foi informada uma data de vencimento do diluente')

    NomePostoVacinacao = row['Nome posto vacinacao']

    DataVacinacao = row['Data vacinacao']
    try:
        DataVacinacao = parser.parse(DataVacinacao)
    except:
        continue

    HoraVacinacao = row['Hora vacinacao']
    EnderecoPostoVacinacao = row['Endereco posto vacinacao (http://paho.org/esavi/ValueSet/DirOrgNotiVS)']
    EnderecoPostoVacinacao = row['Endereco posto vacinacao']
    CodigoMecanismoVerificacao = row[
        'Codigo mecanismo verificacao (http://paho.org/esavi/ValueSet/ModoVerificacionVacunaVS)']
    OutroMecanismoVerificacao = row['Outro mecanismo verificacao']

    DataReforcoVacina = row['Data reforco vacina']
    try:
        DataReforcoVacina = parser.parse(DataReforcoVacina)
    except:
        print('WARN: Não foi informada uma data de reforço da vacina')

    HoraReforcoVacina = row['Hora reforco vacina']

    NomeESAVI = row['Nome ESAVI']
    if (NomeESAVI is None):
        continue

    IdentificadorESAVI = row['Identificador ESAVI']
    CodigoESAVIMedra = row['Codigo ESAVI Medra (http://paho.org/esavi/ValueSet/EsaviMedDRAVS)']
    CodigoESAVIOutro = row['Codigo ESAVI Outro (http://paho.org/esavi/ValueSet/EsaviOtroVS)']

    DataESAVI = row['Data ESAVI']
    try:
        DataESAVI = parser.parse(DataESAVI)
    except:
        continue

    HoraESAVI = row['Hora ESAVI']
    DescricaoESAVI = row['Descricao ESAVI']
    GravidezVacinacao = row['Gravida momento ESAVI (boolean)']
    CodigoGravidesDuranteESAVI = row[
        'Codigo gravides durante ESAVI (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']

    CodigoMonitoramentoPosteriorVacinaESAVI = row['Codigo monitoramento posterior vacina ESAVI']
    CodigoTipoComplicacao = row['Codigo tipo complicacao']
    NomeComplicacao = row['Nome Complicacao']
    CodigoMedraComplicacao = row['Codigo medra complicacao']
    OutrosCodigosComplicacao = row['Outros codigos complicacao']

    GravidadeESAVI = row['Gravidade ESAVI']
    if (math.isnan(GravidadeESAVI)):
        GravidadeESAVI = False
    else:
        GRavidadeESAVI = bool(GravidadeESAVI)

    Gravidademorte = row['Gravidade morte']
    if (math.isnan(Gravidademorte)):
        Gravidademorte = False
    else:
        Gravidademorte = bool(Gravidademorte)

    GravidaderiscoVida = row['Gravidade risco vida']
    if (math.isnan(GravidaderiscoVida)):
        GravidaderiscoVida = False
    else:
        GravidaderiscoVida = bool(GravidaderiscoVida)

    Gravidadeincapacidade = row['Gravidade incapacidade']
    if (math.isnan(Gravidadeincapacidade)):
        Gravidadeincapacidade = False
    else:
        Gravidadeincapacidade = bool(Gravidadeincapacidade)

    Gravidadehospitalizacao = row['Gravidade hospitalizacao']
    if (math.isnan(Gravidadehospitalizacao)):
        Gravidadehospitalizacao = False
    else:
        Gravidadehospitalizacao = bool(Gravidadehospitalizacao)

    GravidadeanomaliaCongenita = row['Gravidade anomalia congenita']
    if (math.isnan(GravidadeanomaliaCongenita)):
        GravidadeanomaliaCongenita = False
    else:
        GravidadeanomaliaCongenita = bool(GravidadeanomaliaCongenita)

    Gravidadeaborto = row['Gravidade aborto']
    if (math.isnan(Gravidadeaborto)):
        Gravidadeaborto = False
    else:
        Gravidadeaborto = bool(Gravidadeaborto)

    GravidademorteFetal = row['Gravidade morte fetal']
    if (math.isnan(GravidademorteFetal)):
        GravidademorteFetal = False
    else:
        GravidademorteFetal = bool(GravidademorteFetal)

    OutroseventosImportantes = row['Outros eventos importantes']
    if (math.isnan(OutroseventosImportantes)):
        OutroseventosImportantes = False
    else:
        OutroseventosImportantes = bool(OutroseventosImportantes)

    OutroseventosImportantesTX = row['Outros eventos importantes TX']

    CodigodesfechoDESAVI = row['Codigo desfecho DESAVI']
    if (math.isnan(CodigodesfechoDESAVI)):
        print('WARN: Não foi informado um código de desfecho')
        continue

    Datamorte = row['Data morte']
    try:
        Datamorte = parser.parse(Datamorte)
    except:
        print('WARN: Não foi informada uma data de morte')

    autopsia = row['autopsia']

    DatanotificacaoMorte = row['Data notificacao morte']
    try:
        DatanotificacaoMorte = parser.parse(DatanotificacaoMorte)
    except:
        print('WARN: Não foi informada uma data de notifiacao de morte')

    DatanotificacaoMorteFetal = row['Data notificacao morte fetal']
    try:
        DatanotificacaoMorteFetal = parser.parse(DatanotificacaoMorteFetal)
    except:
        print('WARN: Não foi informada uma data de notificacao de morte fetal')

    Autopsiafetal = row['Autopsia fetal']
    Comentarios = row['Comentarios']

    DatainicioInvestigacao = row['Data inicio investigacao']
    try:
        DatainicioInvestigacao = parser.parse(DatainicioInvestigacao)
    except:
        print('WARN: Não foi informada uma data de inicio de investigacao')

    DatacausalidadeESAVI = row['Data causalidade ESAVI']
    try:
        DatacausalidadeESAVI = parser.parse(DatacausalidadeESAVI)
    except:
        print('WARN: Não foi informada uma data de casualidade da ESAVI')

    SistemaclassificacaoCausalidade = row['Sistema classificacao causalidade']
    OutrosistemaClassificacaoCausalidade = row['Outro sistema classificacao causalidade']
    ClassificacaocausaESAVI = row['Classificacao causa ESAVI']
    Classificacaocausalidade = row['Classificacao causalidade']
    ClassificacaoCausalidadeNaranjo = row['Classificacao causalidade Naranjo']
    ReferenciaIdentificadorVacina = row['Referencia identificador vacina']

    # El sistema de origen no sabe generar automaticamente
    # UUID para numeros de caso o identificadores de paciente
    # Se los generamos aqui
    numeroCaso = str(uuid.uuid5(uuid.NAMESPACE_URL,
                     "http://ops.org/esavi/"+PaisOrigem+"/"+str(NumeroCaso)))
    identificadorPaciente = str(uuid.uuid5(
        uuid.NAMESPACE_URL,  "http://ops.org/esavi/"+PaisOrigem+"/paciente/"+str(IdPaciente)))

    # Armamos el QuestionnaireResponse a partir de los datos
    # con los que contamos
    if (GestanteDuranteVacinacao):
        if(math.isnan(CodigoGravidesDuranteESAVI)):
            continue

        QR = {
            "resourceType": "QuestionnaireResponse",
            "meta": {
                "profile": [
                    "https://paho.org/fhir/esavi/StructureDefinition/ESAVIQuestionnaireResponse"
                ]
            },
            "status": "completed",
            "authored": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "identifier": {
                "system": "http://ops.org/esavi/BRA",
                "value": numeroCaso
            },
            "questionnaire": "https://paho.org/fhir/esavi/Questionnaire/CuestionarioESAVI",
            "text": {
                "status": "generated",
                "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">ID DE RESPOSTA A QUESTIONÁRIO "+numeroCaso+" / BRA</div>"
            },
            "item": [
                {
                    "linkId": "datosNotificacionGeneral",
                    "item": [
                        {
                            "linkId": "datosNotificacion",
                            "item": [
                                {
                                    "linkId": "paisOrigen-Reg",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "urn:iso:std:iso:3166",
                                                "code": str(PaisOrigem)
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreOrganizacionNotificadora",
                                    "answer": [
                                        {
                                            "valueString": NomeOrganizacaoNotificadora
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreDireccionOrganizacion",
                                    "answer": [
                                        {
                                            "valueString": NomeEnderecoOrganizacao
                                        }
                                    ]
                                },
                                {
                                    "linkId": "codigoProfesionNotificador",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ProfesionalNotificadorCS",
                                                "code": str(int(CodigoProfissionalNotificador))
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "fechas",
                            "item": [
                                {
                                    "linkId": "fechaConsulta",
                                    "text": "Fecha de la primera consulta al servicio de salud por causa del ESAVI",
                                    "answer": [
                                        {
                                            "valueDate": DataConsulta.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaNotificacion",
                                    "answer": [
                                        {
                                            "valueDate": DataNotificacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaLlenadoFicha",
                                    "answer": [
                                        {
                                            "valueDate": DataPreenchimento.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaRepoNacional",
                                    "answer": [
                                        {
                                            "valueDate": DataPreenchimentoBaseNacional.date().isoformat()
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "datosIdVacunado",
                    "item": [
                        {
                            "linkId": "datosPaciente",
                            "item": [
                                {
                                    "linkId": "numeroCaso",
                                    "answer": [
                                        {
                                            "valueString": numeroCaso
                                        }
                                    ]
                                },
                                {
                                    "linkId": "idPaciente",
                                    "answer": [
                                        {
                                            "valueString": identificadorPaciente
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreResidenciaHabitual",
                                    "answer": [
                                        {
                                            "valueString": NomeEnderecoPaciente
                                        }
                                    ]
                                },
                                {
                                    "linkId": "sexoPaciente",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "http://hl7.org/fhir/administrative-gender",
                                                "code": str(SexoPaciente)
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaNacimiento",
                                    "answer": [
                                        {
                                            "valueDate": DataNascimento.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "etnia",
                                    "answer": [
                                        {
                                            "valueString": str(Etnia)
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "antecedentesMedicos",
                    "item": [
                        {
                            "linkId": "pacienteEmbarazada",
                            "item": [
                                {
                                    "linkId": "embarazadaMomentoVacuna",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GestanteDuranteVacinacao)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "embarazadaMomentoESAVI",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GestanteDuranteNotificacao)
                                        }
                                    ]
                                },

                                {
                                    "linkId": "fechaUltimaMenstruacion",
                                    "answer": [
                                        {
                                            "valueDate": DataUltimaMenstruacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaProbableParto",
                                    "answer": [
                                        {
                                            "valueDate": DataParto.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "edadGestacional",
                                    "answer": [
                                        {
                                            "valueInteger": int(IdadeGestacional)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "codigoMonitoreoPosteriorVacuna",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/RespuestaSiNoNosabeCS",
                                                "code": str(int(CodigoMonitoreoPosteriorVacuna))
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "antecedentesFarmacosVacunas",
                    "item": [
                        {
                            "linkId": "datosVacunas",
                            "item": [
                                {
                                    "linkId": "nombreVacuna",
                                    "answer": [
                                        {
                                            "valueString": NomeVacina
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreNormalizadoVacuna",
                                    "answer": [
                                        {
                                            "valueString": NomeVacina
                                        }
                                    ]
                                },
                                {
                                    "linkId": "identificadorVacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(IdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreFabricante",
                                    "answer": [
                                        {
                                            "valueString": NomeFabricante
                                        }
                                    ]
                                },
                                {
                                    "linkId": "numeroDosisVacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(DoseVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "numeroLote",
                                    "answer": [
                                        {
                                            "valueString": Lote
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "datosVacunacion",
                            "item": [
                                {
                                    "linkId": "nombreVacunatorio",
                                    "answer": [
                                        {
                                            "valueString": NomePostoVacinacao
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaVacunacion",
                                    "answer": [
                                        {
                                            "valueDate": DataVacinacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreDireccionVacunatorio",
                                    "answer": [
                                        {
                                            "valueString": EnderecoPostoVacinacao
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "registroESAVI",
                    "item": [
                        {
                            "linkId": "datosESAVI",
                            "item": [
                                {
                                    "linkId": "nombreESAVI",
                                    "text": "Nombre del ESAVI",
                                    "answer": [
                                        {
                                            "valueString": NomeESAVI
                                        }
                                    ]
                                },
                                {
                                    "linkId": "IdentificadorESAVI",
                                    "answer": [
                                        {
                                            "valueInteger": int(IdentificadorESAVI)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaESAVI",
                                    "answer": [
                                        {
                                            "valueDate": DataESAVI.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "descripcionESAVI",
                                    "answer": [
                                        {
                                            "valueString": DescricaoESAVI
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "antecedentesEmbarazoESAVI",
                            "item": [
                                {
                                    "linkId": "codigoEmbarazoDuranteESAVI",
                                    "text": "Código consulta sobre la condición de embarazo al momento del ESAVI",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS",
                                                "code": str(int(CodigoGravidesDuranteESAVI))
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaUltimaMenstruacionESAVI",
                                    "text": "Fecha de la última menstruación de la Paciente",
                                    "answer": [
                                        {
                                            "valueDate": DataUltimaMenstruacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaPartoESAVI",
                                    "text": "Fecha del parto, o fecha probable del parto (calculada)",
                                    "answer": [
                                        {
                                            "valueDate": DataESAVI.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "codigoMonitoreoPosteriorVacunaESAVI",
                                    "text": "Código consulta sobre si se monitoreó paciente una vez vacunado",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS",
                                                "code": str(int(CodigoGravidesDuranteESAVI))
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "complicacionesEmbarazoESAVI",
                                    "text": "Complicación del embarazo que se sospecha estuvo relacionada con la administración de la vacuna",
                                    "item": [
                                        {
                                            "linkId": "codigoTipoComplicacionESAVI",
                                            "text": "Código tipo complicacion del embarazo durante el ESAVI",
                                            "answer": [
                                                {
                                                    "valueCoding": {
                                                        "system": "http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS",
                                                        "code": str(int(CodigoTipoComplicacao))
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "linkId": "nombreComplicacionEmbarazoESAVI",
                                            "text": "Descripción de la Complicación durante el ESAVI",
                                            "answer": [
                                                {
                                                    "valueString": NomeComplicacao
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "gravedadESAVI",
                            "text": "Determinación del estado de gravedad del ESAVI",
                            "item": [
                                {
                                    "linkId": "tipoGravedad",
                                    "text": "¿ESAVI Grave?",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GravidadeESAVI)
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "desenlaceESAVI",
                            "text": "Desenlace ESAVI",
                            "item": [
                                {
                                    "linkId": "codDesenlaceESAVI",
                                    "text": "Código Desenlace ESAVI",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ClasificacionDesenlaceCS",
                                                "code": str(int(CodigodesfechoDESAVI))
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "causalidadESAVI",
                            "text": "Información sobre la clasificación de causalidad",
                            "item": [
                                {
                                    "linkId": "fechaCausalidadESAVI",
                                    "text": "Fecha de clasificación final del caso",
                                    "answer": [
                                        {
                                            "valueDate": DatacausalidadeESAVI.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "sistemaClasfcausalidad",
                                    "text": "Método de clasificación de causalidad",
                                    "answer": [
                                        {
                                            "valueString": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/SistemaClasfCausalidadCS",
                                                "code": "Naranjo"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "clasificacionDeCausalidadNaranjo",
                                    "text": "Clasificación de causalidad según la metodología Naranjo",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ClasificacionDesenlaceNaranjoCS",
                                                "code": '0'+str(int(ClassificacaoCausalidadeNaranjo))
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "referenciaIdentificadorVacuna",
                                    "text": "Identificador correlativo de la vacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(ReferenciaIdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "referenciaIdentificadorESAVI",
                                    "text": "Identificador correlativo de la vacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(ReferenciaIdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "embarazoDuranteESAVI",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GravidezVacinacao)
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    else:
        QR = {
            "resourceType": "QuestionnaireResponse",
            "meta": {
                "profile": [
                    "https://paho.org/fhir/esavi/StructureDefinition/ESAVIQuestionnaireResponse"
                ]
            },
            "status": "completed",
            "authored": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "identifier": {
                "system": "http://ops.org/esavi/BRA",
                "value": numeroCaso
            },
            "questionnaire": "https://paho.org/fhir/esavi/Questionnaire/CuestionarioESAVI",
            "text": {
                "status": "generated",
                "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">ID DE RESPOSTA A QUESTIONÁRIO "+numeroCaso+" / BRA</div>"
            },
            "item": [
                {
                    "linkId": "datosNotificacionGeneral",
                    "item": [
                        {
                            "linkId": "datosNotificacion",
                            "item": [
                                {
                                    "linkId": "paisOrigen-Reg",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "urn:iso:std:iso:3166",
                                                "code": str(PaisOrigem)
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreOrganizacionNotificadora",
                                    "answer": [
                                        {
                                            "valueString": NomeOrganizacaoNotificadora
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreDireccionOrganizacion",
                                    "answer": [
                                        {
                                            "valueString": NomeEnderecoOrganizacao
                                        }
                                    ]
                                },
                                {
                                    "linkId": "codigoProfesionNotificador",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ProfesionalNotificadorCS",
                                                "code": str(int(CodigoProfissionalNotificador))
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "fechas",
                            "item": [
                                {
                                    "linkId": "fechaConsulta",
                                    "text": "Fecha de la primera consulta al servicio de salud por causa del ESAVI",
                                    "answer": [
                                        {
                                            "valueDate": DataConsulta.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaNotificacion",
                                    "answer": [
                                        {
                                            "valueDate": DataNotificacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaLlenadoFicha",
                                    "answer": [
                                        {
                                            "valueDate": DataPreenchimento.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaRepoNacional",
                                    "answer": [
                                        {
                                            "valueDate": DataPreenchimentoBaseNacional.date().isoformat()
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "datosIdVacunado",
                    "item": [
                        {
                            "linkId": "datosPaciente",
                            "item": [
                                {
                                    "linkId": "numeroCaso",
                                    "answer": [
                                        {
                                            "valueString": numeroCaso
                                        }
                                    ]
                                },
                                {
                                    "linkId": "idPaciente",
                                    "answer": [
                                        {
                                            "valueString": identificadorPaciente
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreResidenciaHabitual",
                                    "answer": [
                                        {
                                            "valueString": NomeEnderecoPaciente
                                        }
                                    ]
                                },
                                {
                                    "linkId": "sexoPaciente",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "http://hl7.org/fhir/administrative-gender",
                                                "code": str(SexoPaciente)
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaNacimiento",
                                    "answer": [
                                        {
                                            "valueDate": DataNascimento.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "etnia",
                                    "answer": [
                                        {
                                            "valueString": str(Etnia)
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "antecedentesFarmacosVacunas",
                    "item": [
                        {
                            "linkId": "datosVacunas",
                            "item": [
                                {
                                    "linkId": "nombreVacuna",
                                    "answer": [
                                        {
                                            "valueString": NomeVacina
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreNormalizadoVacuna",
                                    "answer": [
                                        {
                                            "valueString": NomeVacina
                                        }
                                    ]
                                },
                                {
                                    "linkId": "identificadorVacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(IdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreFabricante",
                                    "answer": [
                                        {
                                            "valueString": NomeFabricante
                                        }
                                    ]
                                },
                                {
                                    "linkId": "numeroDosisVacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(DoseVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "numeroLote",
                                    "answer": [
                                        {
                                            "valueString": Lote
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "datosVacunacion",
                            "item": [
                                {
                                    "linkId": "nombreVacunatorio",
                                    "answer": [
                                        {
                                            "valueString": NomePostoVacinacao
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaVacunacion",
                                    "answer": [
                                        {
                                            "valueDate": DataVacinacao.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "nombreDireccionVacunatorio",
                                    "answer": [
                                        {
                                            "valueString": EnderecoPostoVacinacao
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "linkId": "registroESAVI",
                    "item": [
                        {
                            "linkId": "datosESAVI",
                            "item": [
                                {
                                    "linkId": "nombreESAVI",
                                    "text": "Nombre del ESAVI",
                                    "answer": [
                                        {
                                            "valueString": NomeESAVI
                                        }
                                    ]
                                },
                                {
                                    "linkId": "IdentificadorESAVI",
                                    "answer": [
                                        {
                                            "valueInteger": int(IdentificadorESAVI)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "fechaESAVI",
                                    "answer": [
                                        {
                                            "valueDate": DataESAVI.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "descripcionESAVI",
                                    "answer": [
                                        {
                                            "valueString": DescricaoESAVI
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "gravedadESAVI",
                            "text": "Determinación del estado de gravedad del ESAVI",
                            "item": [
                                {
                                    "linkId": "tipoGravedad",
                                    "text": "¿ESAVI Grave?",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GravidadeESAVI)
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "desenlaceESAVI",
                            "text": "Desenlace ESAVI",
                            "item": [
                                {
                                    "linkId": "codDesenlaceESAVI",
                                    "text": "Código Desenlace ESAVI",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ClasificacionDesenlaceCS",
                                                "code": str(int(CodigodesfechoDESAVI))
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "linkId": "causalidadESAVI",
                            "text": "Información sobre la clasificación de causalidad",
                            "item": [
                                {
                                    "linkId": "fechaCausalidadESAVI",
                                    "text": "Fecha de clasificación final del caso",
                                    "answer": [
                                        {
                                            "valueDate": DatacausalidadeESAVI.date().isoformat()
                                        }
                                    ]
                                },
                                {
                                    "linkId": "sistemaClasfcausalidad",
                                    "text": "Método de clasificación de causalidad",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/SistemaClasfCausalidadCS",
                                                "code": SistemaclassificacaoCausalidade
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "clasificacionDeCausalidadNaranjo",
                                    "text": "Clasificación de causalidad según la metodología Naranjo",
                                    "answer": [
                                        {
                                            "valueCoding": {
                                                "system": "https://paho.org/fhir/esavi/CodeSystem/ClasificacionDesenlaceNaranjoCS",
                                                "code": '0'+str(int(ClassificacaoCausalidadeNaranjo))
                                            }
                                        }
                                    ]
                                },
                                {
                                    "linkId": "referenciaIdentificadorVacuna",
                                    "answer": [
                                        {
                                            "valueInteger": int(ReferenciaIdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "referenciaIdentificadorESAVI",
                                    "answer": [
                                        {
                                            "valueInteger": int(ReferenciaIdentificadorVacina)
                                        }
                                    ]
                                },
                                {
                                    "linkId": "embarazoDuranteESAVI",
                                    "answer": [
                                        {
                                            "valueBoolean": bool(GravidezVacinacao)
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    # Validamos nuestro QuestionnaireResponse
    url = 'http://ec2-54-236-53-161.compute-1.amazonaws.com:8080/fhir/QuestionnaireResponse'
    MyValidateUrl = url + '/$validate'
    response = requests.post(MyValidateUrl, json=QR)

    # Procesamos Respuesta
    json_response = response.json()

    # Mensaje de Error si Hubo Error
    if response.status_code != 200:
        print("ERROR: " + json_response.get('issue')[0].get('diagnostics'))

    # Enviamos Notificacion al Servidor si todo estuvo OK
    if response.status_code == 200:
        response = requests.post(url, json=QR)
        json_response = response.json()
        print('INFO: ' + json_response.get('id') + ' enviado com sucesso')
