
# side by side

arquivo = open("dog_list.txt")
print(arquivo.readlines())
arquivo.close()

#one below another

print('\n\t\t Openning the list.')
arquivo = open('dog_list.txt', 'r')
linha = '.'
while linha != "":
  linha = arquivo.readline()
  print(linha)
print('\n\t\t End of the list')
arquivo.close()

#if I want to delete the list
"""

import os
os.remove('dog_list.txt')

"""

