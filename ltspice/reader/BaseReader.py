class BaseReader(object):
    def __init__(self):
        pass

    def _readfile(self, path, is_polar):
        assert path.exists(), f"[error] File `{path}` must exist."

        if is_polar:
            return self._read_polar(path)
        else:
            return self._read_onefile(path)

    def _read_polar(self, path):
        with open(path, "rb") as rb:
            txt = rb.read().replace(b"\xb0", b"").decode("utf8")
            return txt.strip().replace("\r", "")

    def _read_onefile(self, path):
        with open(path, "r") as r:
            return r.read().strip().replace("\r", "")

    def _check_head(self, head):
        h_split = head.split("\t")
        if len(h_split) > 2:
            print("[warn] unnecessary element included in head:", head)
        elif len(h_split) < 2:
            print("[warn] some elements not exist in head:", head)

    def _check_body(self, body, i):
        b_split = body.split("\t")
        if len(b_split) > 2:
            print("[warn] unnecessary element included in body:")
            print(f"  {i+1}| {body}")
        elif len(b_split) < 2:
            print("[warn] some elements not exist in body:")
            print(f"  {i+1}| {body}")
