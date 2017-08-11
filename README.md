# watch_angle
angle monitoring system by TWELITE 2525A

## Description
TWELITE 2525Aデバイスを設置した対象の傾き角度のしきい値を検知しLINE Notify経由で通知する  

例）冷蔵庫や部屋の扉が開いた（開きっぱなし）等を検知する。  
　　赤ん坊の寝返りを検知する。  
＊何らかの原因により検知出来ない可能性があるので安全対策を行い。自己責任でご利用ください。  

## Requirement
[HARDWARE]  
TWELITE2525A(監視対象に設置)  
<https://mono-wireless.com/jp/products/TWE-Lite-2525A/index.html>

MoNoStick(USB型受信機)  
<https://mono-wireless.com/jp/products/MoNoStick/index.html>

Serverマシン(MoNoStickを接続可能かつpythonでシリアル通信可能)   

[SOFTWARE]  
python 3

[OTHERS]  
LINE アカウント(LINE Notifyトークン)

## Install
[HARDWARE]  
専用ソフトウェアやターミナルソフトを利用しTWELITE2525AとMoNoStickの設定変更を行う。  
<https://mono-wireless.com/jp/products/TWE-APPS/index.html>  

1~3まではMoNoStickのOTA機能を使い設定する。  
1. TWELITE2525Aを互換モードから通常モードに変更する。
2. TWELITE2525Aからの電波送信モードを定期送信にする。
3. TWELITE2525Aからの電波送信間隔秒数を設定する。  
   (電池消費量とのトレードオフで設定する。＊開発テスト動作時の参考値 8秒)
4. MoNoStickのプログラムを無線タグアプリに書き換える。
5. MoNoStickのインタラクティブモードでデータをSimple Tag V3形式に切り替える。 

[SOFTWARE]  
config.pyに以下情報を入力する。
- MoNoStickとのシリアル通信設定情報
- LINE Notifyトークン

## Usage
$ python watch_angle.py
