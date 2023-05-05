## なにこれ
* Glueデータカタログに登録されているデータベース、テーブルを指定してmermaid形式のER図を作成します。

## 使い方
* glue_erd-1.0.0-py3-none-any.whl をpip installします。
* `glueerd` で実行します。コマンドは `glueerd --help` をご確認ください。
* 実行フォルダに .mdファイルが生成されます。

## ライセンス
MITライセンスです。
```
Copyright (c) 2023 dokeita
Released under the MIT license
https://opensource.org/licenses/mit-license.php
```

## 参考:MermaidでER図を書く
* 公式サイト : https://mermaid.js.org/syntax/entityRelationshipDiagram.html
* VSコードでプレビューする: https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

``` mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```

``` mermaid
erDiagram
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```
