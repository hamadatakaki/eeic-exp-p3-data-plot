import matplotlib.pyplot as plt

from LTspiceReader import LTspiceReader

if __name__ == "__main__":
    input_path = "data/test.txt"
    output_path = "data/figure.png"

    reader = LTspiceReader(input_path)
    key = "V(n003)"

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(
        reader.frequencies(),
        reader.amplitudes(key),
        color="red",
        label=f"{key} amplitudes[dB]",
    )
    plt.xscale("log")
    plt.title("amplitudes")
    plt.savefig(output_path)
