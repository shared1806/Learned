// import { test, expect } from '@playwright/test';
// import { login } from '../utils/loginHelper';


// test.describe('Login', () => {
//     test('Login Successful', async ({ page }) => {
//         await login(page, '0386584244', '123456789Aa@');
//         await expect(page.locator('.text_1_header span')).toHaveText('THI');
//     });

//     test('Login with Invalid Username or Password', async ({ page }) => {
//         await login(page, 'invalid_user', 'invalid_pass');
//         await expect(page.locator('.showMessageError .alert')).toHaveText('Tên đăng nhập hoặc mật khẩu không khớp !');
//     });

//     test('Login with Empty Username', async ({ page }) => {
//         await login(page, '', '123456789Aa@');
//         await expect(page.locator('.showMessageError .alert')).toHaveText('Vui lòng nhập tên đăng nhập');
//     });
    
//     test('Login with Empty Password', async ({ page }) => {
//         await login(page, '0386584244', '');
//         await expect(page.locator('.showMessageError .alert')).toHaveText('Vui lòng nhập mật khẩu');
//     });

//     test('Login with Empty Username and Password', async ({ page }) => {
//         await login(page, '', '');
//         await expect(page.locator('.showMessageError .alert')).toHaveText('Vui lòng nhập tên đăng nhập');
//     }); 
// })