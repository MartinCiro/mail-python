#!/bin/bash
OS=$(uname -o)
case $( uname -o ) in
GNU/Linux*)   echo "linux" sudo apt install python3 python3-pip git -y && git clone git://github.com/AnonyVox/send-mail.git && cd send-mail && sudo pip3 install -r requirements.txt && chmod 777 run.py && python3 run.py ;;
Android*)  echo "Android" pkg install python python3 git -y && git clone git://github.com/AnonyVox/send-mail.git && cd send-mail
esac

