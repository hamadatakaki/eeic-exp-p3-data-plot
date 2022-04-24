import matplotlib.pyplot as plt
from ltspice.utils import safe_dictionary_access, none_wrap


class BaseDrawer(object):
    def __init__(self, figure_path, config):
        self.figure_path = figure_path
        self.config = none_wrap(config, {})
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.configure()

    def save_figure(self):
        self.fig.savefig(self.figure_path)

    def configure(self):
        # title
        title = self.safe_config_access(["title"], "characters")
        self.ax.set_title(title)

        # figsize
        figsize = self.safe_config_access(["figsize"], [7.2, 4.8])
        self.fig.set_size_inches(figsize)

        # x-axis label
        xlabel = self.safe_config_access(["xlabel"], "")
        self.ax.set_xlabel(xlabel)

        # xscale
        xscale = self.safe_config_access(["xscale"], "linear")
        self.ax.set_xscale(xscale)

        # x-ticks
        xticks = self.safe_config_access(["xticks"], None)
        if xticks is not None:
            self.ax.set_xticks(*xticks)

    def safe_config_access(self, qs, failval):
        return safe_dictionary_access(self.config, ["figure"] + qs, failval)


class SimpleDrawer(BaseDrawer):
    def __init__(self, reader, figure_path, config):
        super().__init__(figure_path, config)

        self.ax_amp = self.ax
        self.ax_phase = self.ax_amp.twinx()

        self.configure()

        self.reader = reader

        for key in ["amp", "phase"]:
            self.draw(key)

        self.legend()

        self.fig.tight_layout()

    def draw(self, key):
        assert key in ["amp", "phase"]

        xs = self.reader.freqs

        if key == "amp":
            ax = self.ax_amp
            ys = self.reader.amps
        else:
            ax = self.ax_phase
            ys = self.reader.phases

        # line style
        style = self.safe_config_access(["axes", key, "style"], "solid")

        # y-axis label
        ylabel = self.safe_config_access(["axes", key, "ylabel"], "")
        ax.set_ylabel(ylabel)

        # y-axis scale
        yscale = self.safe_config_access(["axes", key, "yscale"], "linear")
        ax.set_yscale(yscale)

        ax.plot(xs, ys, color=self.color, label=ylabel, linestyle=style)

    def configure(self):
        super().configure()

        # color
        self.color = self.safe_config_access(["color"], "red")

        # legend_loc
        self.legend_loc = self.safe_config_access(["legend_loc"], "lower left")

    def legend(self):
        h1, l1 = self.ax_amp.get_legend_handles_labels()
        h2, l2 = self.ax_phase.get_legend_handles_labels()
        self.ax_amp.legend(h1 + h2, l1 + l2, loc="lower left")

    def logging(self):
        print("# LTspice Reader")
        self.reader.logging()
        print("\n# Drawer")
        print("figure size:", str(self.fig.get_size_inches()))


if __name__ == "__main__":
    from LTspiceReader import LTspicePolarReader
    import yaml

    input_path = "data/LPFButterWorthFreqChar_polar/LPFButterWorthFreqChar_dBdeg.txt"
    output_path = "data/figure.png"
    config_path = "config/simple_drawer.yaml"

    with open(config_path, "r") as r:
        config = yaml.safe_load(r.read())

    reader = LTspicePolarReader(input_path)
    reader.logging()
    drawer = SimpleDrawer(reader, output_path, config)
    drawer.save_figure()
