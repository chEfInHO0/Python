def clean_cpf(cpf:str):
    return cpf.replace('.','').replace('-','')


def format_cpf(cpf:str):
    """
    Formatação visual para cpf
    """
    cpf_formated = list()
    formated = list(cpf)
    final_digit2 = formated.pop() # Armazena o ultimo digito do cpf
    final_digit1 = formated.pop() # Armazena o penultimo digito do cpf
    count = 1
    group = list()
    for number in formated:    # Logica para o agrupamento dos numeros
        group.append(number)
        if count % 3 == 0:
            cpf_formated.append(group) # A cada 3 digitos, os agrupamos e depois reiniciamos os valores da lista
            group = list()
        count += 1
    f = ''
    for group in cpf_formated:
        f += ''.join(group)+'.'
    f = list(f)
    f[-1] = '-'
    f.append(final_digit1)
    f.append(final_digit2)
    return ''.join(f)


def get_cpf():    
    loop = True
    while loop:
        try:
            cpf = str(input('Digite seu CPF : ') or '').strip()
            cpf = clean_cpf(cpf)
            assert len(cpf) == 11
            print(f'CPF digitado : {cpf}')
            return cpf
        except AssertionError:
            print('CPF deve conter 11 digitos')
            loop = True


get_cpf()