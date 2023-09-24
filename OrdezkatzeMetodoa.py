kantitatea = 0
kontagailua={}
frekuentzia_tabla={}
kalkulatutako_portzentailak={}
aldaketak= {}
esaldia=""
textua=""


    
   

def main():
	global kantitatea
	global esaldia
	print("Kaixo, programa honek gaztelaniako mezuak dezifratzeko balio du")
	esaldia= input("Sartu deszifratu nahi duzun mezua: ")
	for karakterea in esaldia:
		if karakterea.isalpha():
			kantitatea +=1
			if karakterea in kontagailua:
				kontagailua[karakterea] +=1
			else:
				kontagailua[karakterea] =1
	print("Sarutako mezua hurrengo karaktere kopuru dauzka: " + str(kantitatea))
	frekuentziak_gorde()
	portzentailak_kalkulatu()
	hizkiak_aldatu()
	textua_inprimatu()
	hizkiak_eskuz_aldatu()
	
def frekuentziak_gorde():
	global frekuentzia_tabla
	frekuentzia_tabla["A"] = 11.96
	frekuentzia_tabla["B"] = 0.92
	frekuentzia_tabla["C"] = 2.92
	frekuentzia_tabla["D"] = 6.87
	frekuentzia_tabla["E"] = 16.78
	frekuentzia_tabla["F"] = 0.52
	frekuentzia_tabla["G"] = 0.73
	frekuentzia_tabla["H"] = 0.89
	frekuentzia_tabla["I"] = 4.15
	frekuentzia_tabla["J"] = 0.3
	frekuentzia_tabla["K"] = 0.0
	frekuentzia_tabla["L"] = 8.37
	frekuentzia_tabla["M"] = 2.12
	frekuentzia_tabla["N"] = 7.01
	frekuentzia_tabla["Ñ"] = 0.29
	frekuentzia_tabla["O"] = 8.69
	frekuentzia_tabla["P"] = 2.776
	frekuentzia_tabla["Q"] = 1.53
	frekuentzia_tabla["R"] = 4.94
	frekuentzia_tabla["S"] = 7.88
	frekuentzia_tabla["T"] = 3.31
	frekuentzia_tabla["U"] = 4.8
	frekuentzia_tabla["V"] = 0.39
	frekuentzia_tabla["W"] = 0.0
	frekuentzia_tabla["X"] = 0.06
	frekuentzia_tabla["Y"] = 1.54
	frekuentzia_tabla["Z"] = 0.15
	print("######################################################")
	print("")
	print("")
	print("Gaztelaniaz hauek dira hizkien agerpen frekuentzia idazterakoan: ")
	for hizkia, frekuentzia in frekuentzia_tabla.items():
		print(f"'{hizkia}': {frekuentzia}")
	print("")
	print("")
	print("######################################################")
	
	
def textua_inprimatu():
	global textua, esaldia, aldaketak
	textua=""
	for karakterea in esaldia:
		if karakterea.isalpha():
			textua+=aldaketak[karakterea]
		else:
			textua+=karakterea
	print("Mezua deszifratu da, mezua hurrengoa da: " )
	print(textua)
	
	
def portzentailak_kalkulatu():
	global kalkulatutako_portzentailak, kontagailua
	for hizkia,zenbakia in kontagailua.items():
		kalkulatutako_portzentailak[hizkia]=(zenbakia/kantitatea)*100
	print("######################################################")
	print("")
	print("")
	print("Zifratutako textuaren hizkien agerpen portzentaia kalkulatu dugu eta hauek dira: ")
	for hizkia, zenbat in kalkulatutako_portzentailak.items():
		print(f"'{hizkia}': {zenbat}")
	print("")
	print("")
	print("######################################################")
	
	
def hizkiak_aldatu():
	global aldaketak
	portzeintailak_ordenatuta = dict(sorted(kalkulatutako_portzentailak.items(), key=lambda item: item[1], reverse=True))
	frekuentziak_ordenatu =	dict(sorted(frekuentzia_tabla.items(), key=lambda item: item[1], reverse=True))
	for lehenGiltza, bigarrenGiltza in zip(portzeintailak_ordenatuta.keys(), frekuentziak_ordenatu.keys()):
		aldaketak[lehenGiltza] = bigarrenGiltza
	print("######################################################")
	print("")
	print("")
	print("Horain mezuen hizkien agerpen portzentaila eta frekuentzia konparatuz, hizkien aldaketak egin ditugu:")
	for aurrekoHizkia, egungoHizkia in aldaketak.items():
		print(f"'{aurrekoHizkia}': {egungoHizkia}")
	print("")
	print("")
	print("######################################################")
	
	
	
	
def hizkiak_eskuz_aldatu():
	global aldaketak
	while True:
		erantzuna= input("Eskuz aldaketak egin nahi dituzu: B/E")
		if erantzuna == "B":
			amaitu = False
			break
		elif erantzuna == "E":
			amaitu = True
			break
		else:
			print("Erantzuna ez da egokia esan, mesadez erantzun egoki bat ipini")
	
	while amaitu == False:
		try:
			k1= input("Ze karaktere aldatu nahi duzu mezu zifratutik?")
			k2= input("Ze karaktere ipini nahi duzu horren ordez?")
			if len(k1) != 1 or len(k2) != 1:
				raise Exception()
			aldaketak[k1] = k2
			print("######################################################")
			print("")
			print("")
			print("Hizkien aldaketa berria honako hau da: ")
			for aurrekoHizkia, egungoHizkia in aldaketak.items():
				print(f"'{aurrekoHizkia}': {egungoHizkia}")
			print("")
			print("")
			print("######################################################")
			textua_inprimatu()
			while True:
				erantzuna= input("Aldaketa gehiago egin nahi dituzu?: B/E")
				if erantzuna == "B":
					amaitu = False
					break
				elif erantzuna == "E":
					amaitu = True
					break
				else:
					print("Erantzuna ez da egokia esan, mesadez erantzun egoki bat ipini")
		except:
			print("Sartutako karaktereak ez dira egokiak, berriro saiatu")		
				
			

#RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.

#DURRUTI FUE UN FACTOR DE PRIMER ORDEN EN EL PAPEL DE LA CLASE OBRERA EN CATALUNYA EN JULIO DE 1936. PERO DURRUTI, COMO OCURRE CON LAS PERSONALIDADES EN LA HISTORIA, NO CAYO DEL CIELO. PERSONIFICABA LA TRADICION REVOLUCIONARIA DE LA CLASE OBRERA. SU ENORME POPULARIDAD ENTRE LA CLASE TRABAJADORA, REFLEJADA EN EL ENTIERRO MULTITUDINARIO EN BARCELONA EL 22 DE NOVIEMBRE DE 1936, MUESTRA ESA IDENTIFICACION. SU MUERTE FUE SIN DUDA UN GOLPE OBJETIVO AL PROCESO REVOLUCIONARIO EN MARCHA. SIN DURRUTI QUEDO MAS LIBRE EL CAMINO PARA QUE EL ESTALINISMO, CON LA COMPLICIDAD DEL GOBIERNO DEL FRENTE POPULAR Y DE LA DIRECCION ANARQUISTA, TERMINARA EN MAYO DE 1937 LA TAREA DE LIQUIDAR LA REVOLUCION, DESMORALIZANDO A LA CLASE OBRERA Y FACILITANDO CON ELLO EL POSTERIOR TRIUNFO FRANQUISTA.

#run
if __name__ == "__main__":
	main()
	

	
	

