
# coding: utf-8

# In[32]:


def fibonacci_recursivo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


# In[33]:


def fibonacci_iterativo(n):
    a,b = 0, 1
    for i in range (n):
        a,b = b,a+b
    return a


# In[60]:


def main():
    n=int(input("Digite um número "))
    for i in range(1,n+1):
        print ("O fibonacci recursivo é = "+str(fibonacci_recursivo(i)))
    for i in range(1,n+1):
        print ("O fibonacci iterativo é = "+ str(fibonacci_iterativo(i)))
if __name__=="__main__":
    main()

