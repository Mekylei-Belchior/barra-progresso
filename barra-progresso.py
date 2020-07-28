# -*- coding: utf-8 -*-
from sys import stdout


INICIO = 1
FIM = 10000
STATUS = ['Processando', 'Completo']
REPETICAO = 50

print()

for i in range(REPETICAO):
	for j in range(INICIO, FIM + 1):
	    # Calcula o percentual do processo
	    percent = (int(round(float(j)/FIM * 100)))
	    
	    if percent < 100:
	    	# Imprime na tela a barra de progresso
	    	stdout.write('\r%s%s%s' % (
	    		
	    		f'[ {STATUS[0]:^13}',
	    		'      ] [ ',
	    		f'{("-" * (percent // 2)):<50} ] ( {str(percent):^4}% )')
	    	)
	    else:
	    	# Imprime na tela a barra de progresso 100%
	    	stdout.write('\r%s%s' % (
	    	
	    		f'[ {STATUS[1]:^13} {str(i+1).zfill(2)}/{REPETICAO}] [ ',
	    		f'{("■" * (percent // 2)):<50} ] ( {str(percent):^4}% )')
	    	)

	    # Exibe os dados do buffer. Permite visualizar o percentual em progresso.
	    stdout.flush()

	print()
