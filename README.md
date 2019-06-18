# NAIST_SyncWithGoogleCalender

NAISTの履修登録状況を確認して、Googleカレンダーに同期させます。

/dist/account.txtを自分の曼荼羅ログイン情報に書き換えてoutputCSV.exeを起動すると.csvファイルが吐き出されます。

そのCSVのデータをGoogleカレンダーのインポート設定からインポートすれば仕様できます。

インポート詳細 : https://support.google.com/calendar/answer/37118?hl=ja

```text:account.rb
naist-hanako
123password456
```


