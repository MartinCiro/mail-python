#!/bin/bash
OS=$(uname -o)
case $( uname -o ) in
GNU/Linux*)   echo "linux"; exec -c sudo apt install python3 python3-pip -y; chmod 777 enviar.py && echo "Instalado! No olvide modificar sus varibles De: y Para:" read enter ;;
Android*)  echo "Android"; pkg install libtool binutils clang libxml2 libxslt python python3 git -y; pip install cython lxml yagmail;  chmod 777 enviar.py ;;
esac

