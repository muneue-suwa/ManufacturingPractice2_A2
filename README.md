# 機械工作実習2で制作するロボットのためのプログラム

## プログラムの用途
岡山大学機械システム系学科システムコースの機械工作実習2の授業にて制作するロボットに使用するプログラム

## tree
```
$ tree ~/Git
.
├── MP2_A2_audiofiles
│   └── AudioFiles
│       └── *.mp3  # Audio files
└─── ManufacturingPractice2_A2
    ├── README.md
    ├── main.py
    └── src  # Source files
```

## 動作環境
### 本番環境
#### Raspberry PI
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 9.4 (stretch)
Release:	9.4
Codename:	stretch
```
#### Python3
```
$ python3 --version
Python 3.5.3
```
### テスト環境
#### Ubuntu MATE
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.1 LTS
Release:	18.04
Codename:	bionic
```
#### Python3
```
$ python3 --version
Python 3.6.6
```

## 準備

### pygame（Pythonのパッケージ）のインストール
```
$ sudo apt install python3-pygame
```

### gdriveの設定
著作権等の問題により，GitHubへの音源の保存が難しいと思われるため，音源はGoogle driveに入れ，テスト環境と本番環境を同期化させる．

#### インストール
`[URL]` は [GitHub_gdrive](https://github.com/prasmussen/gdrive) を参照すること
##### 本番環境
```
$ curl -JLO [URL]
$ sudo cp gdrive-linux-rpi /usr/local/bin/
$ sudo gdrive-linux-rpi about
$ sudo chmod +x gdrive-linux-rpi
$ gdrive-linux-rpi about  # 認証する
$ vim ~/.bashrc  # aliasの設定をする
```
##### テスト環境
```
$ curl -JLO [URL]
$ sudo cp gdrive-linux-x64 /usr/local/bin/
$ sudo gdrive-linux-x64 about
$ sudo chmod +x gdrive-linux-x64
$ gdrive-linux-x64 about  # 認証する
$ vim ~/.bashrc  # aliasの設定をする
```

#### 使用方法
`[ID]` はGoogle Driveの `AudioFiles` のディレクトリのIDを参照すること
##### アップロード
```
$ gdrive sync upload ~/Git/MP2_A2_audiofiles/AudioFiles [ID]
```

##### ダウンロード
```
$ gdrive sync download [ID] ~/Git/MP2_A2_audiofiles/AudioFiles
```

## 参考文献
[Raspberry Piで音楽(wav/mp3)ファイルを再生する方法 python編](https://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918)
[google drive を コマンドから使うgdrive が早くて便利](http://takuya-1st.hatenablog.jp/entry/2016/07/06/034412)

## 音源
[効果音ラボ](https://soundeffect-lab.info/)
