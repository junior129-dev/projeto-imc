# 🧮 Projeto IMC (Índice de Massa Corporal)

Este é um projeto em Python que calcula o Índice de Massa Corporal (IMC) com base nos dados informados pelo usuário. 
A aplicação armazena os dados localmente usando SQLite, permitindo futuras análises sobre a evolução do peso de cada pessoa cadastrada.

## 📌 Funcionalidades atuais

- Recebe o nome do usuário
- Solicita peso e altura
- Calcula o IMC
- Exibe a classificação de acordo com o resultado
- Armazena os dados do usuário em um banco SQLite

## 🔄 Funcionalidades planejadas

- Comparar o peso atual com registros anteriores do mesmo usuário
- Informar se a pessoa manteve, ganhou ou perdeu peso
- Melhorar estrutura do banco para histórico individual
- Organizar dados para futura exportação (CSV ou visualização simples)

## 💻 Tecnologias utilizadas

- **Python 3**
- **SQLite3** (banco de dados embutido no Python)
- Programação Orientada a Objetos (em desenvolvimento)

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/junior129-dev/projeto-imc.git
   cd projeto-imc
   python imc.py
Certifique-se de ter o Python 3 instalado na sua máquina.
Caso use Windows, pode dar dois cliques no arquivo para executá-lo via terminal.

## 📈Exemplo de uso
Digite seu nome: Junior
Digite sua altura (em metros): 1.75
Digite seu peso (em kg): 70

Olá, Junior!
Seu IMC é: 22.86
Classificação: Peso normal

🧠 Autor
Desenvolvido por Junior – Estudante de Engenharia de Software, focado em desenvolvimento back-end e em busca da primeira oportunidade na área de desenvolvimento.
