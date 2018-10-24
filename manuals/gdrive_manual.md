#### インストール
`[URL]` は [GitHub_gdrive](https://github.com/prasmussen/gdrive) を参照すること
##### 本番環境
ダウンロード，インストールを行う．
```shell-session:install_gdrive-linux-rpi
$ curl -JLO [URL]
$ sudo mv gdrive-linux-rpi /usr/local/bin/
$ sudo chmod +x /usr/local/bin/gdrive-linux-rpi
$ sudo gdrive-linux-rpi about
$ gdrive-linux-rpi about  # 認証する
```
シェルスクリプトで `gdrive` コマンドが使えるように，`/usr/local/bin/gdrive` を作成する．
```bash:/usr/local/bin/gdrive
#!/bin/sh

gdrive-linux-rpi $@
```

##### テスト環境
`Raspberry PI` と同様にダウンロード，インストールを行う．
```shell-session:install_gdrive-linux-x64
$ curl -JLO [URL]
$ sudo mv gdrive-linux-x64 /usr/local/bin/
$ sudo chmod +x /usr/local/bin/gdrive-linux-x64
$ sudo gdrive-linux-x64 about
$ gdrive-linux-x64 about  # 認証する
```
シェルスクリプトで `gdrive` コマンドが使えるように，`/usr/local/bin/gdrive` を作成する．
```bash:/usr/local/bin/gdrive
#!/bin/sh

gdrive-linux-x64 $@
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
