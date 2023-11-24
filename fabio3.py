def fibos(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibos(n - 1) + fibos(n - 2)

print(fibos(5))

#Incompleto