from pathlib import Path

from ltspice.reader.BaseReader import BaseReader


class LTspiceStepReader(BaseReader):
    def __init__(self, pulse_path, step_path) -> None:
        self.times = []
        self.pulses = []
        self.steps = []
        self.pulse_path = Path(pulse_path)
        self.step_path = Path(step_path)

        self.readfile()
        self.analysis()

    def readfile(self):
        self.pulse_txt = self._readfile(self.pulse_path, False)
        self.step_txt = self._readfile(self.step_path, False)

    def analysis(self):
        plines = self.pulse_txt.split("\n")
        slines = self.step_txt.split("\n")

        self._check_head(plines[0])
        self._check_head(slines[0])

        body = list(zip(plines[1:], slines[1:]))
        self.datasize = len(list(body))

        for i, (b_pulse, b_step) in enumerate(body):
            self._check_body(b_pulse, i)
            self._check_body(b_step, i)

            bps, bss = b_pulse.split("\t"), b_step.split("\t")
            time_bp, time_bs = float(bps[0]), float(bss[0])
            assert time_bp == time_bs, "[error] times are not syncronized."

            self.times.append(time_bp)
            self.pulses.append(float(bps[1]))
            self.steps.append(float(bss[1]))

    def logging(self):
        print("pulse path:", self.pulse_path.absolute())
        print("step path:", self.step_path.absolute())
        print("sample size:", self.datasize)
        print("times range [s]:", [self.times[0], self.times[-1]])
        print("pulse voltage range [V]:", [self.pulses[0], self.pulses[-1]])
        print("step voltage range [V]:", [min(self.steps), max(self.steps)])


if __name__ == "__main__":
    step_path = "data/butterworth_step_char.txt"
    pulse_path = "data/step_input.txt"

    reader = LTspiceStepReader(pulse_path, step_path)
    reader.logging()
