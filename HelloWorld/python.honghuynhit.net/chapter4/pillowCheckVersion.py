from PIL import Image
print('PIL',Image.PILLOW_VERSION)
im = Image.open('E:\Work\Project\image\huynhdh.PNG')
im.save('E:\Work\Project\image\photo_new.png','PNG')

# Create thumbnail image
im.thumbnail((100,100))
im.save('E:\Work\Project\image\huynhthumbnail.png','PNG')
