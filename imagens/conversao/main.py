from PIL import Image

imageFile = Image.open(r'.\img.png')
imageFile = imageFile.convert('L')
imageFile.save(r'\img_pb.png')
