#!/bin/bash
OS=$(uname -o)
case $( uname -o ) in
GNU/Linux*)   echo "linux"  sudo pip3 install -r requirements.txt && chmod 777 enviar.py && echo "¿Quiere hacer una prueba?" read enter && python3 enviar.py ;;
Android*)  echo "Android" pkg install python python3 git -y; pip3 install -r requirements.txt; chmod 777 enviar.py && echo "¿Quiere hacer una prueba?" read enter python3 enviar.py ;;
esac

