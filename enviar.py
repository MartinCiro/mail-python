#!/usr/bin/env python3
import yagmail
import os

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
re="\033[4;31m"

os.system('clear')
print(cy+"[+] Herramienta de envio correos")
print("")
numero = input('[+] Ingrese el numero de telefono : '+re)
a=len(numero)
#Ayuda a determinar si el numero ingresado si cumple con el tamaño requerido
if a<10:
	print("El mensaje sera enviado con un numero incorrecto")
	input ("Presione intro para continuar")
#Es necesario reemplazar NO@gmail.com por el tuyo
correo="NO@gmail.com"

#Es necesario reemplazar passw con la contraseña de ingreso de NO@gmail.com
contraseña="passw"
print(""+cy)
print("1.  Airg")
print("2.  RingMedia")
print("3.  JellySocial")
print("4.  Muuvii")
print("5.  Cykadas")
print("6.  3dm")
print("7.  3gmotion")
print("8.  Addyct")
print("9.  ClubApps")
print("10. Oferta Locura")
print("11. Comcel.com.co")
print("12. Wasabi")
print("13. Moob")
print("14. Memoob")
print("15. Nextext")
print("16. Apratel")
print("17. PbCustomerCare")
print("18. Quicklii")
print("19. Satelco")
print("20. MobileAmericas")
print("21. Timwe")
print("22. Pictuday")
print("21. Reclamaciones Colombia")
print("22. pictuday")
print("24. Prueba")
opcion = int(input('[+] Elige una opcion: '+gr))
#Este será el asunto (se concatena el numero solicitado más lo que desea que diga el asunto)
asunto=numero + " Cancelacion de trivias"
#Este es el cuerpo del mensaje
massage="Buen día, estoy tratando de hacer la cancelación de las trivias activas, he enviado la palabra salir a los códigos correspondiente sin éxito al igual que la palabra baja. El número de teléfono es " + numero + " Colombia"
if opcion == 1:
	opcion="support@airg.com"
elif opcion == 2:
    opcion="help.co@ringmedia.mx" 
elif opcion == 3:
	opcion="help.co@jellysocial.com"
elif opcion==4:
	opcion="info@muuvii.com"
elif opcion == 5:
	opcion="info@cykadas.com"
elif opcion == 6:
	opcion="sac.co@3dm.com.co"
elif opcion == 7:
	opcion="ayuda@3gmotion.com"
elif opcion == 8:
	opcion="servicio_cliente@addyct.com"
elif opcion == 9:
	opcion="soporte@clubapps.com.co"
elif opcion == 10:
	opcion="info@oferlocura.com.co"
elif opcion == 11:
	opcion="SERVICIOC@COMCEL.COM.CO"
elif opcion == 12:
	opcion="support@wasabi.com"
elif opcion == 13:
	opcion="info@moob.club"
elif opcion == 14:
	opcion="info@memoob.com"
elif opcion == 15:
	opcion="helpdesk@nextext.mx"
elif opcion == 16:
	opcion="helpdesk@nextext.mx"
elif opcion == 17:
	opcion="atc@pbcustomercare.com"
elif opcion == 18:
	opcion="customer.support@quicklii.co"
elif opcion == 19:
	opcion="info@satelco.co"
elif opcion == 20:
    opcion="it@mobile-americas.com"
elif opcion == 21:
	opcion="soporte@timwe.com"
elif opcion == 22:
	opcion="help.co@pictuday.com"
elif opcion == 23:
	opcion="reclamaciones.colombia@movile.com"
print("Se está enviando a: "+ opcion)
print(""+cy)

yagmail.SMTP(correo, contraseña).send(to=opcion, subject=asunto, contents=massage)

# Adjuntar archivos en el correo
# yagmail.SMTP(correo, contraseña).send(to=opcion, subject=asunto, contents=massage, attachments=[yagmail.inline('/media/ciro/vacio/left.png')])
print("[+] Correo enviado...")

# Author - MartinCiro
