import sqlite3
try:#essa função é para garantir que o comando foi realizado com sucesso para o usuário.
    conn = sqlite3.connect("imc.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM imc WHERE peso = 70")

    conn.commit()
    conn.close()
    print('Os dados foram excluídos com sucesso!!!')
except sqlite3.Error as erro:
    print('Erro ao excluir: ', erro)