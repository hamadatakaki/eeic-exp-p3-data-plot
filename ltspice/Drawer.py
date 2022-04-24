from ltspice.drawer.SimpleFreq import SimpleFreqDrawer

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
    drawer = SimpleFreqDrawer(reader, output_path, config)
    drawer.save_figure()
