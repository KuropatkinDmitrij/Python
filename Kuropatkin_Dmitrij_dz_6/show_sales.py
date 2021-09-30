if __name__ == "__main__":

    from sys import argv

    with open("bakery.csv", "r", encoding="utf-8") as f:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit]:
            if len(argv) == 2:
                print(*(v for i, v in enumerate(f) if i >= int(argv[1]) - 1), sep="")
            else:
                start, finish = map(int, argv[1:4])
                print(*(v for i, v in enumerate(f) if start - 1 <= i < finish), sep="")

        else:
            print(f.read())
