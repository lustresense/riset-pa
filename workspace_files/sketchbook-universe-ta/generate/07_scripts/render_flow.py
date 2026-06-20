import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_image(html_path, output_path, selector='#root', width=1500, scale=2):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={'width': width, 'height': 800},
            device_scale_factor=scale
        )
        await page.goto(f'file://{html_path}', wait_until='networkidle')
        await page.wait_for_timeout(500)
        
        el = page.locator(selector)
        bbox = await el.bounding_box()
        if bbox:
            fit_w = max(width, int(bbox['width'] + 120))
            fit_h = int(bbox['height'] + 120)
            await page.set_viewport_size({'width': fit_w, 'height': fit_h})
            await page.wait_for_timeout(300)
        
        await el.screenshot(path=output_path)
        await browser.close()
        
        size_kb = os.path.getsize(output_path) / 1024
        print(f'Exported: {output_path} ({size_kb:.0f} KB)')

if __name__ == '__main__':
    html_path = '/home/z/my-project/download/user_flow.html'
    output_path = '/home/z/my-project/download/02_user_flow.png'
    asyncio.run(html_to_image(html_path, output_path, width=1500, scale=2))
