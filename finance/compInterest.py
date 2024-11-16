
import time
from Settings.properties import * # <carpetaOrigen>.<nombreArchivoPy>
# Proceso principal 

try:
	while goAhead == True:
############# Inicializacion de Variables ################
		initValues    = clearVars() # Arreglo con valores inicializados dayCnt
		detailFlag    = initValues[0]
		incrementFlag = initValues[1]
		dayCnt        = initValues[2]
		counter2      = initValues[3]
##########################################################
		print()
		initAmount      = float(input("Monto inicial        : "))
		processDays     = int(input("Total de días        : "))     # Días de proceso
		incrementAmount = float(input("Incremento quincenal : "))

		if incrementAmount > 0:
			incrementFlag = True
	
		currAmount = initAmount
		oldAmount  = currAmount
		print()

		for day in range(0,(processDays+1)):
			if incrementFlag == True:
				if day > 0:
					dayCnt += 1
				n = dayCnt	
				if dayCnt == incrementDay:
					counter2 += 1
					if detailFlag == True:
						print("Incremento " + str(counter2) + ": + ${:,.2f}".format(incrementAmount))
					currAmount = oldAmount + incrementAmount
					n      = 1
					flag1  = 1
					dayCnt = 1
				else:
					flag1 = 0
			else:
				n = day

			newAmount = (currAmount*((1+f)**n))
			interests = (newAmount-(incrementAmount*flag1))-oldAmount
			oldAmount = newAmount
	
			if detailFlag == True:
				print("Dia " + str(day) + " Saldo : ${:,.2f}".format(newAmount)) 
				print("Intereses del dia : ${:,.2f}".format(interests))
				print()
	
		print()
		print("Saldo Inicial     : ${:,.2f}".format(initAmount))
		print("Desembolso        : ${:,.2f}".format(counter2*incrementAmount))	
		print("Intereses totales : ${:,.2f}".format((newAmount-(counter2*incrementAmount))-initAmount))
		print(sDottedLine)
		print("Saldo Final       : ${:,.2f}".format(newAmount))
		goAhead = WantToRepeat(goAhead)
		
except:
	os.system("cls")
	print()
	print("Algo salio mal")

finally:
	print()
	print(sStars + " Fin del programa " + sStars)
	time.sleep(2)
	print()
