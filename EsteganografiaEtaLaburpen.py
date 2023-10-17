import hashlib
import os
from PIL import Image


def main():
	kont=1
	aurkituta=False
	while aurkituta==False:
		irudiaPath= str(os.getcwd()) + "/irudia/imagen" + str(kont) + ".jpg"
		print(f'{kont}. irudia:')
		print("Gordetako lekua: " + str(irudiaPath))
		with open(irudiaPath, 'rb') as artxiboa:
                	edukia = artxiboa.read()
		hash_obj = hashlib.md5()
		hash_obj.update(edukia)
		result=hash_obj.hexdigest()
		print("Laburpena: " + str(result))
		if result == "e5ed313192776744b9b93b1320b5e268":
			aurkituta=True
			print("Irudia hau irudi egokia izan da")
		else:
			
			kont += 1
			print("Irudia hau ez da irudi egokia")


#e5ed313192776744b9b93b1320b5e268

#"Al Fascismo no se le discute, se le destruye." Buenaventura Durruti

#StegoSuite

#run
if __name__ == "__main__":
	main()
	
