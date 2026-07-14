from PIL import Image

try:
    img = Image.open("images/남한.png")
    print("정상입니다!")
    print(img.format)
    print(img.size)
except Exception as e:
    print(e)