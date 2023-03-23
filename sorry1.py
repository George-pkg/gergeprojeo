import time
t1 = 'eu sei que vacilei com você, e eu to me culpando a um bom tempo já...-' \
     'pse, eu to até meio sem palavras pra falar...e to meio que fazendo isso no carro -' \
     'eu tava pensando nessa forma de pedir desculpa desde mais cedo porém só conseguir fazer agr -' \
     'eu errei em várias formas possivel e isso me fez me ta uma "traumatizada" com tudo... -' \
     'porém eu quero aqui me redimir com você, pois você é a minha inspiração pra fazer TUDO! -' \
     'você é unica pessoa que eu me importo de vdd, tu és a pessoa que me faz levantar todo dia -' \
     'que me motiva a estudar, em me esforçar e para mostrar o meu melhor sempre, -' \
     'você simplesmente me motiva a qualquer coisa, to eu aqui fazendo um programa que até apendi algo novo, -' \
     'e fiz tudo isso pra essa pessoa maravilhosa que é você, simplesmente especial,' \
     '(até quando nós estamos "brigados" vc me ajuda de alguma forma :) -' \
     'eu te amo -' \
     'te amo muito -' \
     'te falo isso escutando "nobory wanta see us together, but it dont matter, no(cause i got you baby)"-' \
     'e escutando a msc, "demorei pra encontar alguem como vc, que soube me conversar que soube me entender" -' \
     'então fica aqui comigo, me perdoa meu amor?'
for p, l in enumerate(t1):
    time.sleep(0.2)
    if l == '-':
        print()
    else:
        print(l, end='')
sn = str(input('você me perdoa? \n'
               'sim ou não'))
if sn in 'simSIM':
    print('bgd, <3 <3 \n'
          'vc deve tá sorrindo agr e eu te olhando... \n'
          'i love you')