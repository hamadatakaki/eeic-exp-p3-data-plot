import argparse
from pathlib import Path
import sys

from ltspice.drawer.CompareFreq import CompareFreqDrawer
from ltspice.utils import load_yaml


def check_args(args):
    confpath = Path(args.config) if args.config is not None else None
    config = None

    if bool(confpath) and confpath.exists():
        config = load_yaml(confpath)
    else:
        print(f"[error] config `{confpath}` not exist.")
        sys.exit(1)

    return config


def main(args):
    config = check_args(args)

    drawer = CompareFreqDrawer(args.output_image, config)
    drawer.save_figure()
    drawer.logging()


if __name__ == "__main__":
    desc_msg = "plotting frequency characteristics (amplitudes, phases)."
    parser = argparse.ArgumentParser(description=desc_msg)

    parser.add_argument(
        "-o", "--output_image", required=True, help="Plot image save path."
    )
    parser.add_argument("-c", "--config", required=False, help="Plot configure.")

    args = parser.parse_args()

    main(args)
