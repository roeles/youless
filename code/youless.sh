#!/bin/bash
IP=192.168.178.10
ROOT=/home/archive/data/youless
WATTFILE=$ROOT/watt.csv
KWHFILE=$ROOT/kwh.csv
TIMESTAMP=`date +%s`
SEPARATOR=","

#Echo timestamp
echo -n $TIMESTAMP$SEPARATOR >> $WATTFILE
#Echo Watt data
wget -O - -q http://$IP/a | grep Watt | awk '{ print $1 }' >> $WATTFILE

##Echo timestamp
#echo -n $TIMESTAMP$SEPARATOR >> $KWHFILE
##Echo kWh data
#wget -O - -q http://$IP/a | grep kWh | awk '{ print $1 }' | sed 's/,/./' >> $KWHFILE

