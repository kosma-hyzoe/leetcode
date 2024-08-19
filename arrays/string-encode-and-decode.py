from array import array


class Solution:

    def encode(self, strs):
        code = []
        for w in strs:
            code.extend([str(len(w)), '#', w])
        return "".join(code)

    def decode(self, s):
        words = []
        wc = 0
        no = ""
        read_num = True

        for let in s:
            if no == 0:
                read_num = True
                no = ""
                wc += 1

            if read_num:
                if let == "#":
                    no = int(no)
                    read_num = False
                    words.append("")
                else:
                    no += let
            else:
                words[wc] += let
                no -= 1
        return words
