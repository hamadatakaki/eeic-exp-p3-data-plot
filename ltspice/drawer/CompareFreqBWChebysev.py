from matplotlib import pyplot as plt
from ltspice.drawer.BaseDrawer import BaseDrawer


class CompareFreqCharsDrawer(BaseDrawer):
    def __init__(self, bw_reader, ch_reader, figure_path, config):
        self.figure_path = figure_path
        self.config = config

        assert bw_reader.freqs == ch_reader.freqs

        self.filters = ["bw", "chebyshev"]
        self.readers = {"bw": bw_reader, "chebyshev": ch_reader}

        self.fig = plt.figure()
        self.ax_amp = self.fig.add_subplot(1, 2, 1)
        self.ax_phase = self.fig.add_subplot(1, 2, 2)
        self.axes = {"amp": self.ax_amp, "phase": self.ax_phase}

        self.configure()
        for key in ["amp", "phase"]:
            self.draw(key)

        self.legend()
        self.fig.tight_layout()

    def configure(self):
        figsize = self.safe_config_access(["figsize"], [14.4, 4.8])
        self.fig.set_size_inches(figsize)

        # x-axis label, scale, ticks
        xlabel = self.safe_config_access(["xlabel"], "")
        xscale = self.safe_config_access(["xscale"], "linear")
        xticks = self.safe_config_access(["xticks"], None)

        for ax in [self.ax_amp, self.ax_phase]:
            # x-axis label, scale
            ax.set_xlabel(xlabel)
            ax.set_xscale(xscale)

            # x-ticks
            if xticks is not None:
                ax.set_xticks(*xticks)

    def draw(self, key):
        assert key in ["amp", "phase"]

        hier = ["axes", key]
        ax = self.axes[key]

        # configure by key: title, ylabel, yscale
        title = self.safe_config_access(hier + ["title"], "hoge特性")
        ylabel = self.safe_config_access(hier + ["ylabel"], "hoge[fuga]")
        yscale = self.safe_config_access(hier + ["yscale"], "linear")

        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_yscale(yscale)

        for filt in self.filters:
            xs = self.readers[filt].freqs
            ys = self.readers[filt].amps if key == "amp" else self.readers[filt].phases
            color = self.safe_config_access(["filter", filt, "color"], "black")

            ax.plot(xs, ys, color=color, label=ylabel)

    def legend(self):
        for key in ["amp", "phase"]:
            loc = self.safe_config_access(["axes", key, "legend_loc"], "lower left")
            self.axes[key].legend(loc=loc)

    def logging(self):
        for filt in self.filters:
            self.readers[filt].logging()
