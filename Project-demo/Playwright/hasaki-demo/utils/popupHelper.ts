import { Page } from '@playwright/test';

export async function handlePopups(page: Page): Promise<void> {
    // Kiểm tra xem popup Onesignal có xuất hiện không và click nếu có
    const onesignalPopup = page.locator('#onesignal-slidedown-allow-button');
    if (await onesignalPopup.isVisible()) {
        await onesignalPopup.click();
    }

    // Kiểm tra và click vào button chấp nhận cookies nếu nó hiển thị
    const acceptCookiesButton = page.locator('#acceptCookies');
    if (await acceptCookiesButton.isVisible()) {
        await acceptCookiesButton.click();
    }
}