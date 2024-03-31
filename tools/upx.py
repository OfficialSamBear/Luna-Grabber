import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.version = "4.2.0"
        self.url = f"https://github.com/upx/upx/releases/download/v{self.version}/upx-{self.version}-win64.exe"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.exe", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ExeFile("upx.exe") as exe_file:
            zip_file.extractall()
            shutil.move(f"./upx-{self.version}-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.exe")
        shutil.rmtree(f"upx-{self.version}-win64")


if __name__ == "__main__":
    UPX()
