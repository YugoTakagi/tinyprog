import time


def main():
    len_ = 200
    for i in Colorber(range(len_), eitem='*'):

        # [1] 処理 ---

        time.sleep(0.05)

        # ...

    print("\n>>> OK!")




class Colorbar:

    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    end = "\033[0m"
    bold = "\033[1m"
    under_line = "\033[4m"
    clear = "\033[39m"

    background_black = "\033[40m"
    background_white = "\033[47m"


    def __init__(self, list_:list,
            item:str='-', eitem='-',num_items:int=35):
        self.num_items = num_items
        self.list = list_
        self.len = len(self.list)
        self.item = item
        self.eitem = eitem


    def __len__(self):
        return self.len

    
    def __getitem__(self, i):
        self.plot_prog(i)
        return self.list[i]


    def plot_prog(self, i):
        if i == 0:
            self.time_start = time.time()
        self.time_end = time.time()
        # [2] プログレスバー ---
        i_ = i + 1
        pnum = int(i_ * (self.num_items / self.len))
        nnum = self.num_items - pnum
        print("\r    " + \
                self.bold + \
                # green + item * pnum + \
                # red + item * nnum + \
                # end + \
                self.red + self.eitem * pnum + \
                self.end + self.item * nnum + \
                self.green + f" {i_}/{self.len} items" + \
                self.red + f" {int(i_ / self.len * 100)} %" + \
                self.blue + " {:.2g} it/s".format(self.time_end - self.time_start) + \
                self.clear, end="")
        # ...
        self.time_start = time.time()


if __name__ == '__main__':
    main()
