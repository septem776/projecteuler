def sumofmultiples(n, upper):
    ret = 0
    i = 1
    while True:
        if i * n >= upper:
            break
        
        ret += i * n
        i += 1

    return ret

if __name__ == '__main__':
    print(sumofmultiples(3, 1000) + sumofmultiples(5, 1000) - sumofmultiples(15, 1000)) 
