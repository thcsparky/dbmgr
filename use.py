from class2 import dbmgr
import os


def main():
    a = input('load or save?\n').strip()
    if a != 'load' and a != 'save':
        print('welp\n')
    if a == 'save':
        dictsparky = {'0': 'hey', '1': 'f', '2': 'you'}
        dictempty = {}
        itemz = dbmgr(os.getcwd() + '/file.json', dictempty)
        itemz.dictContainer = dictsparky
        print(itemz.dictContainer)
        itemz.saveAll()
    if a == 'load':
        dictempty = {}
        itemz = dbmgr(os.getcwd() + '/file.json', dictempty)
        dictsparky = itemz.dictContainer
        print(dictsparky)
        print('reloading..\n')
        itemz.reload()
        print(itemz.dictContainer)
if __name__ == "__main__":
    main()
