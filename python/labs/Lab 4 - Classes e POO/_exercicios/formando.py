from datetime import date


form2 = {    # um formando
    'nome': 'Alberto Alves Almeida',
    'data_nascimento': date(2015, 10, 20),
    'morada': 'Av. Liberdade N. 13 Lisboa', 
    'modulos_inscritos': {
        'tecnicos': ['Linux', 'SQL', 'Windows Server'],
        'gerais': ['Inglês', 'Português']
    }
}


def cria_formando(nome, data_nascimento, morada, modulos_tecnicos, modulos_gerais):
    return {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'morada': morada,
        'modulos': {
            'tecnicos': modulos_tecnicos,
            'gerais': modulos_gerais
        }
    }


def nome(formando):
    return formando['nome']


def apelidos(formando):
    return ' '.join(formando['nome'].split()[1:])


def data_nascimento(formando):
    return formando['data_nascimento']


def modulos_inscritos(formando):
    return formando['modulos']['tecnicos'] + formando['modulos']['gerais']


def morada(formando):
    return formando['morada']


def actualiza_morada(formando, nova_morada):
    formando['morada'] = nova_morada


#(nome, data_nascimento, morada, modulos_tecnicos, modulos_gerais):
form1 = cria_formando(
    'Alberto Silva', 
    date(1994, 10, 27),
    'Praça da Alegria, Lisboa',
    ['Linux', 'C++', 'Windows Server'],
    ['Inglês', 'Português'],
)

print(nome(form1))
actualiza_morada(form1, 'Av. Liberdade, num. 78')

