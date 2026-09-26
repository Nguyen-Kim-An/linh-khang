image_override_css = """
<!-- ============================================================== -->
<!-- KHU VỰC THAY ẢNH CƯỚI DỄ DÀNG (TẬP TRUNG TẤT CẢ VÀO ĐÂY) -->
<!-- Bạn chỉ cần sửa số ảnh (1.jpg đến 16.jpg) ở ngay bên dưới: -->
<!-- ============================================================== -->
<style id="wedding-photos-override">
  /* Tự động căn giữa và co giãn ảnh đẹp mắt, không bị méo */
  #IMAGE130 > .ladi-image > .ladi-image-background,
  #IMAGE210 > .ladi-image > .ladi-image-background,
  #IMAGE211 > .ladi-image > .ladi-image-background,
  #IMAGE78 > .ladi-image > .ladi-image-background,
  #IMAGE80 > .ladi-image > .ladi-image-background,
  #IMAGE77 > .ladi-image > .ladi-image-background,
  #IMAGE187 > .ladi-image > .ladi-image-background,
  #IMAGE241 > .ladi-image > .ladi-image-background,
  #IMAGE242 > .ladi-image > .ladi-image-background,
  #IMAGE243 > .ladi-image > .ladi-image-background,
  #IMAGE244 > .ladi-image > .ladi-image-background,
  #IMAGE245 > .ladi-image > .ladi-image-background,
  #IMAGE85 > .ladi-image > .ladi-image-background,
  #IMAGE230 > .ladi-image > .ladi-image-background,
  #IMAGE231 > .ladi-image > .ladi-image-background,
  #IMAGE233 > .ladi-image > .ladi-image-background,
  #IMAGE234 > .ladi-image > .ladi-image-background,
  #IMAGE235 > .ladi-image > .ladi-image-background,
  #IMAGE96 > .ladi-image > .ladi-image-background {
    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    top: 0px !important;
    left: 0px !important;
    width: 100% !important;
    height: 100% !important;
  }

  /* 1. ẢNH BÌA LỚN TRÊN ĐẦU TRANG */
  #IMAGE130 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/1.jpg") !important;
  }

  /* 2. CHÚ RỂ (Khang) & CÔ DÂU (Linh) */
  #IMAGE210 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/3.jpg") !important; /* Chú rể Khang */
  }
  #IMAGE211 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/2.jpg") !important; /* Cô dâu Linh */
  }

  /* 3. 3 ẢNH THIỆP MỜI TIỆC (Lễ Vu Quy, Thành Hôn, Tiệc Cưới) */
  #IMAGE78 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/4.jpg") !important; /* Lễ Vu Quy */
  }
  #IMAGE80 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/5.jpg") !important; /* Lễ Thành Hôn */
  }
  #IMAGE77 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/6.jpg") !important; /* Tiệc Cưới CTM */
  }

  /* 4. ẢNH PHẦN ĐẾM NGƯỢC (Save The Date - Khung ngang) */
  #IMAGE187 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/10.jpg") !important; /* Ảnh ngang */
  }

  /* 5. DẢI PHIM 5 ẢNH (Film strip cuộn ngang) */
  #IMAGE241 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/7.jpg") !important;
  }
  #IMAGE242 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/8.jpg") !important;
  }
  #IMAGE243 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/9.jpg") !important;
  }
  #IMAGE244 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/11.jpg") !important;
  }
  #IMAGE245 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/12.jpg") !important;
  }

  /* 6. ALBUM ẢNH CƯỚI (Album of love - 6 ảnh) */
  #IMAGE85 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/13.jpg") !important; /* Ảnh lớn trên cùng */
  }
  #IMAGE230 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/14.jpg") !important;
  }
  #IMAGE231 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/15.jpg") !important;
  }
  #IMAGE233 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/4.jpg") !important;
  }
  #IMAGE234 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/11.jpg") !important;
  }
  #IMAGE235 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/12.jpg") !important;
  }

  /* 7. ẢNH LỜI CẢM ƠN DƯỚI CHÂN TRANG (Thank you!) */
  #IMAGE96 > .ladi-image > .ladi-image-background {
    background-image: url("./assets/images/sorted/16.jpg") !important;
  }
</style>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# remove old override if any
import re
html = re.sub(r'<!-- ===+ -->\s*<!-- KHU VỰC THAY ẢNH CƯỚI.*?<\/style>', '', html, flags=re.DOTALL)

target = '</head>'
pos = html.find(target)
if pos != -1:
    new_html = html[:pos] + image_override_css + "\n" + html[pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('SUCCESS: Injected wedding photos override block!')
else:
    print('ERROR: </head> not found')
