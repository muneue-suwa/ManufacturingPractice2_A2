# Raspberry PIの操作方法

## 音量調節方法
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
