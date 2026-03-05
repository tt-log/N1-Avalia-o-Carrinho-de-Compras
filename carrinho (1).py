from produto import Produto


class Carrinho:
    def __init__(self):
        self.produtos = []
        self.total = 0

    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"{produto.nome} adicionado ao carrinho.")

    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                print(f"{nome} removido do carrinho.")
                return
        print("Produto não encontrado.")

    
    def calcular_total(self):
        self.total = sum(produto.preco for produto in self.produtos)
        return self.total

    
    def aplicar_desconto(self, percentual):
        total = self.calcular_total()
        desconto = total * (percentual / 100)
        return total - desconto

    
    def gerar_nota_fiscal(self, desconto=0):
        print("\n************ NOTA FISCAL ************")
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco:.2f}")

        total = self.calcular_total()
        print(f"\nTotal: R${total:.2f}")

        if desconto > 0:
            total_com_desconto = self.aplicar_desconto(desconto)
            print(f"Desconto: {desconto}%")
            print(f"Total com desconto: R${total_com_desconto:.2f}")

        print("*************************************\n")


def main():
    p1 = Produto("Caderno", 20.0)
    p2 = Produto("Lapis", 1.50)
    p3 = Produto("Caneta", 1.50)
    p4 = Produto("Borracha", 2.0)

    c1 = Carrinho()

    
    c1.adicionar_produto(p1)
    c1.adicionar_produto(p2)
    c1.adicionar_produto(p3)
    c1.adicionar_produto(p4)

    print("\n************ Seus produtos são ************")
    for item in c1.produtos:
        print(item.nome)

    
    c1.remover_produto("Lapis")

    
    c1.gerar_nota_fiscal(desconto=10)


main()