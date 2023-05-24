tamanho = int(input("Digite o tamanho do lado do triângulo: "))
for i in range(tamanho):
  espacos = " " * (tamanho - i - 1)
  asteriscos = "*" * (2 * i + 1)
  print(espacos + asteriscos)
