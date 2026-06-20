const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    deviceScaleFactor: 2,
    viewport: { width: 1600, height: 800 }
  });
  
  const page = await context.newPage();
  
  // Navigate to the HTML file
  const filePath = '/home/z/my-project/download/03_level_design.html';
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle' });
  
  // Wait for fonts to load
  await page.waitForTimeout(3000);
  
  // Get the full page height
  const bodyHeight = await page.evaluate(() => document.body.scrollHeight);
  const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
  
  console.log(`Page dimensions: ${bodyWidth}x${bodyHeight}`);
  console.log(`Output at 2x: ${bodyWidth * 2}x${bodyHeight * 2}`);
  
  // Take full page screenshot
  await page.screenshot({
    path: '/home/z/my-project/download/03_level_design.png',
    fullPage: true,
  });
  
  console.log('Screenshot saved to /home/z/my-project/download/03_level_design.png');
  
  await browser.close();
})();
