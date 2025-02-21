import subprocess  # Importando o módulo subprocess
import time

# Função para iniciar o servidor PHP local
def iniciar_servidor_php():
    print("Iniciando o servidor PHP local para o painel...")
    painel_pasta = 'C:/Users/Micro/Documents/codigos/ONLY/PHP/002/ESTRUTURA DO PROJETO'  # Altere para o caminho correto
    # Inicia o servidor PHP local na porta 8000 com o diretório de painel especificado
    subprocess.Popen(['php', '-S', 'localhost:8000', '-t', painel_pasta])
    
    time.sleep(2)  # Espera 2 segundos para garantir que o servidor está funcionando corretamente
    print("Servidor PHP iniciado. O painel está acessível em http://localhost:8000")

# Função para exibir o menu principal
def menu_principal():
    while True:
        print("\n--- Painel de Administração ---")
        print("1. Iniciar o painel do site")
        print("2. Ver status do servidor")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_servidor_php()
        elif escolha == "2":
            verificar_status_servidor()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para verificar o status do servidor (simulação de status)
def verificar_status_servidor():
    print("\n--- Status do Servidor ---")
    print("Servidor PHP está rodando em http://localhost:8000")
    print("Status: Ativo e em operação.")
    print("Pressione 'Enter' para voltar ao menu principal.")
    input()  # Espera o usuário pressionar Enter para voltar

# Função principal que inicia o painel
def iniciar_painel():
    print("Iniciando o painel do site...")
    menu_principal()

# Executando a função principal
if __name__ == "__main__":
    iniciar_painel()
