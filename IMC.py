'''Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status de acordo
com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO OK
- Entre 18.5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA'''
##########################################################################################################
import sqlite3
conn = sqlite3.connect("imc.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS imc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    peso REAL,
    altura REAL,
    imc REAL
)
''')
while True:
    nome = str(input('Digite seu nome (ou S para sair): ')).upper()
    if nome == 'S':  # Condição de parada
        print("Fim do programa. Consulte um profissional de saúde para avaliações mais precisas.")
        cursor.execute(f"SELECT nome, peso, altura, {imc:.2f} FROM imc")
        print(cursor.fetchall())

        break

    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / (altura ** 2)

#inserindo dados no banco
    #cursor.execute("ALTER TABLE imc ADD COLUMN nome TEXT")

    cursor.execute("INSERT INTO imc(nome, peso, altura, imc)"
                   "VALUES(?, ?, ?,?)", (nome, peso, altura, imc))
    conn.commit()



    print(f'Seu IMC é {imc:.2f}')

    #conn.close() usado para fechar a conexão do banco de dados quando o programa termina

    if imc <= 18.5:
        print('Peso ABAIXO DO NORMAL. Procure um médico.')
    elif 18.5 < imc < 25:
        print('PESO IDEAL. Continue cuidando da sua saúde!')
    elif 25 <= imc < 30:
        print('SOBREPESO. Atenção para hábitos alimentares e atividade física.')
    elif 30 <= imc < 40:
        print('OBESIDADE. É hora de buscar ajuda e mudar hábitos.')
    else:
        print('OBESIDADE GRAVE. Cuide-se!')


