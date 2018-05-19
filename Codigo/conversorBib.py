def leArquivo(nomeArq):
	
	arq = open(nomeArq,'r')
	texto = arq.read()
	arq.close()
	
	return texto
	
def tokens(texto):
	lstTokens = []
	a = texto.split()
	
	for simbol in a:
		if '(' == simbol or ')' == simbol:
			lstTokens.append(simbol)
		elif '(' not in simbol and ')' not in simbol:
			lstTokens.append(simbol)
		
		elif '()' in simbol:
			
			lstTokens.append(simbol[:simbol.find('(')+1])
			lstTokens.append(simbol[simbol.find(')')+1])
			
		elif ')' in simbol:
			
			lstTokens.append(simbol[:simbol.find(')')])
			
			if ')' not in simbol:
				lstTokens.append(simbol[simbol.find(')'):])
			elif ')' in simbol:
				while ')' in simbol:
					lstTokens.append(')')
					simbol = simbol.replace(')',"",1)
					
		elif '(' in simbol:
			
			lstTokens.append(simbol[simbol.find('(')])
			simbol = simbol[1:]
			
			if '(' not in simbol:
				lstTokens.append(simbol)
			elif '(' in simbol:
				while '(' in simbol:
					lstTokens.append('(')
					simbol = simbol.replace('(',"",1)
	return lstTokens
	
def maquina(lista,arquivoSaida):
	nomeMaq = lista[1]
	
	if nomeMaq	== 'moore':
		moore = maqMoore(lista)
		transMealy(moore[6],moore[5])
		escreve('mealy',moore,arquivoSaida)
		
	elif nomeMaq == 'mealy':
		mealy = maqMealy(lista)
		lstOutfn, lstTrans = transMoore(mealy[5])
		lst = []
		
		for i in mealy:
			lst.append(i)
		lst[5] = lstTrans
		lst.append(lstOutfn)
		
		lst[2] = []
		cont=0
		for a in lstOutfn:
			if cont%2 == 0:
				lst[2].append(a)
			cont+=1	

		escreve('moore',lst,arquivoSaida)
	else:
		print("ERROR!")
	
def maqMealy(lstMealy):
	lstEstados = []
	lstIN = []
	lstOUT = []
	lstFinal = []
	lstTran = []
	index = 0
	start=""

	lstMealy.remove('(')
	lstMealy.remove('mealy')
	lstMealy.remove('(')
	
	start = comumMaq(lstMealy,index,lstIN,lstOUT,lstEstados,lstFinal,start)
	
	while len(lstMealy) > 1:
		
		if lstMealy[index] == 'trans':
			del(lstMealy[:index+1])			
			index = 0			
			lst = []
			
			while ')' != lstMealy[index] and len(lstMealy) != 0:				
				ind = 1
				lst = []
				
				if lstMealy[ind] != ')' and lstMealy[ind+1] != ')' and lstMealy[ind+2] != ')' and lstMealy[ind+3] != ')':
					lst.append(lstMealy[ind])					
					lst.append(lstMealy[ind+1])
					lst.append(lstMealy[ind+2])
					lst.append(lstMealy[ind+3])					
					
					lstTran.append(lst)
					del(lstMealy[:ind+5])
					
			del(lstMealy[:])		
		index+=1
	
	return lstIN,lstOUT,lstEstados,start,lstFinal,lstTran
	
def comumMaq(lstMealy,index,lstIN,lstOUT,lstEstados,lstFinal,start):
	start = ""
	while lstMealy[index] != 'trans':
		
		if lstMealy[index] == 'symbols-in':			
			del(lstMealy[index])
		
			while lstMealy[index] != ')':
				lstIN.append(lstMealy[index])
				del(lstMealy[index])
					
			del(lstMealy[:index])
			
		elif lstMealy[index] == 'symbols-out':
			del(lstMealy[index])
			
			while lstMealy[index] != ')':
				lstOUT.append(lstMealy[index])
				del(lstMealy[index])			
			
		elif lstMealy[index] =='states':			
			del(lstMealy[:index+1])
			index=0
				
			while lstMealy[index] != ')':
				lstEstados.append(lstMealy[index])
				del(lstMealy[index])			
						
		elif lstMealy[index] == 'start':
			del(lstMealy[:index+1])
			index = 0
	
			start = lstMealy[index]
			del(lstMealy[index])
			
		elif lstMealy[index] == 'finals':
			del(lstMealy[:index+1])
			index = 0
			
			while lstMealy[index] != ')':
				lstFinal.append(lstMealy[index])
				del(lstMealy[index])
		
		index += 1
	return start
	
def maqMoore(lstMoore):
	lstEstados = []
	lstIN = []
	lstOUT = []
	lstFinal = []
	lstTran = []
	DicFN = {}
	index = 0
	start=""

	lstMoore.remove('(')
	lstMoore.remove('moore')
	lstMoore.remove('(')
	
	start = comumMaq(lstMoore,index,lstIN,lstOUT,lstEstados,lstFinal,start)
	
	while len(lstMoore) > 1:
		
		if lstMoore[index] == 'trans':
			del(lstMoore[:index+1])
			index = 0
			lst = []
			while 'out-fn' not in lst:				
				ind = 1
				lst = []
				if lstMoore[ind] != ')' and lstMoore[ind+1] != ')' and lstMoore[ind+2] != ')':
					lst.append(lstMoore[ind])					
					lst.append(lstMoore[ind+1])
					lst.append(lstMoore[ind+2])	
					if 'out-fn' not in lst:
						lstTran.append(lst)					
						del(lstMoore[:ind+4])
		
		elif lstMoore[index] == 'out-fn':
			del(lstMoore[:index+2])			
			index=0
			
			while index < len(lstMoore):
				if lstMoore[index] in lstEstados and lstMoore[index+1] == '(': 
					DicFN[lstMoore[index]] = ' '
					del(lstMoore[:index])
					
				else:					
					if lstMoore[index] in lstEstados and lstMoore[index+1] in lstOUT: 
						DicFN[lstMoore[index]] = lstMoore[index+1]
						del(lstMoore[:index])
						index=0
								
				index+=1
			del(lstMoore[:index])
		index+=1
	
	return  lstIN,lstOUT,lstEstados,start,lstFinal,lstTran,DicFN

def transMealy(DicFN,lstTran):
	lstTransMealy = []
	
	for t in lstTran:
		
		if DicFN[t[1]] == ' ':
			t.append('e')	
		else:
			t.append(DicFN[t[1]])		
			lstTransMealy.append(t)

def transMoore(lstTran):
	lstTransicao = []
	dicOutfn = {}
	cont = 0
	lstTemp = lstTran
	lstOutfn = []	
	i = 0
	
	for linha in lstTran:
		
		cont = 0
		for unid in lstTemp:
			if linha[1] == unid[1] and linha[3] == unid[3]:
				cont += 1
				
		if cont == 1:
			lstOutfn.append(linha[1])
			lstOutfn.append(linha[3])
			
		if cont > 1:
			i += 1
			if (linha[1],linha[3]) not in dicOutfn:
				dicOutfn[(linha[1],linha[3])] = linha[1] + str(i)
	
	for linha in lstTran:
		lst = []
		lst.append(linha[0])
		if linha[1] in lstOutfn:
			lst.append(linha[1])
		else:
			lst.append(dicOutfn[linha[1],linha[3]])
			
		lst.append(linha[2])
		lstTransicao.append(lst)
		
	for linha in lstTran:
		if (linha[1],linha[3]) in dicOutfn and dicOutfn[(linha[1],linha[3])] not in lstOutfn:
			lstOutfn.append(dicOutfn[(linha[1],linha[3])])
			lstOutfn.append(linha[3])
	
	return lstOutfn, lstTransicao
	
def escreve(nome,lst,arquivoSaida):	
	x = ""
	
	if nome == 'mealy':
		arqEsc = open(arquivoSaida,'w')
		x += '( mealy \n ( symbols-in '
		x,lst = formaTexto(x,lst)
		x += '))'
		
	elif nome == 'moore':
		arqEsc = open(arquivoSaida,'w')
		x += '( moore \n ( symbols-in '
		x,lst = formaTexto(x,lst)
		
		x += ') \n ( out-fn \n '
		cont = 0
		for a in lst[6]:
			if cont == 0:
				x += '('
			cont+=1
			x +=  a + ' '
			if cont == 2:
				x += ') '
				cont = 0			
		x += '))'
	arqEsc.writelines(x)
	arqEsc.close()
	
def formaTexto(x,lst):

	#Inserindo SYMBOLS-IN
	for a in lst[0]: 
		x += a + ' '		
	x += ')\n ( symbols-out '
	
	#Inserindo SYMBOLS-OUT
	for a in lst[1]:
		x += a + ' '	
	x += ') \n ( states '
	
	#Inserindo STATES
	for a in lst[2]:
		x += a + ' '
	x += ') \n ( start ' 
	
	#Inserindo START
	x += lst[3] + ' ) \n ( finals ' 
	
	#INSERINDO FINALS
	for a in lst[4]:
		x += a + ' '
	x += ') \n ( trans \n ' 

	#INSERINDO TRANS
	cont = 0
	for a in lst[5]:
		x += '( '
		
		for b in a:
			x += b + ' '
		x += ') '
		cont+=1
		
		if cont == 3:
			x += '\n '
			cont = 0
	
	return x,lst