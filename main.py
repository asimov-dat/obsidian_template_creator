import sys
import os
import template_creator

path = '/home/dat/obsidian/brain/Planing_Systems/2022/March/'
num = 0

while num := 4:
    template_creator.menu()
    num = int(input('option: '))
    template_creator.menu_option(num, path)

