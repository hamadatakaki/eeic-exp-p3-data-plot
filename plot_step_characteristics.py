import argparse
from pathlib import Path
import yaml


from ltspice.reader.Step import LTspiceStepReader
from ltspice.drawer.SimpleStep import SimpleStepDrawer


def check_args(args):
    confpath = Path(args.config) if args.config is not None else None
    config = None

    if bool(confpath) and confpath.exists():
        with open(confpath, "r") as r:
            stream = r.read()

        config = yaml.safe_load(stream)

    return LTspiceStepReader(args.input_txt, args.step_txt), config


def main(args):
    reader, config = check_args(args)

    drawer = SimpleStepDrawer(reader, args.output_image, config)
    drawer.save_figure()
    drawer.logging()


if __name__ == "__main__":
    desc_msg = "plotting frequency characteristics (amplitudes, phases)."
    parser = argparse.ArgumentParser(description=desc_msg)

    parser.add_argument(
        "-i", "--input_txt", required=True, help="LTspice export input-pulse data path."
    )
    parser.add_argument(
        "-s", "--step_txt", required=True, help="LTspice export output-step data path."
    )
    parser.add_argument(
        "-o", "--output_image", required=True, help="Plot image save path."
    )
    parser.add_argument("-c", "--config", required=False, help="Plot configure.")

    args = parser.parse_args()

    main(args)
