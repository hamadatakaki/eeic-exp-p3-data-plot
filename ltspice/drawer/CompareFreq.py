import matplotlib.pyplot as plt
import japanize_matplotlib

from ltspice.drawer.SimpleFreq import SimpleFreqDrawer
from ltspice.reader.Polar import LTspicePolarReader
from ltspice.utils import load_yaml

# from ltspice.utils import safe_dictionary_access, none_wrap

japanize_matplotlib.japanize()


# TODO: 動く


class CompareFreqDrawer(object):
    def __init__(self, figure_path, config):
        self.figure_path = figure_path

        self.fig = plt.figure()
        self.drawers = []
        self.names = []

        figsize = config["figure"]["figsize"]
        self.fig.set_size_inches(figsize)

        conf_arr = [(k, v) for k, v in config["figure"]["options"].items()]

        for name, conf in conf_arr:
            reader = LTspicePolarReader(conf["input"])
            config = load_yaml(conf["config"])
            drawer = SimpleFreqDrawer(reader, figure_path, config)
            self.names.append(name)
            self.drawers.append(drawer)

        [self.fig.add_subplot(dr.ax) for dr in self.drawers]

    def save_figure(self):
        self.fig.savefig(self.figure_path)

    def logging(self):
        for (name, dr) in zip(self.names, self.drawers):
            print(f"== {name} ==")
            print()
            dr.logging()
            print()
