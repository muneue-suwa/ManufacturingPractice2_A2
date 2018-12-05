#!/bin/bash

INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

mkdir -p $INSTALL_SH_DIRNAME/log

python3 $INSTALL_SH_DIRNAME/crontab/make_crontab.py

sudo crontab $INSTALL_SH_DIRNAME/crontab/shutdown_button.crontab
crontab $INSTALL_SH_DIRNAME/crontab/mp2.crontab
