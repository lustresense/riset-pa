const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    deviceScaleFactor: 2,
    viewport: { width: 1680, height: 900 }
  });
  const page = await context.newPage();

  // Load the HTML file
  await page.goto('file:///home/z/my-project/download/04_cnn_behavior_mapping.html', {
    waitUntil: 'networkidle',
  });

  // Wait for fonts to load
  await page.waitForTimeout(3000);

  // Get the full page dimensions
  const dimensions = await page.evaluate(() => {
    return {
      width: document.documentElement.scrollWidth,
      height: document.documentElement.scrollHeight
    };
  });

  console.log(`Content dimensions: ${dimensions.width} x ${dimensions.height}`);

  // Take full page screenshot
  await page.screenshot({
    path: '/home/z/my-project/download/04_cnn_behavior_mapping.png',
    fullPage: true,
  });

  console.log('Screenshot saved!');

  await browser.close();
})();
