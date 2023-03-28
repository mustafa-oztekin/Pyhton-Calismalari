from PIL import Image

image = Image.open('rvmtr.png')

new_image = image.resize((400, 100))
new_image.save('rvmtryeni.png')
