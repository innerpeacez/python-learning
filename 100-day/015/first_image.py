from PIL import Image


def main():
    image = Image.open('./avatar-icon.jpg')
    size = 128, 128
    image.thumbnail(size)
    image.show()
    # image.transpose(Image.FLIP_LEFT_RIGHT).show()


if __name__ == '__main__':
    main()
