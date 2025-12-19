class SmartList(list):
    def __getitem__(self, index):
        if index < 0:
            return list.__getitem__(self, -index - 1)
        return list.__getitem__(self, index)


if __name__ == "__main__":
    sl = SmartList([10, 20, 30])
    print(sl[0])
    print(sl[-1])
    print(sl[-2])