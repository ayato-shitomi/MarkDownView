# CLIマークダウンビュワー

## 使い方

```
> python3 main.py <README FILE>
```

## 実装範囲

実装した範囲は以下

> ・コードブロック
・タイトルと見出し
・引用
・インラインコード

これから実装したい機能

> 太字等の挙動


## エラーケース

### Error1

引数の個数は1つまでです。

### Error2

引数はマークダウンファイルでなくてはなりません。
よって、`.md`で終わる必要があります。

## バグ

> 引用の中のインラインコードが長すぎるとバグります。

テストケース
```
> `ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTYUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`
```