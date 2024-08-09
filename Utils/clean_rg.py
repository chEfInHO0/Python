
def clean_rg(rg:str):
    return rg.replace('.','').replace('-','')


def seven_digits_rg(rg:str):
    "ex: 527 813 1"
    rg = list(rg)
    rg_format = list()
    group = list()
    last_digit = rg.pop()
    count = 1
    for digit in rg:
        group.append(digit)
        if count % 3 == 0:
            rg_format.append(group)
            group = list()
        count += 1
    rg_f = ''
    for group in rg_format:
        rg_f += ''.join(group)+'.'
    rg_f = list(rg_f)
    rg_f[-1] = '-'
    rg_f.append(last_digit)
    rg_f = ''.join(rg_f)
    print(rg_f)

        
def eight_digits_rg(rg:str):
    "4 527 813 1"
    #TODO Alterar lógica para 8 dígitos
    rg = list(rg)
    rg_format = list()
    group = list()
    last_digit = rg.pop()
    count = 1
    one_digit_count = 0
    for digit in rg:
        group.append(digit)
        if count % 3 == 0:
            rg_format.append(group)
            group = list()
        if len(group) == 1 and one_digit_count == 0:
            rg_format.append(group)
            group = list()
            one_digit_count += 1
            count = 0
        count += 1
    rg_f = ''
    for group in rg_format:
        rg_f += ''.join(group)+'.'
    rg_f = list(rg_f)
    rg_f[-1] = '-'
    rg_f.append(last_digit)
    rg_f = ''.join(rg_f)
    print(rg_f)

  
def nine_digits_rg(rg:str):
    "45 527 813 1"
    #TODO Alterar lógica para 9 dígitos
    rg = list(rg)
    rg_format = list()
    group = list()
    last_digit = rg.pop()
    count = 1
    two_digit_count = 0
    for digit in rg:
        group.append(digit)
        if count % 3 == 0:
            rg_format.append(group)
            group = list()
        if len(group) == 2 and two_digit_count == 0:
            rg_format.append(group)
            group = list()
            two_digit_count += 1
            count = 0
        count += 1
    rg_f = ''
    for group in rg_format:
        rg_f += ''.join(group)+'.'
    rg_f = list(rg_f)
    rg_f[-1] = '-'
    rg_f.append(last_digit)
    rg_f = ''.join(rg_f)
    print(rg_f)


def format_rg(rg:str):
    match len(rg):
        case 7:
            seven_digits_rg(rg)
        case 8:
            eight_digits_rg(rg)
        case 9:
            nine_digits_rg(rg)
        case _:
            print('Não foi possivel realizar a ação')
        

def get_rg():
    invalidRg = True
    while invalidRg:
        try:
            rg = str(input('Digite o RG: ') or '')
            if len(rg) < 7:
                raise(ValueError)
            for digit in rg:
                int(digit)
            invalidRg = False
            format_rg(rg)
        except ValueError:
            print('O RG deve conter ao menos 7 dígitos numéricos')
            invalidRg = True

get_rg()