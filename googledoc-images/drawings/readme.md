# drawings

## 目的

+ Google Drive にて作成した図(drawings) を GitHub上で見れるようにしたい

## やり方

### 1. Google Drive にて、図形を作成

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-01.png)


### 2. ツールバーから、 `ファイル` を選択

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-02.png)


### 3. `ウェブに公開` を選択

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-03.png)

### 4. 以下のようなポップアップが出てくるので、 `公開` をクリック

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-04.png)

### 5. 以下のようなポップアップが出てくるので、 `OK` をクリック

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-05.png)

### 6. リンクが生成されるので、それをコピーする

![](https://github.com/iganari/zatsu/blob/modify-readme-only/googledoc-images/drawings/images/drawings-06.png)

### 7. コピーしたURLをMarkdownに貼り付ける

+ 形式

```
![](コピーしたURL)
```

+ デモ

![](https://docs.google.com/drawings/d/e/2PACX-1vTVlxu8AkysmuMcEc1p7jikU_QLwesyOITyiU5-n5XYIqmhQir4RzfmKkvIK14Mi17xZeMdrhgbi75h/pub?w=960&h=720)


## :warning: 

+ `共有可能なリンク` はそのファイル自体へのリンクであり、今回のような完全に図としてのアクセスとは違うので、Markdownに `図として` 貼り付けることは出来ません
+ 逆にそのファイル自体にアクセスしてほしい場合(共同で作業する時など)は、 `共有可能なリンク` を使用しましょう
