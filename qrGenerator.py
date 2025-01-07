import qrcode

class MyQR:
    def __init__(self, size: int):
        self.qr=qrcode.QRCode(box_size=size)

    def createQr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter the text to generate qr: ")

        try:
            self.qr.add_data(user_input)
            qr_image=self.qr.make_image(fill_color=fg, back_colot=bg)
            qr_image.save(file_name)
            print(f"Successfully created!! {file_name} ")

        except Exception as e:
            print("error: ",e)

def main():
    myqr = MyQR(size=30)
    myqr.createQr("sample.png", "black", "white")

if __name__=="__main__":
    main()