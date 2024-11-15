import time

from data.urls import Urls
from pages.download_page import DownLoadPage


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        page = DownLoadPage(driver, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
