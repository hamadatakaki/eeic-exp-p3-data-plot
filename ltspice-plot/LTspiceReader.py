from pathlib import Path


class LTspiceReader(object):
    def __init__(self, path):
        self.freqs = []
        self.names = []
        self.bodies = {}
        self.path = Path(path)

        self.construction_analysis()

    def construction_analysis(self):
        self.__load_txt()
        self.__analysis_header()
        self.__analysis_body()

    def __load_txt(self):
        assert self.path.exists(), f"[error] text file does not exist: {self.path}"

        # TODO: 文字コード対策

        with open(self.path, "r") as r:
            txt = r.read()

        lines = list(txt.strip().split("\n"))
        self.lines_num = len(lines)

        self.header = lines[0]
        self.bodies = lines[1:]
        self.samples = len(self.bodies)

    def __analysis_header(self):
        heads = list(self.header.split("\t"))
        self.names = heads[1:]
        self.graphs = {title: [] for title in self.names}

    def __analysis_body(self):
        for index, line in enumerate(self.bodies):
            self.__analysis_line(line, index)

    def __analysis_line(self, line, index):
        # TODO: bodyの解析にregexを使うように変更

        body = list(line.split("\t"))
        if len(body) != len(self.names) + 1:
            print(f"[warning] data is lacking at line: {index+2}")
            return

        self.freqs.append(float(body[0]))

        for (title, data_str) in zip(self.names, body[1:]):
            db, th = [float(f) for f in data_str[1:-1].split("dB,")]
            self.graphs[title] += [(db, th)]

    def logging_statistics(self):
        maxf, minf = max(self.freqs), min(self.freqs)
        print(f"Max frequency: {maxf} [Hz]")
        print(f"Min frequency: {minf} [Hz]")
        print(f"Sample size: {self.samples}")

    def frequencies(self):
        return self.freqs

    def graph_names(self):
        return self.names

    def amplitudes(self, name):
        assert name in self.names

        return [db for (db, _) in self.graphs[name]]

    def phases(self, name):
        assert name in self.names

        return [th for (_, th) in self.graphs[name]]


if __name__ == "__main__":
    path = "./data/test.txt"
    reader = LTspiceReader(path)
    reader.logging_statistics()
