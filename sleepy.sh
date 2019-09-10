#!/bin/bash
sec=$[ ( $RANDOM % 20) + 1]s
echo "PID=$$ ($PPID) simulating a job for $sec"
sleep $sec
echo PID=$$ done sleeping.
