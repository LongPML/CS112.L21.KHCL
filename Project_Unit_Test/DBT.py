def DBT_Solve1(n):
        if 1 == n:
                return 1
        elif 10 > n:
                return 2
        else:
                n_len = len(str(n))
                start = 10
                end = 90
                Cost = 1

                for i in range(2, n_len):
                        Cost += i*((end - start)//10 +1)
                        start *= 10
                        end = end * 10 + 90
                Cost += ((n//10 - 10**(n_len - 2)) + 1)*n_len
                if 0 == n % 10:
                        return Cost
                else: return Cost + n_len

def DBT_Solve2(n):
        if 1 == n:
                return 1
        elif 10 > n:
                return 2
        else:
                n_len = len(str(n))
                Cost = ((9*(n_len-2) +8)*(10**(n_len-2)) - 8)//9 + ((n//10 - 10**(n_len-2)) + 1)*n_len + 1
                if 0 == n % 10:
                        return Cost
                else: return Cost + n_len