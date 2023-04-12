import pandas
import requests
import uuid
import datetime
import json

# Importamos el excel a un DataFrame
df = pandas.read_excel('Questionnaire.xlsx', sheet_name='Questionário')

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
    DataNotificacao = row['Data notificação']
    DataPreenchimento = row['Data preenchimento']
    DataPreenchimentoBaseNacional = row['Data preenchimento base nacional']
    NumeroCaso = row['Numero caso']
    IdPaciente = row['Id paciente']
    EnderecoPaciente = row['Endereco paciente (http://paho.org/esavi/ValueSet/DirOrgNotiVS)']
    NomeEnderecoPaciente = row['Nome endereco paciente']
    SexoPaciente = row['Sexo paciente']
    DataNascimento = row['Data nascimento']
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
    TipoConfirmacaoCOVID = row['Tipo confirmacao COVID']
    DataAmostraCOVID = row['Data Amostra COVID']
    GestanteDuranteVacinacao = row['Gestante durante vacinacao (boolean)']
    GestanteDuranteNotificacao = row['Gestante durante notificacao (boolean)']
    DataUltimaMenstruacao = row['Data ultima menstruacao']
    DataParto = row['Data parto']
    IdadeGestacional = row['Idade gestacional']
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
    NomeDiluente = row['Nome diluente']
    DataVencimentoDiluente = row['Data vencimento diluente']
    NomePostoVacinacao = row['Nome posto vacinacao']
    DataVacinacao = row['Data vacinacao']
    HoraVacinacao = row['Hora vacinacao']
    EnderecoPostoVacinacao = row['Endereco posto vacinacao (http://paho.org/esavi/ValueSet/DirOrgNotiVS)']
    EnderecoPostoVacinacao = row['Endereco posto vacinacao']
    CodigoMecanismoVerificacao = row[
        'Codigo mecanismo verificacao (http://paho.org/esavi/ValueSet/ModoVerificacionVacunaVS)']
    OutroMecanismoVerificacao = row['Outro mecanismo verificacao']
    DataReforcoVacina = row['Data reforco vacina']
    HoraReforcoVacina = row['Hora reforco vacina']
    NomeESAVI = row['Nome ESAVI']
    IdentificadorESAVI = row['Identificador ESAVI']
    CodigoESAVIMedra = row['Codigo ESAVI Medra (http://paho.org/esavi/ValueSet/EsaviMedDRAVS)']
    CodigoESAVIOutro = row['Codigo ESAVI Outro (http://paho.org/esavi/ValueSet/EsaviOtroVS)']
    DataESAVI = row['Data ESAVI']
    HoraESAVI = row['Hora ESAVI']
    DescricaoESAVI = row['Descricao ESAVI']
    GravidaMomentoESAVI = row['Gravida momento ESAVI (boolean)']
    CodigoGravidesDuranteESAVI = row[
        'Codigo gravides durante ESAVI (http://paho.org/esavi/ValueSet/RespuestaSiNoNosabeVS)']
    DataUltimaMenstruacao = row['Data ultima menstruacao']
    DataParto = row['Data parto']
    CodigoMonitoramentoPosteriorVacinaESAVI = row['Codigo monitoramento posterior vacina ESAVI']
    CodigoTipoComplicacao = row['Codigo tipo complicacao']
    NomeComplicacao = row['Nome Complicacao']
    CodigoMedraComplicacao = row['Codigo medra complicacao']
    OutrosCodigosComplicacao = row['Outros codigos complicacao']
    GravidadeESAVI = row['Gravidade ESAVI']
    Gravidademorte = row['Gravidade morte']
    GravidaderiscoVida = row['Gravidade risco vida']
    Gravidadeincapacidade = row['Gravidade incapacidade']
    Gravidadehospitalizacao = row['Gravidade hospitalizacao']
    GravidadeanomaliaCongenita = row['Gravidade anomalia congenita']
    Gravidadeaborto = row['Gravidade aborto']
    GravidademorteFetal = row['Gravidade morte fetal']
    OutroseventosImportantes = row['Outros eventos importantes']
    OutroseventosImportantesTX = row['Outros eventos importantes TX']
    CodigodesfechoDESAVI = row['Codigo desfecho DESAVI']
    Datamorte = row['Data morte']
    autopsia = row['autopsia']
    DatanotificacaoMorte = row['Data notificacao morte']
    DatanotificacaoMorteFetal = row['Data notificacao morte fetal']
    Autopsiafetal = row['Autopsia fetal']
    Comentarios = row['Comentarios']
    DatainicioInvestigacao = row['Data inicio investigacao']
    DatacausalidadeESAVI = row['Data causalidade ESAVI']
    SistemaclassificacaoCausalidade = row['Sistema classificacao causalidade']
    OutrosistemaClassificacaoCausalidade = row['Outro sistema classificacao causalidade']
    ClassificacaocausaESAVI = row['Classificacao causa ESAVI']
    Classificacaocausalidade = row['Classificacao causalidade']
    ClassificacaocausalidadeWHOUMC = row['Classificacao causalidade WHOUMC']
    # El sistema de origen no sabe generar automaticamente
    # UUID para numeros de caso o identificadores de paciente
    # Se los generamos aqui
    numeroCaso = str(uuid.uuid5(uuid.NAMESPACE_URL,
                     "http://ops.org/esavi/"+PaisOrigem+"/"+str(NumeroCaso)))
    identificadorPaciente = str(uuid.uuid5(
        uuid.NAMESPACE_URL,  "http://ops.org/esavi/"+PaisOrigem+"/paciente/"+str(IdPaciente)))

    # Armamos el QuestionnaireResponse a partir de los datos
    # con los que contamos
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
                        "linkId": "antecedentesEnfermedadesPrevias",
                        "item": [
                            {
                                "linkId": "descripcionEnfPrevia",
                                "answer": [
                                    {
                                        "valueString": DoencaPrevia
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "linkId": "antecedentesSarsCov2",
                        "item": [
                            {
                                "linkId": "diagnosticoprevioSarsCov2",
                                "answer": [
                                    {
                                        "valueCoding": {
                                            "system": "https://paho.org/fhir/esavi/CodeSystem/RespuestaSiNoNosabeCS",
                                            "code": str(int(DiagnosticoPrevio))
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
                            },
                            {
                                "linkId": "fechaVencimientoVacuna",
                                "answer": [
                                    {
                                        "valueDate": DataVencimento.date().isoformat()
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
                            },
                            {
                                "linkId": "gravMuerte",
                                "text": "Muerte",
                                "answer": [
                                    {
                                        "valueBoolean": bool(Gravidademorte)
                                    }
                                ]
                            },
                            {
                                "linkId": "gravRiesgoVida",
                                "text": "Amenaza la vida al momento de la detección del ESAVI",
                                "answer": [
                                    {
                                        "valueBoolean": bool(GravidaderiscoVida)
                                    }
                                ]
                            },
                            {
                                "linkId": "gravDiscapacidad",
                                "text": "Genera discapacidad severa o permanente al momento de la detección",
                                "answer": [
                                    {
                                        "valueBoolean": bool(Gravidadeincapacidade)
                                    }
                                ]
                            },
                            {
                                "linkId": "gravHospitalizacion",
                                "text": "Hospitalización o prolongación de la misma",
                                "answer": [
                                    {
                                        "valueBoolean": bool(Gravidadehospitalizacao)
                                    }
                                ]
                            },
                            {
                                "linkId": "gravAnomaliaCongenita",
                                "text": "Anomalía congénita",
                                "answer": [
                                    {
                                        "valueBoolean": bool(GravidadeanomaliaCongenita)
                                    }
                                ]
                            },
                            {
                                "linkId": "otrosEventosImportantes",
                                "text": "Otros Eventos considerados Médicamente Importantes",
                                "answer": [
                                    {
                                        "valueBoolean": bool(OutroseventosImportantes)
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
                    }
                ]
            }
        ]
    }
    # Validamos nuestro QuestionnaireResponse
    print(json.dumps(QR))
    url = 'http://ec2-54-236-53-161.compute-1.amazonaws.com:8080/fhir/QuestionnaireResponse'
    MyValidateUrl = url + '/$validate'
    print('Validando...@'+MyValidateUrl)
    response = requests.post(MyValidateUrl, json=QR)

    # Procesamos Respuesta
    json_response = response.json()

    # Mensaje de Error si Hubo Error
    if response.status_code != 200:
        print("Error")
        print(response.status_code)
        print(json_response)

    # Enviamos Notificacion al Servidor si todo estuvo OK
    if response.status_code == 200:
        response = requests.post(url, json=QR)
        json_response = response.json()
        print("status")
        print(response.status_code)
        print(json_response)
