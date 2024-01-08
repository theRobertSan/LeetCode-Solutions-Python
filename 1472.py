class BrowserHistory:
    def __init__(self, homepage: str):
        self.curPos = 0
        self.urlPos = {self.curPos: homepage}
        self.size = len(self.urlPos)

    def visit(self, url: str):
        self.curPos += 1
        self.urlPos[self.curPos] = url
        self.size = self.curPos + 1

    def back(self, steps: int):
        self.curPos -= steps
        if self.curPos < 0:
            self.curPos = 0

        return self.urlPos[self.curPos]

    def forward(self, steps: int):
        self.curPos = self.curPos + steps
        if self.curPos >= self.size:
            self.curPos = self.size - 1

        return self.urlPos[self.curPos]
