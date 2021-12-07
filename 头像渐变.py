from PIL import Image

# 读取图片
guoqi = Image.open('国旗.png')
touxiang = Image.open('头像.jpg')

# 获取国旗的尺寸
x,y = guoqi.size
# 根据需求，设置左上角坐标和右下角坐标（截取的是正方形）
# Image.crop(box): 截取图片，box是一个(左，上，右，下)的元组，也就是相对于左上角(0,0)的像素值
# quyu = guoqi.crop((5,10, x,y-5))
quyu = guoqi.crop((0,0, x,y-5))

# 获取头像的尺寸
w,h = touxiang.size
# 将区域尺寸重置为头像的尺寸
quyu = quyu.resize((w,h))
# 透明渐变设置
for i in range(w):
    for j in range(h):
        color = quyu.getpixel((i, j))
        alpha = 255-i//2
        if alpha < 0:
            alpha=0
        color = color[:-1] + (alpha, )
        quyu.putpixel((i, j), color)

#touxiang.show()
#quyu.show()

# 粘贴到头像并保存 
touxiang.paste(quyu,(0,0),quyu)
touxiang.save('五星红旗半透明渐变头像.png')
#touxiang.show()
 
