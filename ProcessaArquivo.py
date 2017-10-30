
# coding: utf-8

# In[16]:


def processa_arquivo_txt(n):
    print("Processando txt")
def processa_arquivo_csv(n):
    print("Processando csv")

def main():
    arquivo = input("Digite o nome do arquivo no fomarto 'nome_do_arquivo.extensao' : ")
    extensao = arquivo[-4:]
    if extensao == (".txt"):
        processa_arquivo_txt(arquivo)
    elif extensao == (".csv"):
        processa_arquivo_csv(arquivo)
    else:
        print("O arquivo não se encontra na extensão .txt ou .csv")
if __name__ == "__main__":
    main()

