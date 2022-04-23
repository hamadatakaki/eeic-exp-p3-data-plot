# LTspice exported data plot

## usage

1. LTspiceの `export data` 機能でプロットしたいデータを `.txt` 形式にしてダウンロードする

この時、Formatに `Polar: (dB, deg)` を指定する（デフォルトで `Polar: (dB, deg)` になっている）

2. このリポジトリをcloneしてくる

```
> git clone https://github.com/hamadatakaki/ltspice-plot.git
```

3. セットアップ

`requirements.txt` から依存ライブラリを入れる

```
> pip3 install -r requirements.txt
```

直接pipで入れずに仮想環境を挟む場合は次のようにするといい

```
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
```

4. 実行

```
# TODO: ここを直す
> python3 bin/hoge.py
> python bin/hoge.py  # 仮想環境を挟む場合こうなるはず
```

# examples

略
