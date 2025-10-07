import socket

HOST = '0.0.0.0'
PORT = 65432
MEDIA_APROVACAO = 7.0

print("--- Servidor de Média de Notas ---")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincula o socket ao endereço e porta definidos
    s.bind((HOST, PORT))
    # Coloca o servidor em modo de escuta, aguardando conexões
    s.listen()
    print(f"Servidor iniciado e escutando em {HOST}:{PORT}")

    # --- INÍCIO DO LOOP PRINCIPAL DO SERVIDOR ---
    while True:
        print("\nAguardando uma nova conexão de cliente...")
        
        # O servidor fica parado aqui até um novo cliente se conectar
        conexao, endereco = s.accept()
        
        # Bloco para gerenciar a conexão com o cliente que acabou de se conectar
        with conexao:
            print(f"Conectado por {endereco}")

            # Loop da conversa com o cliente atual
            while True:
                try:
                    dados = conexao.recv(1024)
                    if not dados:
                        print(f"Cliente {endereco} desconectou normalmente.")
                        break

                    notas_str = dados.decode('utf-8')
                    print(f"Notas recebidas de {endereco}: {notas_str}")
                    
                    notas = [float(n) for n in notas_str.split(',')]
                    media = sum(notas) / len(notas)
                    print(f"Média calculada: {media:.2f}")

                    if media >= MEDIA_APROVACAO:
                        resultado = f"Aprovado! Sua média foi: {media:.2f}"
                    else:
                        resultado = f"Reprovado! Sua média foi: {media:.2f}"
                    
                    conexao.sendall(resultado.encode('utf-8'))
                    print("Resultado enviado.")

                except ConnectionResetError:
                    print(f"Cliente {endereco} desconectou de forma abrupta.")
                    break
                
                except (ValueError, IndexError):
                    resultado = "Erro: formato de notas inválido."
                    print("Enviando mensagem de formato inválido.")
                    conexao.sendall(resultado.encode('utf-8'))
        
        print(f"Conexão com {endereco} foi encerrada.")
        # O loop 'while True' vai recomeçar e o servidor voltará a esperar por um novo cliente.