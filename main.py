from PIL import Image,ImageFilter,ImageDraw,ImageFont
from PIL.ImageFilter import(
    BLUR,CONTOUR,DETAIL,EDGE_ENHANCE,EDGE_ENHANCE_MORE,EMBOSS,FIND_EDGES,SMOOTH,SMOOTH_MORE,SHARPEN
)
print("----------------Efekt-Filtre-----------------")
print("1-Thumbnail")
print("2-Blur")
print("3-CONTOUR")
print("4-Edge")
print("5-Smooth")
print("6-Emboss")
print("7-Sharpen")
print("8-More Edge")
print("9-Enhance")
print("10-More Smooth")
print("11-Details")
print("12-Resmi Döndür")
print("13-Filigran Ekle")
print("14-PNG ye çevirme")
print("----------------CREATED BY HAROLD_FINCH-----------------")
a = int(input("Seçeneği Gir"))
if a == 1:
    resim = Image.open("a.jpg",mode='r')
    resim.thumbnail((150,150))
    resim.save("thumbnail.jpg")
    resim2 = Image.open("thumbnail.jpg")
    resim2.show()
if a == 2:
    resim = Image.open("a.jpg")
    blur = resim.filter(ImageFilter.BLUR)
    blur.show()
    blur.save("blur.jpg")
if a == 3:
    resim = Image.open("a.jpg")
    resim = resim.filter(CONTOUR)
    resim.show()
    resim.save("kontur.jpg")
if a == 4:
    resim = Image.open("a.jpg")
    resim = resim.filter(FIND_EDGES)
    resim.show()
    resim.save("edge.jpg")
if a == 5:
    resim = Image.open("a.jpg")
    resim = resim.filter(SMOOTH)
    resim.show()
    resim.save("smooth.jpg")
if a == 6:
    resim = Image.open("a.jpg")
    resim = resim.filter(EMBOSS)
    resim.show()
    resim.save("emboss.jpg")
if a == 7:
    resim = Image.open("a.jpg")
    resim = resim.filter(SHARPEN)
    resim.show()
    resim.save("sharpen.jpg")
if a == 8:
    resim = Image.open("a.jpg")
    resim = resim.filter(EDGE_ENHANCE_MORE)
    resim.show()
    resim.save("edgemore.jpg")
if a == 9:
    resim = Image.open("a.jpg")
    resim = resim.filter(EDGE_ENHANCE)
    resim.show()
    resim.save("enhance.jpg")
if a == 10:
    resim = Image.open("a.jpg")
    resim = resim.filter(SMOOTH_MORE)
    resim.show()
    resim.save("smooth_more.jpg")
if a == 11:
    resim = Image.open("a.jpg")
    resim = resim.filter(DETAIL)
    resim.show()
    resim.save("detail.jpg")
if a == 12:
    resim = Image.open("a.jpg")
    a = int(input("Derece"))
    resim = resim.rotate(a)
    resim.show()
    resim.save("rotate.jpg")
if a == 13:
    resim = Image.open("a.jpg")
    resim_genislik , resim_yukseklik = resim.size
    filigran = ImageDraw.Draw(resim)
    metin = input("Filigran Yazısı")
    font = ImageFont.truetype('verdana.ttf',30)
    metin_genislik , metin_yukseklik = filigran.textsize(metin,font)
    margin = 20
    x = resim_genislik - metin_genislik - margin
    y = resim_yukseklik - metin_yukseklik - margin
    filigran.text((x,y),metin,font=font)
    resim.show()
    resim.save("filigran.jpg")
if a == 14:
    resim = Image.open("a.jpg",mode = 'r')
    resim.save("png.png")
    resim2 = Image.open("png.png")
    resim2.show()