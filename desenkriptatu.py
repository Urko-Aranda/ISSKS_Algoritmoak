contador = {}
porcentajes_calculados = {}
porcentajes_introducidos = {}
letras_cambiadas = {}
numero_letras = 0
mensaje = ""

def main():
    global numero_letras
    global mensaje
    mensaje = input("Introduce el mensaje: ")
    for caracter in mensaje:
        if caracter.isalpha():
            numero_letras += 1
            if caracter in contador:
                contador[caracter] += 1
            else:
                contador[caracter] = 1
                
    for letra, cuenta in contador.items():
        print(f"'{letra}': {cuenta}")
        
    calcular_porcentajes()
    guardar_porcentajes()
    comparar_porcentajes()
    guardar_clave()
    imprimir_mensaje()
    clave()
    
def calcular_porcentajes():
    for letra,elemento in contador.items():
    	porcentajes_calculados [letra] = (elemento/numero_letras)*100
    	
    print("porcentajes")
    for letra, cuenta in porcentajes_calculados.items():
        print(f"'{letra}': {cuenta}")
    	
def guardar_porcentajes():
    porcentajes_introducidos["A"] = 11.96
    porcentajes_introducidos["B"] = 0.92
    porcentajes_introducidos["C"] = 2.92
    porcentajes_introducidos["D"] = 6.87
    porcentajes_introducidos["E"] = 16.78
    porcentajes_introducidos["F"] = 0.52
    porcentajes_introducidos["G"] = 0.73
    porcentajes_introducidos["H"] = 0.89
    porcentajes_introducidos["I"] = 4.15
    porcentajes_introducidos["J"] = 0.3
    porcentajes_introducidos["K"] = 0.0
    porcentajes_introducidos["L"] = 8.37
    porcentajes_introducidos["M"] = 2.12
    porcentajes_introducidos["N"] = 7.01
    porcentajes_introducidos["Ñ"] = 0.29
    porcentajes_introducidos["O"] = 8.69
    porcentajes_introducidos["P"] = 2.776
    porcentajes_introducidos["Q"] = 1.53
    porcentajes_introducidos["R"] = 4.94
    porcentajes_introducidos["S"] = 7.88
    porcentajes_introducidos["T"] = 3.31
    porcentajes_introducidos["U"] = 4.8
    porcentajes_introducidos["V"] = 0.39
    porcentajes_introducidos["W"] = 0.0
    porcentajes_introducidos["X"] = 0.06
    porcentajes_introducidos["Y"] = 1.54
    porcentajes_introducidos["Z"] = 0.15
    
def comparar_porcentajes2():
    for letra, valor_calculado in porcentajes_calculados.items():
        encontrado = False
        for letra2, valor_introducido in porcentajes_introducidos.items():
            #print(letra2)
            if abs(valor_calculado - valor_introducido) < 0.1:
                encontrado = True
                letras_cambiadas[letra] = letra2
                
def comparar_porcentajes():
    porcentajes_calculados2 = dict(sorted(porcentajes_calculados.items(), key=lambda item: item[1], reverse=True))
    porcentajes_introducidos2 = dict(sorted(porcentajes_introducidos.items(), key=lambda item: item[1], reverse=True))

    for clave_primero, clave_segundo in zip(porcentajes_calculados2.keys(), porcentajes_introducidos2.keys()):
        letras_cambiadas[clave_primero] = clave_segundo

    print("letras cambiadas:")
    for letra, cuenta in letras_cambiadas.items():
        print(f"'{letra}': {cuenta}")
            

def imprimir_mensaje():
    texto = ""
    for caracter in mensaje:
        if caracter.isalpha():
            texto += letras_cambiadas[caracter]
        else:
            texto += caracter
    print("EL MENSAJE ES:")
    print(texto)


def guardar_clave():
    letras_cambiadas["A"] = "D"
    letras_cambiadas["B"] = "_"
    letras_cambiadas["C"] = "I"
    letras_cambiadas["D"] = "P"
    letras_cambiadas["E"] = "A"
    letras_cambiadas["F"] = "X"
    letras_cambiadas["G"] = "J"
    letras_cambiadas["H"] = "T"
    letras_cambiadas["I"] = "O"
    letras_cambiadas["J"] = "N"
    letras_cambiadas["K"] = "R"
    letras_cambiadas["L"] = "Z"
    letras_cambiadas["M"] = "H"
    letras_cambiadas["N"] = "S"
    letras_cambiadas["Ñ"] = "_"
    letras_cambiadas["O"] = "F"
    letras_cambiadas["P"] = "M"
    letras_cambiadas["Q"] = "B"
    letras_cambiadas["R"] = "C"
    letras_cambiadas["S"] = "Q"
    letras_cambiadas["T"] = "L"
    letras_cambiadas["U"] = "C"
    letras_cambiadas["V"] = "Y"
    letras_cambiadas["W"] = "_"
    letras_cambiadas["X"] = "E"
    letras_cambiadas["Y"] = "_"
    letras_cambiadas["Z"] = "U"
    
def clave():
    seguir = input("quieres seguir? S/N")
    while seguir == "S":
        for letra, cuenta in letras_cambiadas.items():
            clave = input(f"{letra} con cual se corresponde?")
            if clave.isalpha():
                letras_cambiadas[letra] = clave 
        imprimir_mensaje()

    
#RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.

#EL MENSAJE ES: CON DURRUTI MORIA EL DIRICENTE QUE, A SU MANERA, MEJOR EXPRESABA COMO COMBATIR AL FASCISMO DESDE UN CRITERIO DE INDEPENDENCIA DE CLASE, A DIFERENCIA DEL COLABORACIONISMO FRENTEPOPULISTA DE LA DIRECCION ANARQUISTA. DURRUTI FUE UN FACTOR DE PRIMER ORDEN EN EL PAPEL DE LA CLASE OBRERA EN CATALUNYA EN JULIO DE 1936. PERO DURRUTI, COMO OCURRE CON LAS PERSONALIDADES EN LA HISTORIA, NO CAYO DEL CIELO. PERSONIFICABA LA TRADICION REFOLUCIONARIA DE LA CLASE OBRERA. SU ENORME POPULARIDAD ENTRE LA CLASE TRABAJADORA, REFLEJADA EN EL ENTIERRO MULTITUDINARIO EN BARCELONA EL 22 DE NOFIEMBRE DE 1936, MUESTRA ESA IDENTIFICACION. SU MUERTE FUE SIN DUDA UN COLPE OBJETIFO AL PROCESO REFOLUCIONARIO EN MARCHA. SIN DURRUTI QUEDO MAS LIBRE EL CAMINO PARA QUE EL ESTALINISMO, CON LA COMPLICIDAD DEL COBIERNO DEL FRENTE POPULAR Y DE LA DIRECCION ANARQUISTA, TERMINARA EN MAYO DE 1937 LA TAREA DE LIQUIDAR LA REFOLUCION, DESMORALIZANDO A LA CLASE OBRERA Y FACILITANDO CON ELLO EL POSTERIOR TRIUNFO FRANQUISTA.


#run
if __name__ == "__main__":
    main()

