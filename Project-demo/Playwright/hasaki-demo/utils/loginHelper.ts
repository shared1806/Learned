import { Page } from '@playwright/test';
import { handlePopups } from './popupHelper';
export async function login(page: Page, username: string, password: string): Promise<void> {
    await page.setViewportSize({ width: 1920, height: 1080 });
    // Xóa cache, cookie, local/sessionStorage để tránh session cũ ảnh hưởng
    // await page.context().clearCookies();
    // await page.goto('https://hasaki.vn/', { waitUntil: 'load' });
    // await page.evaluate(() => {
    // localStorage.clear();
    // sessionStorage.clear();
    // });
    await page.goto('https://hasaki.vn/');
    // Tắt popup
    await handlePopups(page);
    await page.hover('.item_login');
    await page.click('#hskLoginButton');
    // Điền thông tin đăng nhập
    await page.fill('#username', username);
    await page.fill('#password', password);
    // Click nút đăng nhập
    await page.locator('button:has-text("Đăng nhập")').click();
    
}
