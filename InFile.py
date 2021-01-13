class InFile:

    def __init__(self, infile):
        self.infile = open(infile, encoding="utf-8")

    def __iter__(self):
        return self

    def read(self, *args, **kwargs):
        res = ''
        while True:
            line = self.infile.readline()
            if not line:
                self.infile.close()
                return line
            if line[:4] == '====':
                if len(res) > 0:
                    break
            else:
                res += line
        return res
