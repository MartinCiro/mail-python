#!/bin/bash
OS=$(uname -o)
case $( uname -o ) in
GNU/Linux*)   echo "linux" sudo apt install python3 python3-pip git -y && sudo pip3 install -r requirements.txt && chmod 777 enviar.py && python3 enviar.py ;;
Android*)  echo "Android" pkg install python python3 git -y && pip3 install -r requirements.txt && chmod 777 enviar.py && python3 enviar.py ;;
esac

