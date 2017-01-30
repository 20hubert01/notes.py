import random
import sys
import os
print('s - zapis do pliku')
print('r - przeczytanie pliku')
print('d - usuniecie z pliku')
print('exit')
print('---------------------------')


select_file = raw_input('Prosze wybrac plik / badz utworzyc nowy  : ')
if select_file == 'exit':
	sys.exit()
else:
	
	while True:
		what = raw_input('Co chces zrobic ? ');

		if what == 's':
			save = raw_input('wybrales zapis do pliku. Co chcesz zanotowac ? ')
			text = open(select_file+'.txt','a+')
			
			if len(text.read()) == 0:
				text.write(save)
			else:
				text.write('\n')
				text.write(save)
			
	#	print('do pliku : '+save_file+'zapisales'+save)
			text.close()
		elif what == 'clear':

			def cls():
				os.system('cls' if os.system=='nt' else 'clear')
			cls()
			

		elif what == 'r':
			text_r = open(select_file+'.txt','a+')
			text_r.write("");
			print (text_r.read())
			text_r.close()
		elif what == 'd':
			text_d = open(select_file+'.txt','r+')
			#table = [(text_d.read().split())]
			quote_table = text_d.read().split('\n')
			for words in quote_table:
				print words
			text_d.close()
			toDelete = raw_input('Ktory wiersz chcesz usunac : ')
			if toDelete.isdigit():
				d_element = open(select_file+'.txt','r')
				quote_elements = d_element.read().split('\n')
				print(len(quote_elements))
				d_element.close()
				if  int(toDelete)>len(quote_elements):
					print "Indeks zaduzy EROR"
					
				else:
					d_e = quote_elements.pop(int(toDelete))
					save_a_new_file = ''
					for tab in quote_elements:
						save_a_new_file=save_a_new_file+tab+'\n'
					save_a_new_file = save_a_new_file.rstrip()
					#print save_a_new_file
					
					d_element_d = open(select_file+'.txt','w')
					d_element_d.write(save_a_new_file)
					d_element_d.close()
					
					
			elif indeks>'':
				indexN = table.index(toDelete)
				tmp_word = table[indexN]
				table.remove(toDelete)
				print('Wiersz '+ tmp_word+'- zostal usuniety')
				text_d.close()
			else:
				print("cos poszlo nie tak ")
		elif what=='exit':
			sys.exit()
		
		
	
	
	







