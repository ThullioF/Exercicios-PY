def valorPagamento(valorPrestacao, diasAtraso):
    if diasAtraso == 0:
        return valorPrestacao
    else:
        multa = valorPrestacao * 0.03
        juros = valorPrestacao * (0.001 * diasAtraso)
        return valorPrestacao + multa + juros

totalPrestacoes = 0
totalValor = 0

while True:
    valorPrestacao = float(input("Informe o valor da prestação (ou digite 0 para encerrar): "))
    
    if valorPrestacao == 0:
        break

    diasAtraso = int(input("Informe o número de dias em atraso: "))
    
    valorPagar = valorPagamento(valorPrestacao, diasAtraso)
    
    print(f"Valor a ser pago: R$ {valorPagar:.2f}")
    
    totalPrestacoes += 1
    totalValor += valorPagar

print("\nRelatório do dia:")
print(f"Quantidade de prestações pagas: {totalPrestacoes}")
print(f"Valor total pago: R$ {totalValor:.2f}")