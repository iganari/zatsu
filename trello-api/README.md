# Trello API MEMO

## ユーザ作成

+ https://trello.com/waiwaitgif

```
export _user='waiwaitgif'
```

## KeyとSecretを取得

まずはここ
https://trello.com/app-key

```
export _key=''
export _sec=''
```

`Token`  を押して、token発行画面にいく

```
https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=${_key}
```

```
export _token=''
```


## part 2

+ 手動オペレーション
    + ボードの作成
    + リストの作成
        + 2個作る


## part 3


+ ボードのIDを調べる

```
### 全情報
curl --request GET \
  --url "https://api.trello.com/1/members/${_user}/boards?filter=all&fields=all&lists=none&memberships=none&organization=false&organization_fields=name%2CdisplayName&key=${_key}&token=${_token}"


### nameとID
curl --request GET \
  --url "https://api.trello.com/1/members/${_user}/boards?filter=all&fields=name&lists=none&memberships=none&organization=false&organization_fields=name%2CdisplayName&key=${_key}&token=${_token}"
```

+ ボード内のID取得

```
export _board_id=''
```

+ リストのIDを調べる

```
curl --request GET \
  --url "https://api.trello.com/1/boards/${_board_id}/lists?cards=none&card_fields=all&filter=open&fields=all&key=${_key}&token=${_token}"
```

+ リストのID取得

```
export _list_id_01=''
```
```
export _list_id_02=''
```

## psrt 4

+ カードを新規作成

```
export _card_name='posttest'  ## スペース入れるとURLの解釈が変わるので注意
```

```
curl --request POST \
  --url "https://api.trello.com/1/cards?name=${_card_name}&idList=${_list_id_01}&keepFromSource=all&key=${_key}&token=${_token}"
```

+ カードのIDを調べる

```
### 全情報
curl --request GET --url "https://api.trello.com/1/lists/${_list_id_01}/cards?fields=id,name,badges,labels&key=${_key}&token=${_token}"


### nameとIDだけ
curl --request GET --url "https://api.trello.com/1/lists/${_list_id_01}/cards?fields=id,name&key=${_key}&token=${_token}"
```

+ 今後、操作したいカードのID

```
export _card_id=''
```
## port 5

+ move card

```
export _list_id_02=''
```

---> 現時点ではまだ分からなかったので、メモ

## post 6

+ カードの削除
    + Not アーカイブ

```
curl --request DELETE \
  --url "https://api.trello.com/1/cards/${_card_id}?key=${_key}&token=${_token}"
```


