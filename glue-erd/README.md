## MermaidでER図を書く
* 公式サイト : https://mermaid.js.org/syntax/entityRelationshipDiagram.html
* プレビューはこれを入れた : https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

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

## Glueデータベースを取得する
