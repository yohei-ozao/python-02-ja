# チャレンジ1
各種のデータと通常のテキストが混在しているテキストドキュメントがあります。データの形式は <データ名>:<値> です。たとえば、Age:25、Height:180cm、Weight:70kg のようになります。データはその他の不要なテキストに混ざってドキュメント中に散在しています。

## パート1
`extract_data` 関数を完成させてください。正規表現のパターンを使用して、テキストからすべてのデータを抽出する必要があります。

- 正規表現のパターンでは、データ名の後にコロンとその値を指定します。
- 値は数字、文字列、英数字の組み合わせのいずれかです。

### 入力と出力の例
入力:
```
"The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."
```

出力:
```python
['Age:25', 'Height:180cm', 'Weight:70kg']
```

## パート2
`better_extract_data` 関数を完成させてください。

- タプルのリストで結果を出力し、各タプルをデータ名と値で構成します。

> ヒント: **キャプチャグループ**を使用する必要があります。キャプチャグループについて調べてみてください。

### 入力と出力の例
入力:
```
"The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."
```

出力:
```python
[("Age", "25"), ("Height", "180cm"), ("Weight", "70kg")]
```