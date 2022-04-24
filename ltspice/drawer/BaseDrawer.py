import matplotlib.pyplot as plt
import japanize_matplotlib
from ltspice.utils import safe_dictionary_access, none_wrap

japanize_matplotlib.japanize()


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
