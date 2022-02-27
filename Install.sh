#!/bin/bash
OS=$(uname -o)
case $( uname -o ) in
GNU/Linux*)   echo "linux"; exec -c sudo apt install python3 python3-pip -y; chmod 777 enviar.py && echo "Instalado! No olvide modificar sus varibles De: y Para:" read enter ;;
Android*)  echo "Android" pkg install python python3 git -y; pip3 install -r requirements.txt; chmod 777 enviar.py && echo "¿Quiere hacer una prueba?" read enter && python3 enviar.py ;;
esac

