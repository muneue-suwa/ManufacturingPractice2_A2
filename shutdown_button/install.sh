INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

sudo mkdir -p /usr/lib/systemd/system/
sudo touch /usr/lib/systemd/system/shutdownd.service
echo "[Unit]\nDescription=Shutdown Daemon\n" | sudo tee /usr/lib/systemd/system/shutdownd.service
echo "[Service]\nExecStart=$INSTALL_SH_DIRNAME/shutdown_button.py\nRestart=always\nType=simple\n" \
    | sudo tee -a /usr/lib/systemd/system/shutdownd.service
echo "[Install]\nWantedBy=multi-user.target\n" | sudo tee -a /usr/lib/systemd/system/shutdownd.service

sudo systemctl enable shutdownd.service 
sudo systemctl status shutdownd.service 

<< COMMENTOUT
shell　/usr/lib/systemd/system/shutdownd.service
[Unit]
Description=Shutdown Daemon

[Service]
ExecStart =/home/pi/py-shutdown.py
Restart=always
Type=simple

[Install]
WantedBy=multi-user.target
次にサービスを自動起動するように設定する。

pi@rp:~ $ sudo systemctl enable shutdownd.service 
ここで Raspberry Pi を再起動して、service のstatus を確認すると登録されていることが分かる。

pi@rp:~ $ sudo systemctl status shutdownd.service 
● shutdownd.service - My Shutdown Daemon, May 2, 2018
   Loaded: loaded (/usr/lib/systemd/system/shutdownd.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2018-05-01 19:52:53 UTC; 1min 22s ago
 Main PID: 336 (pi-shutdown.py)
   CGroup: /system.slice/shutdownd.service
           └─336 /usr/bin/python /home/pi/pi-shutdown.py

May 01 19:52:53 rp systemd[1]: Started My Shutdown Daemon, May 2, 2018.
ちなみに、この enable コマンドでは再起動時に自動起動するが、今サービスを起動するわけではない。すぐに有効にするには、start を使う。同様に disable ではすぐは停止しない。再起動が必要である。

今すぐ起動したり、停止したりするには、start あるいは stop を利用する。

pi@rp:~ $ sudo systemctl start shutdownd.service
pi@rp:~ $ sudo systemctl stop shutdownd.service
COMMENTOUT