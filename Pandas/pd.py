import pandas as pd

class Table():
    def __init__(self) -> None:
        self.column = ["Nome", "Qnt","Valor","Total"]
        self.costs = dict()
        self.cost_name = list()
        self.cost_qnt = list()
        self.cost_value = list()
        self.cost_total = list()
    
    def alert(self):
        print("[S]Sim / [N]Não")
        print("- Caso o valor seja passado em branco, é considerado como 'S' ")
        next_step = (input("").upper().strip() or 'S')
        return next_step

    def set_cost_name(self):
        label = input("Nome do gasto :").upper().strip()
        while label in self.cost_name:
            print("Esse gasto ja foi cadastrado")
            label = input("Nome do gasto :").upper().strip()
        print(f"Você digitou **{label}**, era isso mesmo que queria escrever?")
        next_step = self.alert()
        while next_step not in ['S','N']:
            print("Opção inválida")
            next_step = self.alert()
        if next_step == "S":
            self.cost_name.append(label)
            self.costs[label] = list()
        else:
            self.set_cost_name()

    def set_cost_qnt(self):
        print(self.costs)
        for _,__ in self.costs.items():
            if len(__) == 0:
                try:
                    quantity = int(input(f"Quantidade de unidades para {_} :") or 1)
                    print(f"Você digitou **{quantity}**, era isso mesmo que queria escrever?")
                    next_step = self.alert()
                    while next_step not in ['S','N']:
                        print("Opção inválida")
                        next_step = self.alert()
                    self.costs[_].append(quantity)
                    self.cost_qnt.append(quantity)
                except ValueError:
                    print("O valor deve ser numerico")
    
    def set_cost_value(self):
        for _,__ in self.costs.items():
            if len(__) == 1:
                try:
                    value = int(input(f"Valor de cada unidade para {_} :") or 1)
                    print(f"Você digitou **{value}**, era isso mesmo que queria escrever?")
                    next_step = self.alert()
                    while next_step not in ['S','N']:
                        print("Opção inválida")
                        next_step = self.alert()
                    self.costs[_].append(value)
                    self.cost_value.append(value)
                except ValueError:
                    print("O valor deve ser numerico")

    def set_cost_total(self):
        for _,__ in self.costs.items():
            if len(__) == 2:
                qnt = self.costs[_][0]
                value = self.costs[_][1]
                total = value * qnt
                self.costs[_].append(total)
                self.cost_total.append(total)

    def stop(self):
        print(f"Deseja realizar outro cadastro?")
        print("[S]Sim / [N]Não")
        print("- Caso o valor seja passado em branco, é considerado como 'S' ")
        next_step = (input("").upper().strip() or 'S')
        while next_step not in ['S','N']:
            print("Opção inválida")
            print("[S]Sim / [N]Não")
            next_step = (input("").upper().strip() or 'S')
        if next_step == 'N':
            exit()

    def printData(self):
        print(self.costs)
        print(self.cost_name)
        print(self.cost_qnt)
        print(self.cost_value)
        print(self.cost_total)

    def createDF(self):
        c = self.column
        for x in self.column:
            print(x)
        df = pd.DataFrame()
        for key in self.costs:
            data = [key,self.costs[key][0],self.costs[key][1],self.costs[key][2]]
            df.iloc[0,0] = pd.Series(data)
        return df


        {'GASTO 1': [2, 20, 40], 'GASTO 2': [3, 2, 6]}
    def menu(self):
        while True:
            self.set_cost_name()
            self.set_cost_qnt()
            self.set_cost_value()
            self.set_cost_total()
            df = self.createDF()
            print(df)
            self.stop()


self = Table()
self.menu()