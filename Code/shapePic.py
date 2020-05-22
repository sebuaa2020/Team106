from PIL import Image
im_temp = Image.open('info1.gif')
im_temp = im_temp.resize((20, 20), Image.ANTIALIAS)
im_temp.save("info.gif", "gif") 
