from PIL import Image

CODE_LIB = r"B8&WM#YXQO{}[]()I1i!pao;:,.    "
count = len(CODE_LIB)

def transform_ascii(resized_color_img):
    grayscale_img = resized_color_img.convert("L") # "L" converts the image to grayscale
    code_pic = ''
    for row in range(0, grayscale_img.size[1]):
        for col in range(0, grayscale_img.size[0]):
            grayscale_value = grayscale_img.getpixel((col, row))
            code_pic = code_pic + CODE_LIB[int(((count - 1) * grayscale_value) / 256)]
        code_pic = code_pic + "\n"
    return code_pic


color_img = Image.open("larry.png")

row_ratio = float(input("input height zoom ratio(default 1.0) : ") or "1.0")
col_ratio = float(input("input width zoom ratio(default 1.0) : ") or "1.0")

resized_color_img = color_img.resize((int(color_img.size[0] * col_ratio), int(color_img.size[1] * row_ratio)))
fo = open('result.txt', 'w')

trans_data = transform_ascii(resized_color_img)
print(trans_data)
fo.write(trans_data)
fo.close()