import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    format_poem = re.split(r'[，。,.]', poem)
    while '' in format_poem:
        format_poem.remove('')
    print(format_poem)

    pass


if __name__ == '__main__':
    main()
