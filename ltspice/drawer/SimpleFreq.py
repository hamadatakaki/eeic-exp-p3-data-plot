from ltspice.drawer.base import BaseDrawer


class SimpleFreqDrawer(BaseDrawer):
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
