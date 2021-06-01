
# Code to encrypt/decrypt a stirng with vigenere method

def decode(cypher, llave, alfabeto):
	llave=llave*len(cypher)
	llave=llave[0:len(cypher)]
	listaTexto=[]
	listaKey=[]
	for i in cypher:
		listaTexto.append(i)
	for i in llave:
		listaKey.append(i)
	#print(listaTexto,listaKey)
	contadorKey=0
	contadorText=0
	contador=0
	decodeText=""
	for i in range(0, len(cypher)):
		for j in alfabeto:
			if listaKey[i]==j:
				contadorKey+=1
				break
			else:
				contadorKey+=1
		
		for l in range(contadorKey-1,contadorKey+len(alfabeto)):
			posicion=l
			contador+=1			
			if l>=len(alfabeto):
				posicion=l%len(alfabeto)
			#print("letra: ",alfabeto[posicion])			
			if alfabeto[posicion]==listaTexto[i]:
				break
		
		
		
		if contador>len(alfabeto):
			contador=contador%len(alfabeto)
		decodeText+=alfabeto[contador-1]
		contadorKey=0
		contadorText=0
		contador=0
	#print(decodeText)
	return decodeText
		
def code(texto, llave, alfabeto):
	indices=[]
	diccionario={}
	for i in range(0, len(alfabeto)):
		indices.append(i)
		
	newTexto=texto.split(" ")
	texto=""
	for i in newTexto:
		texto+=i
	llave=llave*len(texto)
	llave=llave[0:len(texto)]
	
	listaTexto=[]
	listaKey=[]
	for i in texto:
		listaTexto.append(i)
	for i in llave:
		listaKey.append(i)
	#print(listaTexto,listaKey)
	contadorKey=0
	contadorText=0
	cypher=""
	for i in range(0, len(texto)):
		for j in alfabeto:
			if listaKey[i]==j:
				contadorKey+=1
				break
			else:
				contadorKey+=1
		#print(listaKey[i]," tiene el indice: ", contadorKey )

		for k in alfabeto:
			if listaTexto[i]==k:
				contadorText+=1
				break
			else:
				contadorText+=1
		contadorKey+=contadorText-1
		if contadorKey>len(alfabeto):
			contadorKey=contadorKey%len(alfabeto)
		cypher+=alfabeto[contadorKey-1]
		contadorKey=0
		contadorText=0
	#print(cypher)
	return cypher
		

if __name__ == '__main__':		
    print("EL TEXTO CIFRADO ES: ", code("HOLAMUNDO","PLANTA",["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]))		
    print("EL TEXTO DESCIFRADO ES: ",decode("WZLNFUCOO","PLANTA",["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]))

