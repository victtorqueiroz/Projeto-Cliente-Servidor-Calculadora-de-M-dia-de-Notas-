# Projeto Cliente-Servidor: Calculadora de Média de Notas

Este projeto foi desenvolvido como parte do trabalho prático sobre Sockets (Capítulo 2) do livro "Redes de Computadores e a Internet" de Kurose e Ross.

A aplicação consiste em um programa servidor e um cliente que se comunicam via sockets TCP. O cliente solicita três notas ao usuário, as envia para o servidor, que por sua vez calcula a média, determina se o status é "Aprovado" ou "Reprovado" e retorna o resultado completo para o cliente.

## Tecnologias Utilizadas
* Python 3
* Biblioteca `socket` do Python

## Estrutura do Projeto
O projeto é composto por dois scripts principais:

* `servidor.py`: Este script inicia um servidor TCP que fica escutando em uma porta específica. Ele é projetado para aceitar uma conexão de cliente, receber os dados (as notas), processá-los, enviar uma resposta e, em seguida, aguardar por uma nova conexão.
* `cliente.py`: Este script solicita a entrada de três notas do usuário, conecta-se ao servidor, envia os dados formatados e, por fim, exibe a resposta recebida do servidor.

## Como Executar o Projeto

Você pode testar a aplicação de duas maneiras: na sua própria máquina (localhost) ou em duas máquinas diferentes na mesma rede.

### Testando na Mesma Máquina (localhost)

1.  **Abra dois terminais** (Prompt de Comando, PowerShell, etc.).
2.  Em ambos os terminais, navegue até a pasta do projeto usando o comando `cd`.
3.  No **primeiro terminal**, inicie o servidor:
    ```bash
    python servidor.py
    ```
    Ele exibirá a mensagem `Servidor iniciado e escutando...`.
4.  No **segundo terminal**, inicie o cliente:
    ```bash
    python cliente.py
    ```
5.  Siga as instruções no terminal do cliente para inserir as três notas. O resultado será exibido em seguida.

### Testando em Duas Máquinas (Rede Local)

1.  Certifique-se de que ambas as máquinas (Máquina A - Servidor, Máquina B - Cliente) estão na mesma rede (ex: mesmo Wi-Fi).
2.  Na **Máquina A**, descubra o endereço IP local (no Windows, use o comando `ipconfig` no terminal).
3.  Na **Máquina B**, abra o arquivo `cliente.py` e altere a variável `HOST` para o endereço IP da Máquina A.
    ```python
    # Exemplo:
    HOST = '192.168.0.10' # Substitua pelo IP real do servidor
    ```
4.  Na **Máquina A**, inicie o servidor:
    ```bash
    python servidor.py
    ```
5.  Na **Máquina B**, inicie o cliente:
    ```bash
    python cliente.py
    ```
6.  Insira as notas no cliente para ver o resultado.

## Captura com Wireshark

Conforme solicitado no trabalho, a comunicação foi capturada com o Wireshark. Para analisar a captura:

1.  Abra o arquivo `.pcapng` no Wireshark.
2.  Use o filtro `tcp.port == 65432` para isolar o tráfego da aplicação.
3.  É possível observar claramente as três fases da comunicação TCP:
    * **Estabelecimento da Conexão:** O Three-Way Handshake (pacotes `SYN`, `SYN-ACK`, `ACK`).
    * **Transferência de Dados:** Pacotes com a flag `PSH` (Push), onde é possível ver os dados das notas sendo enviados do cliente para o servidor e a string de resultado ("Aprovado/Reprovado") sendo enviada de volta.
    * **Encerramento da Conexão:** A troca de pacotes com a flag `FIN` (Finish) para fechar a conexão de forma organizada.

## Autor

Victor Emanuel Silva de Queiroz