# AudiosetLabelSelector
AudiosetのcsvをLabel（クラス名）でSelectします
## 目的
Audiosetを用いた強化学習を行う際、データセットのcsvから必要なラベルのついたデータのみを抽出したcsvを作成する必要がある。  
しかし、クラス名とラベルとの対応付けは専用のcsvファイルで行われており、大変面倒である。  
そこでこのプログラムは、ラベルを介さずクラス名から直接ラベルを指定し、csvファイルを抽出することができる。  

## 使い方
### 事前準備
[Audiosetのダウンロードページ](https://research.google.com/audioset/download.html)
から必要なファイルをダウンロードし、target下に入れる
* class_labels_indices.csv
* eval_segments.csv
* balanced_train_segments.csv
* unbalanced_train_segments.csv


`select.py`内の配列`**TARGETLABELS**`の中身を、選択したいクラス名のリストに書き換える。
[クラス名の参考](https://research.google.com/audioset/dataset/index.html)

### 動作
初めに、[クラス名の参考](https://research.google.com/audioset/dataset/index.html)をもとにcsvデータがほしいクラス名探し、`select.py`内の配列`**TARGETLABELS**`の中身にリストとして記す。
例：
> TARGETLABELS=[
    'Speech',
    'Animal',
    'Wind',
    'Music',
    'Silence',
]


次に
> python select.py  


を実行し、抽出元にしたいファイルを選択する。
> 終了しました!!!  


の表示が出れば成功。
抽出後のcsvは`result/[クラス名].csv`の形式で追加される。
また、抽出に用いたクラス名とラベルの対応表が`result/label.csv`に追加される。
