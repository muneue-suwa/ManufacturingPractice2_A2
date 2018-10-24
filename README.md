# 機械工作実習2で制作するロボットのためのプログラム

## プログラムの用途
岡山大学機械システム系学科システムコースの機械工作実習2の授業にて制作するロボットに使用するプログラム

## tree
```shell-session:tree
$ tree ~/Git
.
├── MP2_A2_audiofiles
│   └── AudioFiles
│       └── *.mp3  # Audio files
└─── ManufacturingPractice2_A2
    ├── README.md
    ├── main.py
    ├── src  # Source files
    └── setting.json  # Setting file
```

## 動作環境
### 本番環境
#### Raspberry PI
```shell-session:raspbian_version
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 9.4 (stretch)
Release:	9.4
Codename:	stretch
```
#### Python3
```shell-session:pytnon3_version
$ python3 --version
Python 3.5.3
```
### テスト環境
#### Ubuntu MATE
```shell-session:ubuntu_version
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.1 LTS
Release:	18.04
Codename:	bionic
```
#### Python3
```shell-session:python3_version
$ python3 --version
Python 3.6.6
```

## 準備

### pygame（Pythonのパッケージ）のインストール
```shell-session:install_pygame
$ sudo apt install python3-pygame
```

### gdriveの設定
著作権等の問題により，GitHubへの音源の保存が難しいと思われるため，音源はGoogle driveに入れ，テスト環境と本番環境を同期化させる．

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

## Raspberry PIの音量調節方法
`amixer` コマンドを使う
### デバイス，音量の確認
```shell-session:amixer_デバイス，音量の確認
$ sudo amixer -M
Simple mixer control 'PCM',0
  Capabilities: pvolume pvolume-joined pswitch pswitch-joined
  Playback channels: Mono
  Limits: Playback -10239 - 400
  Mono: Playback -2000 [40%] [-20.00dB] [on]
```
### 音量の調節
音量を `[n]` %に設定したいとき
```shell-session:amixer_音量の調節
$ sudo amixer sset PCM [n]%
```

## to-do
1. fire_and_conveyor
  1. スイッチ（センサー1）を押したら音（サイレン）とベルコン（モータ1）をスタート
  1. 一定時間後にベルコン（モータ1）を止める：<font color="Green">ベルコンの動作時間</font>
  1. クレーンが倒れる：<font color="Green">動作開始までの時間</font>
    1. クレーンを倒す（モータ2）: <font color="Green">モータ2の動作時間</font>
    1. ストッパーを外す（モータ3）: <font color="Green">モータ3の動作時間</font>
1. explode_and_escape
  1. 爆発と脱出：センサー（センサー2）でスタート：<font color="Green">センサー反応からアクション開始までの時間</font>
    1. 音（爆発音）と光（LED2）
    1. ジャンプ（モータ4）：<font color="Green">モータ4の動作時間</font>

<font color="Green">Green</font>: setting.json

## 参考文献
[Raspberry Piで音楽(wav/mp3)ファイルを再生する方法 python編](https://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918)

[google drive を コマンドから使うgdrive が早くて便利](http://takuya-1st.hatenablog.jp/entry/2016/07/06/034412)

[RaspberryPi 3 コマンドで音量を上げる（ラジオをテレビで再生→音量不足→コマンドで音量U](http://min117.hatenablog.com/entry/2017/06/22/212425)

## 音源
[効果音ラボ](https://soundeffect-lab.info/)
