#### インストール
詳細は [gdrive](https://github.com/prasmussen/gdrive) を参照すること
##### 本番環境
ダウンロード，インストールを行う．
```shell-session:install_gdrive-linux-rpi
cd ~ && \
curl -JLO "https://docs.google.com/uc?id=0B3X9GlR6EmbnVXNLanp4ZFRRbzg&export=download" && \
sudo mv gdrive-linux-rpi /usr/local/bin/ && \
sudo chmod +x /usr/local/bin/gdrive-linux-rpi && \
echo -e '#!/bin/sh\n\ngdrive-linux-rpi $@' | sudo tee /usr/local/bin/gdrive && \
sudo chmod +x /usr/local/bin/gdrive && \
gdrive about && \
mkdir -p ~/Git/MP2_A2_audiofiles/AudioFiles && \
gdrive sync download 1fsgg8db2atpJoXQcaFopyBxnHpK034YE ~/Git/MP2_A2_audiofiles/AudioFiles
```

##### テスト環境
`Raspberry PI` と同様にダウンロード，インストールを行う．
```shell-session:install_gdrive-linux-x64
cd ~ && \
curl -JLO ［URL］ && \
sudo mv gdrive-linux-x64 /usr/local/bin/ && \
sudo chmod +x /usr/local/bin/gdrive-linux-rpi && \
echo -e '#!/bin/sh\n\ngdrive-linux-x64 $@' | sudo tee /usr/local/bin/gdrive && \
sudo chmod +x /usr/local/bin/gdrive && \
gdrive about && \
mkdir -p ~/Git/MP2_A2_audiofiles/AudioFiles && \
gdrive sync download 1fsgg8db2atpJoXQcaFopyBxnHpK034YE ~/Git/MP2_A2_audiofiles/AudioFiles
```

##### その他
`/usr/local/bin/gdrive` を作成するのではなく，`gdrive-linux-*` を `gdrive` にrenameしても良い．

#### 使用方法
`[ID]` はGoogle Driveの `AudioFiles` のディレクトリのIDを参照すること
##### アップロード
```shell-session:gdrive_upload
$ gdrive sync upload ~/Git/MP2_A2_audiofiles/AudioFiles [ID]
```

##### ダウンロード
```shell-session:gdrive_download
$ gdrive sync download [ID] ~/Git/MP2_A2_audiofiles/AudioFiles
```
