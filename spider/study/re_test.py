import re


def main():
    match = re.match(r'[1-9]\d{5}', '100081BIT ')

    print(type(match))
    if match:
        match.group(0)
        print(match.group(0))
    pass


if __name__ == '__main__':
    main()
