#utf-8
# from PIL import ImageColor

# print(ImageColor.getcolor('red','RGBA'))

# from PIL import Image
# catIm = Image.open('/Users/VON/Downloads/code.jpg')
# print(catIm.size)

# width,height = catIm.size
# print(width)
# print(catIm.filename)
# print(catIm.format)
# catIm.save('zophie.jpg')

#new()函数
# from PIL import Image

# im = Image.new('RGBA',(100,200),'purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA',(20,20))
# im2.save('transparentImages.png')

#裁剪图片 粘贴
from PIL import Image
# catIm = Image.open('/Users/VON/Downloads/zophie.png')
# croppedIm = catIm.crop((355,345,565,560))
# croppedIm.save('cropped.png')

# catIm =Image.open('/Users/VON/Downloads/zophie.png')
# catCopyIm =catIm.copy()
# faceIm = catIm.crop((335,345,565,560))
# print(faceIm.size)
# catCopyIm.paste(faceIm,(0,0))
# catCopyIm.paste(faceIm,(400,500))
# catCopyIm.save('pasted.png')

#假定用Zophie的头平铺整个图像

# catIm = Image.open('/Users/VON/Downloads/zophie.png')
# faceIm = Image.open('/Users/VON/WorkSpace/cropped.png')

# catImWidth, catImHeight = catIm.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()

# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm,(left,top))
# catCopyTwo.save('tiled.png')

#调整图像大小
# catIm = Image.open('/Users/VON/Downloads/zophie.png')
# faceIm = Image.open('/Users/VON/WorkSpace/cropped.png')
# width, height = catIm.size
# quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
# quartersizedIm.save('quartersized.png')
# svelteIm = catIm.resize((width, height + 300))
# svelteIm.save('svelet.png')

#旋转和翻转图像
# catIm = Image.open('/Users/VON/Downloads/zophie.png')
# faceIm = Image.open('/Users/VON/WorkSpace/cropped.png')

# catIm.rotate(90).save('rotated90.png')
# catIm.rotate(180).save('rotated180.png')
# catIm.rotate(270).save('rotated270.png')

# #放大图像的尺寸，以适应整个旋转后的新图像
# catIm.rotate(6).save('rotated6.png')
# catIm.rotate(6,expand=True).save('rotated6_expanded.png')

# #镜像翻转
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

#更改单个像素  getpixel(x,y) putpixel((x,y),(RGBA或RGB))
# im = Image.new('RGBA', (100, 100))
# print(im.getpixel((0, 0)))

# for x in range(100):
#     for y in range(50):
#         im.putpixel((x, y), (210, 210, 210))

# from PIL import ImageColor
# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
# print(im.getpixel((0, 0)))
# print(im.getpixel((0, 50)))
# im.save('putPixel.png')
