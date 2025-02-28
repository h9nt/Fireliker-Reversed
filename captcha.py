from io         import BytesIO
from PIL        import Image, ImageTk
import tkinter  as tk
from curl_cffi  import requests
from tls_client import Session


class FireLikerSolver:
    def __init__(self):
        self.captcha_url = "https://fireliker.com/fire-captcha.php"
        self.session = requests
        self.client = Session(client_identifier="120")
        self.cookies = {}  # have to implement to get the cookies from it before

    def get_captcha(self):
        response = self.session.get(
            self.captcha_url,
            headers={
                "Connection": "keep-alive",
                "Cookie": self.cookies,
                "Host": "fireliker.com",
                "Referer": "https://fireliker.com/secure.php",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            },
            verify=False,
        )
        image = Image.open(BytesIO(response.content))
        root = tk.Tk()
        root.title("Captcha Verification")
        image_tk = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=image_tk)
        label.pack()
        root.mainloop()


FireLikerSolver().get_captcha()
