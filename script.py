# 画像を16*16のドット絵に変換します。
# 色味を変えたい場合はPILのImageEnhanceを使用してください。
# あらかじめ正方形にトリミングしておくことを推奨します。正方形でない画像を入力した場合は自動的にトリミングされます。

from PIL import Image

img = Image.open(r"target.png")

# 画像が正方形でない
if img.size[0] != img.size[1]:
  size = min(img.size)
  img = img.crop((0, 0, size, size))

l = img.size[0]/16 # 16等分したサイズ

bg = Image.new("RGB", (512, 512), (255, 255, 255)) # ドット絵用の背景画像

color_codes = []
for i in range(16):
  for j in range(16):
    c = img.crop((l*j, l*i, l*(j+1), l*(i+1)))
    data = list(c.getdata())

    ave = [] # RGBの平均値
    for k in range(3):
      ave.append(sum([x[k] for x in data]) // (len(data)-1))

    hex_code = format(ave[0], "02x") + format(ave[1], "02x") + format(ave[2], "02x")
    color_codes.append(hex_code)

    dot = Image.new("RGB", (32, 32), (ave[0], ave[1], ave[2]))
    bg.paste(dot, (32*j, 32*i))

bg.save(r"output.png")
print(color_codes) # 256ドット分のカラーコード
