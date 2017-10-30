
# coding: utf-8

# In[4]:


def multiplica_matriz(A,B):
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])
    assert colunas_A == linhas_B
    
    C=[]
    for linha in range(linhas_A):
        C.append([])
        for coluna in range(colunas_B):
            C[linha].append(0)
            for k in range(colunas_A):
                C[linha][coluna]+= A[linha][k] * B[k][coluna]
    return C
def main():
    i = int(input(print("")))
    A = [[1,2,3], [4,5,6]] //digite o valor das matrizes, para acrescentar novas linhas crie mais um []
    B = [[1,2],[3,4], [5,6]] //digite o valor das matrizes, para acrescentar novas linhas crie mais um []
    print("A matriz resultante é: " +str(multiplica_matriz(A,B)))
if __name__ == "__main__":
    main()

