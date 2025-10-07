# Importa a biblioteca de sockets
import socket

HOST = '172.25.234.3'
PORT = 65432

# O comando 'with' garante que o socket será fechado corretamente no final.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor.
    s.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")

    try:
        # Pede para o usuário digitar as 3 notas.
        nota1 = input("Digite a primeira nota: ")
        nota2 = input("Digite a segunda nota: ")
        nota3 = input("Digite a terceira nota: ")

        # Garante que os valores são números antes de enviar.
        # Isso também substitui vírgula por ponto (ex: 7,5 -> 7.5)
        notas_numeros = [
            float(nota1.replace(',', '.')),
            float(nota2.replace(',', '.')),
            float(nota3.replace(',', '.'))
        ]

        # Junta as notas em uma única string, separada por vírgulas.
        notas_str = f"{notas_numeros[0]},{notas_numeros[1]},{notas_numeros[2]}"

        # Codifica a string para bytes e a envia para o servidor.
        s.sendall(notas_str.encode('utf-8'))

        # Aguarda a resposta do servidor (até 1024 bytes).
        data = s.recv(1024)

        # Decodifica a resposta e a exibe na tela.
        print(f"Resultado: {data.decode('utf-8')}")

    except ValueError:
        print("Erro: Por favor, digite apenas números para as notas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
