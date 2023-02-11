import qrcode


class GeradorQrcode():
    def __init__(self, data):
        self.data = data

    def gerar(self):
        self.img = qrcode.make(self.data)
        self.img.save('Qrcode.png')


gerador = GeradorQrcode("OI")
gerar = gerador.gerar()
