from pathlib import Path

from ltspice.reader.BaseReader import BaseReader


class LTspicePolarReader(BaseReader):
    def __init__(self, path) -> None:
        self.freqs = []
        self.amps = []
        self.phases = []
        self.path = Path(path)

        self.readfile()
        self.analysis()

    def readfile(self):
        self.txt = self._readfile(self.path, True)

    def analysis(self):
        lines = self.txt.split("\n")
        body = lines[1:]
        self.datasize = len(body)

        self._check_head(lines[0])

        for i, b in enumerate(body):
            self._check_body(b, i)
            b_split = b.split("\t")

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
