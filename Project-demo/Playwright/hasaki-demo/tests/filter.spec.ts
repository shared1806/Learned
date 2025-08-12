import { test, expect } from '@playwright/test';
import { login } from '../utils/loginHelper';

test.describe('Filter', () => {
    test.only('Filter', async ({ page }) => {
        await login(page, '0386584244', '123456789Aa@');
        
        // Search for product first
        await page.fill('#search', 'Nước Tẩy Trang Bioderma Dành Cho Da Nhạy Cảm 500ml Sensibio H2O');
        await page.click('.btn_submit_search');
        await expect(page.locator('h1')).toHaveText('Nước Tẩy Trang Bioderma Dành Cho Da Nhạy Cảm 500ml Sensibio H2O');
        
        // Then apply filter
        await page.click('p[title="Fullsize"]');
        await page.getByText('Mới nhất').click();
        await expect(page.getByText('Mới nhất')).toHaveClass(/bg-primary/);
        await expect(page.getByText('Dung tích: Fullsize')).toHaveText('Dung tích: Fullsize');
    });
});

