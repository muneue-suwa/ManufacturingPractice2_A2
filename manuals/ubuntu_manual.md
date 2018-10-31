# Ubuntu の簡易マニュアル

## 画面を録画する方法
`SimpleScreenRecorder` を使用する．

### 参考文献
[Maarten Baert's website - What is SimpleScreenRecorder?](http://www.maartenbaert.be/simplescreenrecorder/)

## Ubuntu をスピーカー代わりに使う方法
以下のコマンドを実行する．
```shell-session:mic2speaker_with_ubuntu
arecord -r 44100 -c 2 -f S16_LE | aplay
```

### 参考文献
[Ubuntu日本語フォーラム - Line in の音声をそのままスピーカーから出力できません。](https://forums.ubuntulinux.jp/viewtopic.php?id=9251)


## Hotspot（テザリング）を使う方法
以下の文献を参考に設定する．

### 参考文献
[How to Create WiFi Hotspot in Ubuntu 16.04 (Android is Supported)](http://ubuntuhandbook.org/index.php/2016/04/create-wifi-hotspot-ubuntu-16-04-android-supported/)
