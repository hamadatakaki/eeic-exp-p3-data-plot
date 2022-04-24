# LTspice exported data plot

## usage

1. LTspiceの `export data` 機能でプロットしたいデータを `.txt` 形式にしてダウンロードする

Formatには `Polar: (dB, deg)` を指定してください。

この時、1つの波形のみが描画されたシミュレーション画面から `.txt` を抽出してください。

2. このリポジトリをcloneしてくる

```
> git clone https://github.com/hamadatakaki/ltspice-plot.git
```

3. セットアップ

`requirements.txt` から依存ライブラリを入れます。

```
> pip3 install -r requirements.txt
```

直接pipで入れずに仮想環境を挟む場合は次のようにするといいです。

```
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
```

4. 実行

生成したいグラフに対する `.py` を [examples](#examples) から選んで実行します。

```
> python3 <.py file>
> python <.py file> # 仮想環境を挟む場合こうなるはず
```

# examples

## シンプルな周波数特性図

![SBWFC](fig/butterworth_freq_char.png)

対応するファイルは `plot_characteristics.py` です。

```shell
> python3 plot_characteristics -i <input txt path> -o <image dst path> -c config/simple_drawer.yaml
```

`<imput txt path>` は周波数特性図に変換したい `.txt` のパスを、 `<image dst path>` は周波数特性図の保存先のパス（拡張子はpng）を指定してください。

`-c` オプションの引数はなるべく変更しないでください。

```shell
## usage
> python3 plot_characteristics.py -i data/butterworth.txt -o fig/butterworth_freq_char.png -c config/simple_drawer.yaml
# LTspice Reader
text path: data/butterworth.txt
sample size: 401
frequencies range [Hz]: [1000.0, 10000000.0]
amplitude range [dB] [-0.0163213687717722, -120.00101217432]
phase ranges [deg]: [-1.1443753012390516, -268.8528622415462]

# Drawer
figure size: [7.2 4.8]
```
