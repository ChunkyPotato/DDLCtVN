# Sayori Cafe (s21)
image s_cafe_bg:
    "mod_assets/Sayonnaise/s_cafe.png"      #cafe base
image s_cafe_bg2:
    "mod_assets/Sayonnaise/s_cafe_2.png"    #cafe base sundown

image sayori cafe_d:
    "mod_assets/Sayonnaise/s_cafe_d.png"    #happy/mouth open
    crop(0, 0, 1920, 1080)
    size (1280, 720)
image sayori cafe_h:
    "mod_assets/Sayonnaise/s_cafe_h.png"    #happy/smiling
    crop(0, 0, 1920, 1080)
    size (1280, 720)
image sayori cafe_l:
    "mod_assets/Sayonnaise/s_cafe_l.png"    #worried/looking away
    crop(0, 0, 1920, 1080)
    size (1280, 720)
image sayori cafe_s:
    "mod_assets/Sayonnaise/s_cafe_s.png"    #sad
    crop(0, 0, 1920, 1080)
    size (1280, 720)
image sayori cafe_w:
    "mod_assets/Sayonnaise/s_cafe_w.png"    #lustful/owo
    crop(0, 0, 1920, 1080)
    size (1280, 720)


# Transforms

transform tcommon2(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
        #yanchor 1.0 ypos 1.03
