from ltspice.drawer.BaseDrawer import BaseDrawer


class SimpleStepDrawer(BaseDrawer):
    def __init__(self, step_reader, figure_path, config):
        super().__init__(figure_path, config)

        self.configure()

        self.step_reader = step_reader

        for key in ["pulse", "step"]:
            self.draw(key)

        self.ax.legend(loc=self.legend_loc)
        self.fig.tight_layout()

    def configure(self):
        super().configure()

        # legend_loc
        self.legend_loc = self.safe_config_access(["legend_loc"], "lower right")

        # y-axis label
        ylabel = self.safe_config_access(["ylabel"], "")
        self.ax.set_ylabel(ylabel)

    def draw(self, key):
        assert key in ["pulse", "step"]

        xs = self.step_reader.times

        if key == "pulse":
            ys = self.step_reader.pulses
        else:
            ys = self.step_reader.steps

        color = self.safe_config_access(["lines", key, "color"], "black")
        legend = self.safe_config_access(["lines", key, "legend"], "")

        self.ax.plot(xs, ys, color=color, label=legend, lw=1)

    def logging(self):
        print("# LTspice Reader")
        self.step_reader.logging()
        print("\n# Drawer")
        print("figure size:", str(self.fig.get_size_inches()))
