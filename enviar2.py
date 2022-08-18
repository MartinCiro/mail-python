#!/usr/bin/env python3
import yagmail
import os
os.system('clear')

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
re="\033[4;31m"
rall="\033[0m"

Quicklii=[35079,35117,35118,35121,35122,35197,35231,35248,35249,35265,35478,35534,35536,35538,35917,37271,37544,37545,37673]
DM=[25441,35040,35080,35100,35235,35914,35965,37537,37750,37760,37767,57737]
GMOTION=[35405,35606]
ADDYCT=[35583,37060]
AIRG=[25060,25070,25240,27789,35060,35070,35860]
BEMOBI=[35061,37622,37938,37946]
CELMEDIA=[25111,35161]
CLAROSA=[37674,890341]
Cykadas=[25062,25063,35071,35072,35073]
GAMELOFT=[25322,27287,35096,37287]
GOOGLEPLAY=[25117,35062]
Huawei=[25608]
Wasabi=[35001,35020]
muuvii=[35046,35047,35048,35049,35358,35521,35551,35552,35926,35931,37546]
Memoob=[35022,35148,35158,35172,35290]
Nextext=[97077,290029,390039]
Satelco=[27111,27547,27612,35037,35385,37358,95958]
timwe=[25033,25245,25835,27999,35135,97970]
Pictuday=[25356,35356,35358]
AMERICAS=[35200,37707]
PbCustomerCare=[37541]
OPRATEL=[35885]

QuickliiC="customer.support@quicklii.co"
DMC="sac.co@3dm.com.co"
GMOTIONC="ayuda@3gmotion.com"
ADDYCTC="servicio_cliente@addyct.com"
AIRGC="support@airg.com"
BEMOBIC="soporte@clubapps.com.co"
CELMEDIAC="info@oferlocura.com.co"
CLAROSAC="SERVICIOC@COMCEL.COM.CO"
CykadasC="info@cykadas.com"
GAMELOFTC="special.support@gameloft.com"
HuaweiC="huaweiid@huawei.com"
WasabiC="support@wasabi.com"
muuviiC="info@muuvii.com"
MemoobC="info@memoob.com"
NextextC="helpdesk@nextext.mx"
SatelcoC="info@satelco.co"
timweC="soporte@timwe.com"
PictudayC="help.co@pictuday.com"
AMERICASC="it@mobile-americas.com"
PbCustomerCareC="atc@pbcustomercare.com"
OPRATELC="info@opratel.com"

print(cy+"[+] Herramienta de envio correos")
print("")


def greet(opcion):

    #Es necesario reemplazar NO@gmail.com por el tuyo
    correo="NO@gmail.com"

    #Es necesario reemplazar passw con la contraseña de ingreso de NO@gmail.com
    contraseña="passw"

    asunto=numero + " Cancelacion de trivias"

    massage="Buen día, estoy tratando de hacer la cancelación de las trivias activas, he enviado la palabra salir a los códigos correspondiente sin éxito al igual que la palabra baja. El número de teléfono es " + numero + " Colombia"

    print("Se está enviando a: "+ opcion)
    print(""+cy)

    #yagmail.SMTP(correo, contraseña).send(to=opcion, subject=asunto, contents=massage, attachments=[yagmail.inline('/media/ciro/vacio/left.png')])
    yagmail.SMTP(correo, contraseña).send(to=opcion, subject=asunto, contents=massage)
    print("[+] Correo enviado...")

    # Author - MartinCiro

numero = input('[+] Ingrese el numero de telefono : '+re)
cantriv = int(input('Ingrese la cantidad de trivias: '+re))
cantriv = int(cantriv)
for i in range(cantriv):
    codtriv = int(input('Ingrese la trivia: ' + str(i) + cy + ' '))
    if Quicklii.count(codtriv) > 0:
        greet(QuickliiC)
    else:
        if DM.count(codtriv) > 0:
            greet(DMC)
        else:
            if GMOTION.count(codtriv) > 0:
                greet(GMOTIONC)
            else:
                if ADDYCT.count(codtriv) > 0:
                    greet(ADDYCTC)
                else:
                    if AIRG.count(codtriv) > 0:
                        greet(AIRGC)
                    else:
                        if BEMOBI.count(codtriv) > 0:
                            greet(BEMOBIC)
                        else:
                            if CELMEDIA.count(codtriv) > 0:
                                greet(CELMEDIAC)
                            else:
                                if CLAROSA.count(codtriv) > 0:
                                    greet(CLAROSAC)
                                else:
                                    if Cykadas.count(codtriv) > 0:
                                        greet(CykadasC)
                                    else:
                                        if GAMELOFT.count(codtriv) > 0:
                                            greet(GAMELOFTC)
                                        else:
                                            if GOOGLEPLAY.count(codtriv) > 0:
                                                print ("Corresponde a una compra de la google play, correo no enviado http://play.google.com/store/account ó https://support.google.com/googleplay/")
                                            else:
                                                if Huawei.count(codtriv) > 0:
                                                    greet(HuaweiC)
                                                else:
                                                    if Wasabi.count(codtriv) > 0:
                                                        greet(WasabiC)
                                                    else:
                                                        if muuvii.count(codtriv) > 0:
                                                            greet(muuviiC)
                                                        else:
                                                            if Memoob.count(codtriv) > 0:
                                                                greet(MemoobC)
                                                            else:
                                                                if Nextext.count(codtriv) > 0:
                                                                    greet(NextextC)
                                                                else:
                                                                    if Satelco.count(codtriv) > 0:
                                                                        greet(SatelcoC)
                                                                    else:
                                                                        if timwe.count(codtriv) > 0:
                                                                            greet(timweC)
                                                                        else:
                                                                            if Pictuday.count(codtriv) > 0:
                                                                                greet(PictudayC)
                                                                            else:
                                                                                if AMERICAS.count(codtriv) > 0:
                                                                                    greet(AMERICASC)
                                                                                else:
                                                                                    if PbCustomerCare.count(codtriv) > 0:
                                                                                        greet(PbCustomerCareC)
                                                                                    else:
                                                                                        if OPRATEL.count(codtriv) > 0:
                                                                                            greet(OPRATELC)
                                                                                        else:
                                                                                            print("No existe el numero")
