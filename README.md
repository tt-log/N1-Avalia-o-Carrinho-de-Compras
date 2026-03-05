# 🧾 Relatório Técnico – Teoria Aplicada ao Código

Este projeto foi desenvolvido em **Python** utilizando conceitos de **Programação Orientada a Objetos (POO)** e **manipulação de listas**.

---

# 📦 Estrutura do Projeto

```
produto.py
carrinho.py
README.md
```

- **produto.py** → Define a classe Produto  
- **carrinho.py** → Implementa a lógica do carrinho de compras

---

# 1️⃣ Fundamentos de Programação Orientada a Objetos

O sistema utiliza **Programação Orientada a Objetos (POO)**, que organiza o código usando classes e objetos.

## Classes

Foram criadas duas classes principais:

- `Produto`
- `Carrinho`

Exemplo:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
```

## Atributos

Os atributos armazenam informações do objeto:

- nome
- preco
- lista de produtos

## Métodos

Principais métodos do sistema:

- adicionar_produto()
- remover_produto()
- calcular_total()
- aplicar_desconto()
- gerar_nota_fiscal()

---

# 2️⃣ Pilares da POO

## Abstração

Esconde a complexidade do código, deixando apenas as funções principais visíveis.

## Encapsulamento

Os dados e funções ficam organizados dentro das classes.

---

# 3️⃣ Manipulação de Listas em Python

O carrinho usa listas para armazenar produtos.

Criação da lista:

```python
self.produtos = []
```

Adicionar produto:

```python
self.produtos.append(produto)
```

Remover produto:

```python
self.produtos.remove(produto)
```

Calcular total:

```python
sum(produto.preco for produto in self.produtos)
```

---

# ✅ Conclusão

O projeto demonstra a aplicação prática de:

- Programação Orientada a Objetos
- Classes e objetos
- Manipulação de listas
- Organização modular do código

Os arquivos separados (`produto.py` e `carrinho.py`) seguem boas práticas de programação e facilitam a manutenção do sistema.
