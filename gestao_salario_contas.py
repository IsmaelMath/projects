"""

Como ficaria essa (João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas
(C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. Como as contas estão atrasadas, João terá de pagar
multa de 2% sobre cada conta. Faça um programa em Python que calcule e mostre
quanto restará do salário do João.

"""

salario = float(input("Informe o seu salário do mês: "))
contas = []

while True:
    contas_apagar = input("se existe contas a ser paga, responda sim ou não: ")
    if contas_apagar.upper() == "SIM":

        while True:
            valor_conta = float(input("Informe o valor da conta: "))
            tempo_atraso = int(input("Informe o tempo que a conta está em atraso: "))
            juros = float(input("Informe o juro que esta sendo cobrado pela conta "
                                "atrasada de valor {: .2f}: ".format(valor_conta)))
            print("A conta no valor R$ {: .2f} que está com atraso de {} meses com "
                  "juros de {} % ao mês.".format(valor_conta, tempo_atraso, juros))
            dados_corretos = input("Informe 'sim' se os dados da conta estão corretos ou 'não' retornar: ")
            if dados_corretos.upper() == "SIM":
                while True:
                    tipo_de_juros = input("Informe qual o tipo de juro que está sendo cobrado se é juros\n"
                                          " simples(js) ou juros conposto(jc): ")
                    if tipo_de_juros.upper() == "JC":
                        conta = valor_conta * (1 + (juros / 100)) ** tempo_atraso
                        contas.append(conta)
                        break
                    elif tipo_de_juros.upper() == "JS":
                        conta = valor_conta + valor_conta * (juros / 100)
                        contas.append(conta)
                        break
                    else:
                        print("Essa operação não existe, tente novamente !!!!")
            else:
                print("Informe os dados corretamente! ")
            break
    elif contas_apagar.upper() == "NÃO":
        print("Fim !!!")
        break
    else:
        print("Essa resposta não existe, tente novamente !!!")
total_dividas = sum(contas)
salario_liq = salario - sum(contas)

print("O seu salário bruto do mês é de R$ {:.2f} onde você tem {} contas "
      "no valor total com juros de R$ {: .2f} e seu salário líquido do "
      "mês é R$ {:.2f}".format(salario, len(contas), total_dividas, salario_liq))

" Essa foi abordagem um pouco complexo mais o codigo vou disponibilizar no github"