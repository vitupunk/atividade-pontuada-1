import os
os.system
   
    
nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil (SOLTEIRO/CASADO/VIÚVO/DIVORCIADO): ") 
tempo_casada = int(input("coloque o tempo de casada")) 

if sexo == "F" and estado_civil == "CASADA":
        
            tempo_casada = int(input("Digite o tempo de casada (em anos): "))
        
            print("Entrada invalida para o tempo de casada Por favor, insira um numero inteiro.")
            

print("\n Dados da Pessoa ")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
if tempo_casada : 
        print(f"Tempo de Casada: {tempo_casada} anos")