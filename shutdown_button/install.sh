INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`
MP2_PATH=`dirname $INSTALL_SH_DIRNAME`

mkdir -p $MP2_PATH/log
sudo crontab $INSTALL_SH_DIRNAME/shutdown_button.crontab
