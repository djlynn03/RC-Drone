#!/bin/bash

echo "Instantiating pigpiod"
sudo pigpiod
# Sleep for a couple seconds
sleep 2s

# Load python module

# We need a program watcher (master?) to watch the drone's status
# make sure drone doesnt kill anyone

# Exceptions that are unhandled need to make their way to the this 
# watcher
