class Solution:
    def convert(self, s: str, numRows: int) -> str:#parameters: string and integer. Return type: string
        row, size = numRows, len(s)
        index = 0
        space = row - 2 #maximum spacing between each vertical text alignment
        if row == 1 or row >= size:
            return s
        log = {}
        i=0
        while i < size:
            for k in range (row):#ensures the vertical texts are put in the same index
                if i < size:
                    if index not in log:
                        log[index] = ""
                    log[index] += s[i]
                    i +=1
                    if index < row-1:
                        index+=1
                else:
                    break                 
                # new index for the final result
            for k in range (space):
                if i < size:
                    index -= 1
                    if index not in log:
                        log[index] = ""
                    log[index] += s[i]
                    i +=1
                else: 
                    break
            index -=1
        result = ""
        for i in range(row):
            result += log[i]
        return result


    
        