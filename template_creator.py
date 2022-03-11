from datetime import date
import os

diaria = '/home/dat/obsidian/brain/Planing_Systems/2022/t_diaria_2022.md'
domingo = '/home/dat/obsidian/brain/Planing_Systems/2022/t_domingos_2022.md'
sabados = '/home/dat/obsidian/brain/Planing_Systems/2022/t_sabados_2022.md'

def hourwriter():
    objetivo = date(2022, 8, 1)
    hoy = date.today()
    result = objetivo - hoy
    return str(result.days)

def check_existance(file):
    if os.path.exists(file):
        estado = True
        return estado

def read_file(dia):
    with open(dia) as template:
        text = template.read()
        number = hourwriter()
        ntext = text.replace('157', number, 1)
        return ntext

def create_file(text, name):
    with open(name, 'w') as file:
        file.write(text)
        print('file created succesfully')

def create_template(ttype, name):
    ''' debe recibir name como path completo '''
    if ttype == 1:
        if not check_existance(name):
            text = read_file(diaria)
            create_file(text, name)
        else:
            print('file already exists')
    elif ttype == 2:
        if not check_existance(name):
            text = read_file(sabados)
            create_file(text, name)
        else:
            print('file already exists')
    elif ttype == 3:
        if not check_existance(name):
            text = read_file(domingo)
            create_file(text, name)
        else:
            print('file already exists')
    elif ttype == 4:
        print('good bay')
        exit()

def template_menu():
    print('----------------------')
    print('| 1 - semanal        |')
    print('| 2 - sabados        |')
    print('| 3 - domingos       |')
    print('----------------------')


def menu():
    print('----------------------')
    print('| 1 - create template|')
    print('| 2 - check tasks    |')
    print('| 3 - upload tasks   |')
    print('----------------------')

def menu_option(num, path):
    if num == 1:
        template_menu()
        template = int(input('platilla: '))
        dia = str(input('dia: '))
        mes = str(input('mes: '))
        name = f'{path}{dia}_{mes}_2022.md'
        create_template(template, name)
    elif num == 2:
        print('coming soon')
    elif num == 3:
        print('coming soon')
    elif num == 4:
        print('good bay')
        exit()

if __name__  == '__main__':
    path = '/home/dat/obsidian/brain/Planing_Systems/2022/March/'
    menu()
    num = int(input('option: '))
    menu_option(num, path)


