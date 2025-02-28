import execjs

# Base signer for The signature like this its the payload
#zA5iw3KnnRIZZxjs=3ac2&_tac=7b9e6831b5a12e4897d4d7fec39f78c7.ec374ed3&submit=Continue


class Signer:
    def __init__(self):
        self.code = open("_.js", "r").read()
        self.ctx = execjs.compile(self.code)

    def get_value(self):
        return self.ctx.call("sign")
