# crear juego de piedra papel y tijeras

import random


#input
pc=random.randint(1,3)

print ("1.tijeras")
print ("2.piedra")
print ("3.papel")
opc=int(input("digite la opción: "))

#procesing
if (pc==1 and opc==1):
    print("maquina escoge: "+str(pc))
    print("jugador escoge: "+str(opc))
    print("empate", )
elif (pc==1 and opc==2):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("Gana el Jugador")
elif (pc==1 and opc==3):
    print("maquina escoge")+str(pc)
    print("jugador escoge: "), opc
    print("pierde el jugador")
elif (pc==2 and opc==1):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("Pierde el jugador")
elif (pc==2 and opc==2):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("Empate")
elif (pc==2 and opc==3):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("Gana el jugador")
elif (pc==3 and opc==1):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("gana el jugador")
elif(pc==3 and opc==2):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("Pierde el jugador")
elif (pc==3 and opc==3):
    print("maquina escoge"+str(pc))
    print("jugador escoge: "+str(opc))
    print("empate")
else:
    print("no es un digito válido")
    

