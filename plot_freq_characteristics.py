import argparse
from pathlib import Path
import yaml


from ltspice.LTspiceReader import LTspicePolarReader
from ltspice.Drawer import SimpleFreqDrawer


def check_args(args):
    confpath = Path(args.config) if args.config is not None else None
    config = None

    if bool(confpath) and confpath.exists():
        with open(confpath, "r") as r:
            stream = r.read()

        config = yaml.safe_load(stream)

    return LTspicePolarReader(args.input_txt), config


def main(args):
    reader, config = check_args(args)

    drawer = SimpleFreqDrawer(reader, args.output_image, config)
    drawer.save_figure()
    drawer.logging()


if __name__ == "__main__":
    desc_msg = "plotting frequency characteristics (amplitudes, phases)."
    parser = argparse.ArgumentParser(description=desc_msg)

    parser.add_argument(
        "-i", "--input_txt", required=True, help="LTspice export data path."
    )
    parser.add_argument(
        "-o", "--output_image", required=True, help="Plot image save path."
    )
    parser.add_argument("-c", "--config", required=False, help="Plot configure.")

    args = parser.parse_args()

    main(args)
