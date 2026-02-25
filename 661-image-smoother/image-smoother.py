class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        sum = 0
        result = []
        if m == 1:
            if n == 1:
                return img
            else:
                i = 0
                result.append([])
                for j in range(n):
                    if j == 0:
                        sum = img[i][j] + img[i][j+1]
                        avg = sum // 2
                    elif j == n-1:
                        sum = img[i][j] + img[i][j-1]
                        avg = sum // 2
                    else:
                        sum = img[i][j-1] + img[i][j] + img[i][j+1]
                        avg = sum // 3
                    result[i].append(avg)
            return result
            
        if n == 1:
            j = 0
            for i in range(m):
                result.append([])
                if i == 0:
                    sum = img[i][j] + img[i+1][j]
                    avg = sum // 2
                elif i == m-1:
                    sum = img[i][j] + img[i-1][j]
                    avg = sum // 2
                else:
                    sum = img[i-1][j] + img[i][j] + img[i+1][j]
                    avg = sum // 3
                result[i].append(avg)
            return result

        for i in range(m):
            result.append([])
            for j in range(n):
                sum = img[i][j]
                if i == 0:
                    if j == 0:
                        sum += img[i][j+1] + img[i+1][j] + img[i+1][j+1]
                        avg = sum // 4
                    elif j == n-1:
                        sum += img[i][j-1] + img[i+1][j] + img[i+1][j-1]
                        avg = sum // 4
                    else:
                        sum += img[i][j-1] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
                        avg = sum // 6

                elif i == m-1:
                    if j == 0:
                        sum += img[i][j+1] + img[i-1][j] + img[i-1][j+1]
                        avg = sum // 4
                    elif j == n-1:
                        sum += img[i][j-1] + img[i-1][j] + img[i-1][j-1]
                        avg = sum // 4
                    else:
                        sum += img[i][j-1] + img[i][j+1] + img[i-1][j-1] + img[i-1][j] + img[i-1][j+1]
                        avg = sum // 6
        
                elif i != 0 and j == 0:
                    sum += img[i-1][j] + img[i+1][j] + img[i-1][j+1] + img[i][j+1] + img[i+1][j+1]
                    avg = sum // 6

                elif i!= m-1 and j == n-1:
                    sum += img[i-1][j] + img[i+1][j] + img[i-1][j-1] + img[i][j-1] + img[i+1][j-1]
                    avg = sum // 6
                
                else:
                    sum += img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j+1] +  img[i+1][j-1] + img[i+1][j] + img[i+1][j+1]
                    avg = sum // 9
                result[i].append(avg)
                
        return result

                

