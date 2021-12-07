from PIL import Image,ImageColor,ImageDraw

# 加载图片
pic = Image.open('闹闹.jpg')
x,y=pic.size
print(x,y)
#pic.show()
#print(pic.mode)
#print(pic.getpixel((22,10)))
#(pic.convert("L")).show()
#size=(969,1129)
#suoxiao=pic.thumbnail((100,300))
#pic.save('小闹闹.jpg')
#image_gray_resize = pic.resize((80, 80))
#image_gray_resize.show()
#image_gray_rotate = pic.rotate(90)
#image_gray_rotate.show()
#image_gray_flip_h = pic.transpose(Image.FLIP_LEFT_RIGHT)
#image_gray_flip_h.show()
#image_gray_flip_v = pic.transpose(Image.FLIP_TOP_BOTTOM)
#image_gray_flip_v.show()


#pic.info
#daxiao=pic.getbbox()  
#fenge=pic.split()
#print(daxiao)
#print(fenge)

#新建图片  PIL.Image.new(mode, size, color=0)
newpic=Image.new('RGBA',(500,500),(255,0,0,204))
newpic2=Image.new('RGB',(500,500),(100,100,170))
#newpic.show()


rgb_tup = ImageColor.getrgb("#ff0000cc")
#print(rgb_tup)


img = Image.open("闹闹.jpg")

print("origin image size\nwidth: {}\nheight: {}".format(*img.size))
crop_box = (0, 0, 240, 240)
img_crop = img.crop(crop_box)
print("cropped image size\nwidth: {}\nheight: {}".format(*img_crop.size))
#img_crop.save("dog_crop.jpeg")
#img_crop.show()

R,G,B=img.split()
R.show()
G.show()
B.show()

#getpixel((x, y)) 是获取对应像素点的颜色。
#putpixel((x, y), color) 是设置对应像素点的颜色。
 
