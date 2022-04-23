from pathlib import Path


class LTspicePolarReader(object):
    def __init__(self, path) -> None:
        self.freqs = []
        self.amps = []
        self.phases = []
        self.path = Path(path)

        self.readfile()
        self.analysis()

    def readfile(self):
        assert self.path.exists(), f"[error] File `{self.path}` must exist."
        with open(self.path, "rb") as rb:
            self.txt = rb.read().replace(b"\xb0", b"").decode("utf8").strip()

    def analysis(self):
        txt = self.txt.replace("\r", "")
        lines = txt.split("\n")
        head = lines[0]
        body = lines[1:]
        self.datasize = len(body)

        h_split = head.split("\t")
        if len(h_split) > 2:
            print("[warn] unnecessary element included in head:", head)
        elif len(h_split) < 2:
            print("[warn] some elements not exist in head:", head)

        for i, b in enumerate(body):
            b_split = b.split("\t")
            if len(b_split) > 2:
                print("[warn] unnecessary element included in body:")
                print(f"  {i+1}| {b}")
            elif len(b_split) < 2:
                print("[warn] some elements not exist in body:")
                print(f"  {i+1}| {b}")

            self.freqs.append(float(b_split[0]))
            polar = b_split[1]

            if self.check_polar_format(polar):
                amp, phase = polar[1:-1].split("dB,")
                self.amps.append(float(amp))
                self.phases.append(self.normalize_phase(float(phase)))
            else:
                print("[warn] invalid polar format discovered:")
                print(f"  {i+1}| {b}")

    def check_polar_format(self, polar):
        # TODO: use regex
        return polar[0] == "(" and polar[-1] == ")" and "dB," in polar

    def normalize_phase(self, phase):
        if phase < 0:
            phase += 360

        if phase >= 0:
            phase -= 360

        return phase

    def logging(self):
        print("text path:", self.path.absolute())
        print("sample size:", self.datasize)
        print("frequencies range [Hz]:", [self.freqs[0], self.freqs[-1]])
        print("amplitude range [dB]", [max(self.amps), self.amps[-1]])
        print("phase ranges [deg]:", [self.phases[0], self.phases[-1]])


class LTspiceCartesianReader(object):
    pass


if __name__ == "__main__":
    bwpath = "./data/LPFButterWorthFreqChar_polar/LPFButterWorthFreqChar_dBdeg.txt"
    bwreader = LTspicePolarReader(bwpath)
    bwreader.logging()

    cpath = "./data/LPFButterWorthFreqChar_polar/LPFChebyshevFreqChar_dBdeg.txt"
    creader = LTspicePolarReader(cpath)
    creader.logging()

    assert bwreader.freqs == creader.freqs
