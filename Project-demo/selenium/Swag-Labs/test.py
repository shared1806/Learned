import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.selenium_utils import click_element, send_keys_to_element, get_element_text
from utils.config import Config
import time
import base64
from HTMLTestRunner import HTMLTestRunner  

class test_Navigation_Bar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(f"{Config.BASE_URL}")

        send_keys_to_element(self.driver, By.ID, 'user-name', Config.USERNAME)
        send_keys_to_element(self.driver, By.ID, 'password', Config.PASSWORD)
        click_element(self.driver, By.ID, 'login-button') 

    def test_title(self):
        expected_title = "Swag Labs 1"
        actual_title = get_element_text(self.driver, By.CLASS_NAME, 'app_logo')
        # Sử dụng self.assert để kiểm tra, nhưng không raise exception ngay lập tức
        try:
            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}' but got '{actual_title}'")
        except AssertionError as e:
            self.save_screenshot_to_report('test_title_failed')
            self.fail(f"Test failed: {str(e)}")  # Báo lỗi nhưng không dừng execution

    # Hàm chụp ảnh màn hình và trả về base64 để hiển thị trong báo cáo
    def save_screenshot_to_report(self, test_name):
        screenshot_base64 = self.driver.get_screenshot_as_base64()
        screenshot_path = f"report/{test_name}.png"
        with open(screenshot_path, "wb") as f:
            f.write(base64.b64decode(screenshot_base64))

        # Đính kèm hình ảnh dưới dạng HTML vào báo cáo
        with open(screenshot_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            img_tag = f'<img src="data:image/png;base64,{encoded_image}" alt="{test_name} screenshot" style="width:600px;height:auto;">'
            self._add_image_to_report(img_tag)

    # Hàm để thêm HTML vào report
    def _add_image_to_report(self, img_tag):
        if hasattr(self, '_outcome'):  # Python 3.x
            if self._outcome.errors:
                self._outcome.errors[-1][1] = self._outcome.errors[-1][1] + '\n' + img_tag

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        testRunner=HTMLTestRunner(
            output='report',  # Thư mục lưu báo cáo
            report_title="Test Report with Screenshots",  # Tiêu đề báo cáo
            combine_reports=True,  # Kết hợp tất cả test case vào một báo cáo
            add_timestamp=True  # Thêm timestamp vào báo cáo
        )
    )
