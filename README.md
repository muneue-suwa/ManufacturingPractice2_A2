# 機械工作実習2で制作するロボットのためのプログラム

## プログラムの用途
岡山大学機械システム系学科システムコースの機械工作実習2の授業にて制作するロボットに使用するプログラム

## tree
```shell-session:tree
$ tree ~/Git
.
├── MP2_A2_audiofiles
│   └── AudioFiles
│       └── *.mp3  # Audio files
└─── ManufacturingPractice2_A2
    ├── README.md
    ├── crontab_mp2_setting
    ├── main.py
    ├── manuals
    │   ├── gdrive_manual.md
    │   └── rpi_manual.md
    ├── setting.json
    ├── src
    │   ├── explode_and_escape.py
    │   └── fire_and_conveyor.py
    └── test_code.py
```

## 動作環境
### Raspberry PI
`Raspberry PI 2 model B` を使用する．

```shell-session:raspbian_version
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 9.4 (stretch)
Release:	9.4
Codename:	stretch
```
### Python3
```shell-session:pytnon3_version
$ python3 --version
Python 3.5.3
```
## 準備
### pygame（Pythonのパッケージ）のインストール
```shell-session:install_pygame
$ sudo apt install python3-pygame
```

### gdriveの設定
著作権等の問題により，GitHubへの音源の保存が難しいと思われるため，音源はGoogle driveに入れ，テスト環境と本番環境を同期化させる．詳細は [gdrive_manual](manuals/gdrive_manual.md) を参照すること．

### 自動起動の設定
```
$ crontab ~/Git/ManufacturingPractice2_A2/crontab_mp2_setting
```

### その他のRaspberry PIの設定方法
詳細は [rpi_manual](manuals/rpi_manual.md) を参照すること．

## 動作内容
1. fire_and_conveyor
  1. スイッチ（センサー1）を押したら
    1. 音（サイレン），光を開始
    1. ベルコン（モータ1）を開始
  1. 一定時間後にベルコン（モータ1）を止める：<u>ベルコンの動作時間</u>
  1. クレーンが倒れる：<u>動作開始までの時間</u>
    1. クレーンを倒す（モータ2）: <u>モータ2の動作時間</u>
    1. ストッパーを外す（モータ3）: <u>モータ3の動作時間</u>
1. explode_and_escape
  1. 爆発と脱出：センサー（センサー2）でスタート：<u>センサー反応からアクション開始までの時間</u>
    1. 音（爆発音）と光（LED2）
    1. ジャンプ（モータ4）

<u>Under line</u>: setting.json

## 参考文献
[Raspberry Piで音楽(wav/mp3)ファイルを再生する方法 python編](https://qiita.com/Nyanpy/items/cb4ea8dc4dc01fe56918)

[google drive を コマンドから使うgdrive が早くて便利](http://takuya-1st.hatenablog.jp/entry/2016/07/06/034412)

[RaspberryPi 3 コマンドで音量を上げる（ラジオをテレビで再生→音量不足→コマンドで音量U](http://min117.hatenablog.com/entry/2017/06/22/212425)

## 音源
[効果音ラボ](https://soundeffect-lab.info/)
