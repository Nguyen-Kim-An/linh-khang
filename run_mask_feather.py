import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mask Feather Test</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body, html { width: 100%; height: 100%; overflow: hidden; background: #000; }

  #wedding-cover-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999999999;
    overflow: hidden;
    background: radial-gradient(circle at center, #1b2818 0%, #0d150b 100%);
  }

  .cover-bg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    background-image: url("./assets/images/sorted/theme.png");
    background-size: auto 84vh;
    background-position: center center;
    background-repeat: no-repeat;
    -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 7%, black 93%, transparent 100%);
    mask-image: linear-gradient(to bottom, transparent 0%, black 7%, black 93%, transparent 100%);
  }

  /* Lớp gradient tối rất nhẹ trên toàn ảnh */
  .cover-overlay-gradient {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.08) 0%,
      rgba(0, 0, 0, 0.02) 40%,
      rgba(0, 0, 0, 0.18) 100%
    );
    pointer-events: none;
  }

  /* Hotspot con dấu */
  #cover-wax-seal-hotspot {
    position: absolute;
    left: 50vw;
    top: calc(50vh + 84vh * 0.2269);
    width: clamp(55px, 84vh * 0.11, 95px);
    height: clamp(55px, 84vh * 0.11, 95px);
    transform: translate(-50%, -50%);
    border-radius: 50%;
    cursor: pointer;
    background: transparent;
    border: none;
  }

  #cover-wax-seal-hotspot::after {
    content: "";
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    border: 2px solid rgba(255, 215, 0, 0.75);
    animation: sealRipple 2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
    pointer-events: none;
  }

  @keyframes sealRipple {
    0% { transform: scale(0.85); opacity: 0.9; }
    100% { transform: scale(1.35); opacity: 0; }
  }
</style>
</head>
<body>
  <div id="wedding-cover-overlay">
    <div class="cover-bg"></div>
    <div class="cover-overlay-gradient"></div>
    <button id="cover-wax-seal-hotspot" type="button"></button>
  </div>
</body>
</html>
"""

with open('d:/Download/wedding/test_mask_feather.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.set_window_size(412, 915)
driver.get('http://localhost:8080/test_mask_feather.html')
time.sleep(0.5)
driver.save_screenshot('d:/Download/wedding/test_mask_feather.png')
driver.quit()
print('Saved test_mask_feather.png')
