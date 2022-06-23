# ukagakaCreateAnimationPng
このプログラムは伺かのアニメーションを簡単に作成できるように作成されました。< /br>
AlphaInフォルダに入れたpngファイルから指定した色を透明にしてAlphaOutフォルダに保存されます。< /br>
出力名は元の名前が使われるので、必要な順番に名前順にしておいてください。< /br>

また、surfaces.txtに必要なテキストをsurfaceXXXXX.txtに書き出してくれます。


出力先フォルダ名は指定できるので使いやすいように変更してください。< /br>
この名前は、surfaceを指定する際の相対的なパスとしてsurfaceXXXXX.txtに必要なので< /br>
config.txtを下記のように変更すると使いやすいでしょう。< /br>
```
[core]
    #出力するディレクトリ名を指定する。
    Out     = UrlEffect
```

変更しておくことでGhostのshellフォルダに重複することなく簡単に管理することが可能です。
```
surface[ surface_start_num ] {
	element[ element_num ],overlay,UrlEffect/sample.png,0,0
}
```
surfaces....txtと名のついたファイルは読み込んでくれるためこのように分割する。
```
#surfaceXXXXX.txtをsurfacesUrlEffect.txtにrenameしておく。
shell
  ├─surfaces.txt
  ├─surfacesUrlEffect.txt
  └─UrlEffect
      ├─sample001.png
      ├─sample....png
      └─samplexxx.png
```

## config
設定項目
```
#出力先フォルダ名
Out     = AlphaOut

#透過する色を指定する。
red     = 237
green   = 28
blue    = 36

##surface番号の開始番号を指定する。
surface_start_num = 9000

##surfaceのelement番号を指定する。
element_num = 10

#アニメーションを表示時間を指定する。
animation_speed = 1

#アニメーション番号を指定する。
animation_num = 0
```

###実際に出力される形
```
surface.append0 {
	animation[ animation_num ].interval,sometimes
	animation[ animation_num ].pattern0,overlay,[ surface_start_num ],[ animation_speed ],0,0
}
#必要な数だけ出力される。
surface[ surface_start_num ] {
	element10,overlay,AlphaOut/sample.png,0,0
}
```


## License
MIT

## Author
ambergon 
[twitter](https://twitter.com/Sc_lFoxGon)








