# Tinyprog

Tinyprog (tiny progressbar)は，シンプルなプログレスバーです．

## インストール
インストール方法は次の通りです．
``` bash
git clone https://github.com/YugoTakagi/tinyprog.git
cd tinyprog 
pip install .
```

## 使い方
プログレスバーの表示方法は次の通りです．
for文に添えることで進捗を表示します．

``` python
import time
import tinyprog

for i in tinyprog.Colorbar(range(200)):
    time.sleep(0.05)
print('> End!')
```
