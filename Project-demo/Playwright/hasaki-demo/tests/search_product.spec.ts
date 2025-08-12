import { test, expect } from '@playwright/test';
import { login } from '../utils/loginHelper';

test.describe('searchProduct', () => {
    test('Search Product', async ({ page }) => {
        await login(page, '0386584244', '123456789Aa@');
        await page.fill('#search', 'Nước Tẩy Trang Bioderma Dành Cho Da Nhạy Cảm 500ml Sensibio H2O');
        await page.click('.btn_submit_search');
        await expect(page.locator('h1')).toHaveText('Nước Tẩy Trang Bioderma Dành Cho Da Nhạy Cảm 500ml Sensibio H2O');
    });
});

