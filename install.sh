INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

mkdir -p $INSTALL_SH_DIRNAME/log
sudo crontab $INSTALL_SH_DIRNAME/shutdown_button/shutdown_button.crontab
crontab $INSTALL_SH_DIRNAME/setting_files/mp2.crontab
