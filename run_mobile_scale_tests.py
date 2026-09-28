import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

scales = [
    (85, 'scale_85vh'),
    (78, 'scale_78vh'),
    (72, 'scale_72vh'),
    (65, 'scale_65vh'),
]

template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mobile Scale Test</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body, html {{ width: 100%; height: 100%; overflow: hidden; background: #132014; }}

  #wedding-cover-overlay {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999999999;
    overflow: hidden;
    background-color: #152416;
    background-image: url("./assets/images/sorted/theme.png");
    background-size: auto {scale}vh;
    background-position: center center;
    background-repeat: no-repeat;
  }}

  /* Lớp gradient tối rất nhẹ trên toàn ảnh */
  .cover-overlay-gradient {{
    position: absolute;
    inset: 0;
    background: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.12) 0%,
      rgba(0, 0, 0, 0.02) 40%,
      rgba(0, 0, 0, 0.22) 100%
    );
    pointer-events: none;
  }}

  /* Hotspot con dấu */
  #cover-wax-seal-hotspot {{
    position: absolute;
    left: 50vw;
    top: calc(50vh + {scale}vh * 0.2269);
    width: clamp(55px, {scale}vh * 0.11, 100px);
    height: clamp(55px, {scale}vh * 0.11, 100px);
    transform: translate(-50%, -50%);
    border-radius: 50%;
    cursor: pointer;
    background: rgba(255, 0, 0, 0.25);
    border: none;
  }}

  #cover-wax-seal-hotspot::after {{
    content: "";
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    border: 2px solid rgba(255, 215, 0, 0.75);
    animation: sealRipple 2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
    pointer-events: none;
  }}

  @keyframes sealRipple {{
    0% {{ transform: scale(0.85); opacity: 0.9; }}
    100% {{ transform: scale(1.35); opacity: 0; }}
  }}
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

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.set_window_size(412, 915)

for val, name in scales:
    html_content = template.format(scale=val)
    with open('d:/Download/wedding/test_scale_temp.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    driver.get('http://localhost:8080/test_scale_temp.html')
    time.sleep(0.5)
    driver.save_screenshot(f'd:/Download/wedding/test_mobile_{name}.png')
    print(f'Saved test_mobile_{name}.png')

driver.quit()
