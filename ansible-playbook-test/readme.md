# ansible playbook test

## 使い方

+ コンテナの起動

```
sh docker-build-run.sh
```

+ [コンテナ内] ansible-playbookの実行

```
cd user
ansible-playbook -i inventoryfile/local servers.yml
```
