try:

    for i in range(1,1000,1):
        print(i,i**(2*i)*10)
except Exception:
    print(Exception,i,sep="\n\n\n")