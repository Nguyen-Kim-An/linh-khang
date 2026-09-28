import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mobile Seamless Scale</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body, html { width: 100%; height: 100%; overflow: hidden; background: #152416; }

  #wedding-cover-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999999999;
    overflow: hidden;
    background-color: #172718;
    background-image: url("./assets/images/sorted/theme.png");
    background-size: auto 82vh;
    background-position: center center;
    background-repeat: no-repeat;
  }

  /* Lớp phủ chuyển màu viền mềm mại trên và dưới để hòa tan 100% vào nền */
  .cover-overlay-gradient {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      #172718 0%,
      rgba(23, 39, 24, 0.7) 8%,
      rgba(0, 0, 0, 0.04) 25%,
      rgba(0, 0, 0, 0.04) 75%,
      rgba(23, 39, 24, 0.7) 92%,
      #172718 100%
    );
    pointer-events: none;
  }

  /* Hotspot con dấu */
  #cover-wax-seal-hotspot {
    position: absolute;
    left: 50vw;
    top: calc(50vh + 82vh * 0.2269);
    width: clamp(55px, 82vh * 0.11, 95px);
    height: clamp(55px, 82vh * 0.11, 95px);
    transform: translate(-50%, -50%);
    border-radius: 50%;
    cursor: pointer;
    background: rgba(255, 0, 0, 0.2);
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
    <div class="cover-overlay-gradient"></div>
    <button id="cover-wax-seal-hotspot" type="button"></button>
  </div>
</body>
</html>
"""

with open('d:/Download/wedding/test_seamless_mobile.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.set_window_size(412, 915)
driver.get('http://localhost:8080/test_seamless_mobile.html')
time.sleep(0.5)
driver.save_screenshot('d:/Download/wedding/test_seamless_mobile.png')
driver.quit()
print('Saved test_seamless_mobile.png')
