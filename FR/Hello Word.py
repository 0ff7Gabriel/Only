print("Hello World")

from operator import index

def iniciar(index):
    print("Executando outras funções...")

if __name__ == "__main__":
    iniciar(index)
    

def saudacao(start):
    print("Olá! Esse código veio de outro arquivo.")


if __name__ == "__main__":
    saudacao(index)


import os

# Obtém o diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo que deseja abrir
file_name = "start.py"

# Caminho completo do arquivo
file_path = os.path.join(current_dir, file_name)

# Verifica se o arquivo existe e abre
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("Conteúdo do arquivo start.py:")

os.system(f'python "{file_path}"')

asdasd = True  # dash 
if asdasd:
    print("Seja Bem-vindo")
else:
    print("Seja Bem-vindo")

asdasd = True  # dash 
if asdasd:
    print("DKISS")
else:
    print("DKISS")

{
    "name": "dkiss/php",
    "autoload": {
        "psr-4": {
            "Dkiss\\Php\\": "src/"
        }
    },
    "authors": [
        {
            "name": "dkiss",
            "email": "dkissartist@gmail.com"
        }
    ],
    "require": {}
}

import os

# Nome do arquivo HTML
arquivo_html = "HelloWorld.html"

# Verificando se o arquivo HTML já existe
if os.path.exists(arquivo_html):
    # Se o arquivo existir, removemos
    os.remove(arquivo_html)
    print(f"O arquivo {arquivo_html} foi excluído.")

# Criando o arquivo HTML novamente
with open(arquivo_html, "w") as file:
    # Escrevendo o código HTML no arquivo
    file.write("""<!DOCTYPE html> <!-- Linha 1: Declaração do tipo do documento -->
<html lang="pt-br"> <!-- Linha 2: Início do código HTML -->

<head> <!-- Linha 3: Início da seção de cabeçalho -->
    <meta charset="UTF-8"> <!-- Linha 4: Definição de codificação -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Linha 5: Definição da escala de visualização -->
    <title>Meu Site</title> <!-- Linha 6: Título do site -->
    <link rel="stylesheet" href="styles.css"> <!-- Linha 7: Inclusão de arquivo CSS -->
</head> <!-- Linha 8: Fim da seção de cabeçalho -->

<body> <!-- Linha 9: Início do corpo do site -->
    <header> <!-- Linha 10: Cabeçalho da página -->
        <h1>Bem-vindo ao Meu Site!</h1> <!-- Linha 11: Título principal -->
        <nav> <!-- Linha 12: Navegação -->
            <ul> <!-- Linha 13: Lista de links -->
                <li><a href="#home">Início</a></li> <!-- Linha 14: Link para Início -->
                <li><a href="#sobre">Sobre</a></li> <!-- Linha 15: Link para Sobre -->
                <li><a href="#contato">Contato</a></li> <!-- Linha 16: Link para Contato -->
            </ul> <!-- Linha 17: Fim da lista -->
        </nav> <!-- Linha 18: Fim da navegação -->
    </header> <!-- Linha 19: Fim do cabeçalho -->

    <section id="home"> <!-- Linha 20: Seção de início -->
        <h2>Seção Início</h2> <!-- Linha 21: Subtítulo da seção -->
        <p>Conteúdo principal do site.</p> <!-- Linha 22: Parágrafo -->
    </section> <!-- Linha 23: Fim da seção Início -->

    <section id="sobre"> <!-- Linha 24: Seção sobre -->
        <h2>Sobre nós</h2> <!-- Linha 25: Subtítulo da seção -->
        <p>Informações sobre a empresa ou projeto.</p> <!-- Linha 26: Parágrafo -->
    </section> <!-- Linha 27: Fim da seção sobre -->

    <section id="contato"> <!-- Linha 28: Seção de contato -->
        <h2>Contato</h2> <!-- Linha 29: Subtítulo da seção -->
        <form> <!-- Linha 30: Formulário de contato -->
            <label for="nome">Nome:</label> <!-- Linha 31: Campo nome -->
            <input type="text" id="nome" name="nome" required> <!-- Linha 32: Entrada de texto -->
            <label for="email">E-mail:</label> <!-- Linha 33: Campo e-mail -->
            <input type="email" id="email" name="email" required> <!-- Linha 34: Entrada de e-mail -->
            <textarea id="mensagem" name="mensagem" placeholder="Sua mensagem..." required></textarea> <!-- Linha 35: Campo de mensagem -->
            <button type="submit">Enviar</button> <!-- Linha 36: Botão de envio -->
        </form> <!-- Linha 37: Fim do formulário -->
    </section> <!-- Linha 38: Fim da seção de contato -->

    <footer> <!-- Linha 39: Início do rodapé -->
        <p>&copy; 2025 Meu Site. Todos os direitos reservados.</p> <!-- Linha 40: Copyright -->
    </footer> <!-- Linha 41: Fim do rodapé -->
</body> <!-- Linha 42: Fim do corpo -->
</html> <!-- Linha 43: Fim do código HTML -->""")
    
# Confirmação
print(f"O arquivo {arquivo_html} foi criado novamente!")
# Abrindo o arquivo HTML para escrever
with open("HelloWorld.html", "w") as file:
    # Iniciando o código HTML
    file.write("<!DOCTYPE html>\n<html lang='pt-br'>\n<head>\n<title>Meu Site</title>\n</head>\n<body>\n")
    
# Exibindo mensagem no console
print("O HTML foi iniciado com sucesso!")

# Abrindo (ou criando) o arquivo HTML para escrever o conteúdo
with open("Only.html", "w") as file:
    file.write("<!DOCTYPE html>\n<html lang='pt-br'>\n<head>\n<title>Only</title>\n</head>\n<body>\n<h1>Only</h1>\n</body>\n</html>")
    
# Exibindo mensagem no console
print("O site 'Only' foi iniciado com o título 'Only'!")

asdasd = True  # dash 
if asdasd:
    print("Seja Bem-vindo ao Only")
else:
    print("Seja Bem-vindo ao Only")

# Abrindo (ou criando) o arquivo HTML para escrever o conteúdo
with open("MelhoresFuncoes.html", "w") as file:
    file.write("""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Melhores Funções do Mercado</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #f4f4f4; }
        header { background: #333; color: #fff; padding: 10px 0; text-align: center; }
        section { padding: 20px; margin: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        h1, h2 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 10px 0; }
        footer { text-align: center; padding: 10px 0; background: #333; color: #fff; position: fixed; width: 100%; bottom: 0; }
    </style>
</head>
<body>
    <header>
        <h1>Bem-vindo ao Site com as Melhores Funções do Mercado!</h1>
    </header>

    <section>
        <h2>Recursos Incríveis:</h2>
        <p>Este site foi desenvolvido para oferecer a melhor experiência online, com recursos inovadores e funcionalidades de ponta. Confira abaixo algumas das melhores funções do mercado:</p>
        <ul>
            <li><strong>Design Responsivo:</strong> O site se adapta perfeitamente a qualquer dispositivo, proporcionando uma experiência de navegação fluida, seja em desktop, tablet ou celular.</li>
            <li><strong>Integração de Inteligência Artificial:</strong> Funcionalidades inteligentes que melhoram a interação do usuário, recomendando conteúdos e ajustando a interface com base no comportamento do visitante.</li>
            <li><strong>Carregamento Ultra Rápido:</strong> A otimização de performance garante que as páginas carreguem em milissegundos, oferecendo uma experiência de navegação sem interrupções.</li>
            <li><strong>Segurança Avançada:</strong> Proteção de dados do usuário através de criptografia e medidas de segurança de última geração, mantendo a privacidade e a confiança dos nossos visitantes.</li>
            <li><strong>Facilidade de Navegação:</strong> Interface intuitiva e menus fáceis de usar, garantindo que o usuário encontre o que precisa rapidamente, sem complicações.</li>
            <li><strong>Suporte 24/7:</strong> Equipe de suporte sempre disponível para ajudar com dúvidas ou problemas, garantindo um atendimento rápido e eficiente.</li>
        </ul>
    </section>

    <footer>
        <p>&copy; 2025 Site com as Melhores Funções do Mercado. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
    """)

# Exibindo mensagem no console
print("O site com as melhores funções do mercado foi criado com sucesso!")

import os

# Definindo o caminho para as pastas php e sql
php_folder = "php"
sql_folder = "sql"

# Criando as pastas se elas não existirem
os.makedirs(php_folder, exist_ok=True)
os.makedirs(sql_folder, exist_ok=True)

# Definindo o conteúdo do arquivo PHP (codigo_php_para_criar_usuarios.php)
php_code = """<?php
// Conexão com o banco de dados
require_once '../includes/config.php';  // Ajuste o caminho conforme sua estrutura

// Dados do novo usuário
$nome = "Dkiss";
$email = "dkissartist@gmail.com";
$senha = "14082003";  // Senha fornecida
$is_admin = 1;  // Indicando que o usuário será um administrador

// Hash da senha
$hashedSenha = password_hash($senha, PASSWORD_DEFAULT);

// Preparando o SQL para inserir o usuário no banco
$sql = "INSERT INTO usuarios (nome, email, senha, is_admin) VALUES (:nome, :email, :senha, :is_admin)";
$stmt = $pdo->prepare($sql);

// Executando a consulta
$stmt->execute([
    ':nome' => $nome,
    ':email' => $email,
    ':senha' => $hashedSenha,
    ':is_admin' => $is_admin
]);

// Verificando se o cadastro foi bem-sucedido
if ($stmt->rowCount() > 0) {
    echo json_encode([
        "message" => "Usuário Dkiss registrado com sucesso como administrador!"
    ]);
} else {
    echo json_encode([
        "message" => "Erro ao registrar o usuário."
    ]);
}
?>
"""

# Definindo o conteúdo do arquivo SQL (Banco_de_Dados.sql)
sql_code = """CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    is_admin TINYINT(1) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Caminho para salvar os arquivos
php_file_path = os.path.join(php_folder, "codigo_php_para_criar_usuarios.php")
sql_file_path = os.path.join(sql_folder, "Banco_de_Dados.sql")

# Criando e escrevendo o código no arquivo PHP
with open(php_file_path, "w") as php_file:
    php_file.write(php_code)

# Criando e escrevendo o código no arquivo SQL
with open(sql_file_path, "w") as sql_file:
    sql_file.write(sql_code)

# Confirmando a criação dos arquivos
print("Arquivos PHP e SQL foram criados com sucesso nas pastas 'php' e 'sql'.")

import getpass

# Definindo as credenciais do administrador (simulando um banco de dados)
admin_id = "Dkiss"
admin_senha_hash = "14082003"  # Em um cenário real, seria o hash da senha

# Função para validar login
def login():
    print("Digite seu ID e senha para acessar o painel de administrador.")

    # Pegando as entradas de ID e senha
    user_id = input("ID (nome ou email): ")
    user_senha = input("Senha: ")  # Usando input sem ocultar a senha

    # Validação do login
    if user_id == admin_id and user_senha == admin_senha_hash:
        print("\nAcesso concedido! Bem-vindo ao painel de administração.")
    else:
        print("\nID ou senha inválidos. Tente novamente.")

# Chamando a função de login
login()

import subprocess
import time

# Função para autenticação do administrador
def autenticar_admin():
    id_admin = "Dkiss"  # ID de administrador
    senha_admin = "14082003"  # Senha do administrador
    
    print("=== Autenticação de Administrador ===")
    id_input = input("Digite seu ID de administrador: ")
    senha_input = input("Digite sua senha: ")
    
    if id_input == id_admin and senha_input == senha_admin:
        print("Autenticação bem-sucedida! Acesso concedido ao painel de administração.")
        return True
    else:
        print("ID ou senha incorretos. Acesso negado.")
        return False

# Função para exibir o menu inicial
def menu_inicial():
    print("\n===== Menu Inicial =====")
    print("1. Acessar painel de administração")
    print("2. Iniciar funcionamento do site")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Função para iniciar o funcionamento do site (simulado)
def iniciar_site():
    print("\nIniciando o funcionamento do site...")
    print("Processando inicialização do site:")
    
    # Simulando os processos que ocorrem para iniciar o site
    print("Iniciando o servidor...")
    time.sleep(1)  # Pausa para simular o tempo de processamento
    print("Servidor iniciado com sucesso!")

    print("Carregando dados do site...")
    time.sleep(1)
    print("Dados carregados com sucesso!")

    print("Conectando ao banco de dados...")
    time.sleep(1)
    print("Conexão com o banco de dados estabelecida!")

    print("Configurando rotas e usuários...")
    time.sleep(1)
    print("Rotas e usuários configurados com sucesso!")

    print("\nO site foi iniciado com sucesso!")
    print("Bem-vindo ao site! O site está em funcionamento.")

    # Agora, vamos iniciar o arquivo PHP
    iniciar_php_arquivo()

# Função para iniciar o arquivo PHP
def iniciar_php_arquivo():
    try:
        # Chama o arquivo PHP para iniciar o site
        print("\nIniciando o arquivo PHP...")
        
        # O comando abaixo depende de onde está o arquivo PHP
        # Substitua 'index.php' pelo nome do arquivo PHP que você deseja iniciar
        comando_php = ["php", "index.php"]  # Use o caminho correto para o seu arquivo PHP, caso necessário
        
        # Executa o comando para rodar o arquivo PHP
        subprocess.run(comando_php, check=True)
        print("Arquivo PHP iniciado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o arquivo PHP: {e}")
    except FileNotFoundError:
        print("Erro: O PHP não está instalado ou o caminho para o PHP está incorreto.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
import os
import subprocess

# Função para iniciar todos os arquivos dentro das pastas especificadas
def iniciar_arquivos_da_pasta(pasta_raiz):
    # Verifica se a pasta raiz existe
    if not os.path.exists(pasta_raiz):
        print(f"A pasta '{pasta_raiz}' não foi encontrada.")
        return
    
    # Percorre todas as subpastas e arquivos dentro da pasta raiz
    for root, dirs, files in os.walk(pasta_raiz):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            
            # Verifica a extensão do arquivo para saber como executá-lo
            if file.endswith('.py'):
                print(f"Iniciando o arquivo Python: {caminho_arquivo}")
                subprocess.run(['python', caminho_arquivo], check=True)
            elif file.endswith('.php'):
                print(f"Iniciando o arquivo PHP: {caminho_arquivo}")
                subprocess.run(['php', caminho_arquivo], check=True)
            else:
                print(f"Arquivo {caminho_arquivo} não pode ser executado automaticamente (somente .py ou .php).")

# Função principal
def main():
    pasta_raiz = '002'  # O nome da pasta raiz (que contém as subpastas)
    iniciar_arquivos_da_pasta(pasta_raiz)

# Chama a função principal
if __name__ == "__main__":
    main()
    
# Função para exibir o menu principal do painel
def exibir_menu():
    print("\n===== Painel de Administração =====")
    print("1. Visualizar usuários")
    print("2. Adicionar usuário")
    print("3. Remover usuário")
    print("4. Editar usuário")
    print("5. Procurar usuário")
    print("6. Visualizar estatísticas")
    print("7. Visualizar informações de usuário")
    print("8. Formas de pagamento usadas")
    print("9. O que foi digitado")
    print("10. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

# Base de dados de usuários
usuarios = {
    '1': {'nome': 'João Silva', 'email': 'joao@email.com', 'cadastro': '2023-01-10', 'pagamento': 'Cartão de Crédito', 'endereco': 'Rua A, 123'},
    '2': {'nome': 'Maria Souza', 'email': 'maria@email.com', 'cadastro': '2023-02-15', 'pagamento': 'PayPal', 'endereco': 'Rua B, 456'},
    '3': {'nome': 'Carlos Oliveira', 'email': 'carlos@email.com', 'cadastro': '2023-03-20', 'pagamento': 'Boleto', 'endereco': 'Rua C, 789'}
}

# Função para exibir a lista de usuários
def listar_usuarios():
    print("\nUsuários cadastrados:")
    for id, dados in usuarios.items():
        print(f"{id}. {dados['nome']} - {dados['email']}")

# Função para adicionar um novo usuário
def adicionar_usuario():
    nome = input("\nDigite o nome do novo usuário: ")
    email = input("Digite o email do usuário: ")
    cadastro = input("Digite a data de cadastro (AAAA-MM-DD): ")
    pagamento = input("Digite a forma de pagamento usada (Cartão, PayPal, Boleto): ")
    endereco = input("Digite o endereço do usuário: ")
    
    id_novo = str(len(usuarios) + 1)  # Gera um novo ID
    usuarios[id_novo] = {
        'nome': nome,
        'email': email,
        'cadastro': cadastro,
        'pagamento': pagamento,
        'endereco': endereco
    }
    print(f"Usuário '{nome}' adicionado com sucesso!")

# Função para remover um usuário
def remover_usuario():
    id_usuario = input("\nDigite o ID do usuário para remover: ")
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        print(f"Usuário com ID {id_usuario} removido com sucesso!")
    else:
        print("ID de usuário não encontrado.")

# Função para editar um usuário
def editar_usuario():
    id_usuario = input("\nDigite o ID do usuário para editar: ")
    if id_usuario in usuarios:
        novo_nome = input(f"Digite o novo nome para o usuário ID {id_usuario}: ")
        usuarios[id_usuario]['nome'] = novo_nome
        print(f"Usuário ID {id_usuario} atualizado para '{novo_nome}'.")
    else:
        print("ID de usuário não encontrado.")

# Função para procurar um usuário
def procurar_usuario():
    nome_usuario = input("\nDigite o nome do usuário para procurar: ")
    encontrado = False
    for id, dados in usuarios.items():
        if nome_usuario.lower() in dados['nome'].lower():
            print(f"Usuário encontrado: ID {id} - {dados['nome']} - {dados['email']}")
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")

# Função para visualizar estatísticas
def visualizar_estatisticas():
    total_usuarios = len(usuarios)
    print(f"\nEstatísticas:")
    print(f"Total de usuários cadastrados: {total_usuarios}")

# Função para visualizar informações detalhadas do usuário
def visualizar_informacoes_usuario():
    id_usuario = input("\nDigite o ID do usuário para visualizar informações: ")
    if id_usuario in usuarios:
        dados = usuarios[id_usuario]
        print(f"\nInformações do usuário ID {id_usuario}:")
        print(f"Nome: {dados['nome']}")
        print(f"Email: {dados['email']}")
        print(f"Data de Cadastro: {dados['cadastro']}")
        print(f"Forma de pagamento: {dados['pagamento']}")
        print(f"Endereço: {dados['endereco']}")
    else:
        print("ID de usuário não encontrado.")

# Função para visualizar as formas de pagamento usadas
def formas_pagamento_usadas():
    pagamentos = set(dados['pagamento'] for dados in usuarios.values())
    print("\nFormas de pagamento usadas pelos usuários:")
    for pagamento in pagamentos:
        print(pagamento)

# Função para visualizar o que foi digitado pelos clientes
def oq_foi_digitado():
    print("\n=== O que foi digitado pelos clientes ===")
    print("Nenhuma entrada registrada ainda.")

# Função principal para controlar o painel de administração
def painel_administracao():
    if autenticar_admin():  # Verifica se a autenticação foi bem-sucedida
        while True:
            opcao = exibir_menu()

            if opcao == '1':
                listar_usuarios()
            elif opcao == '2':
                adicionar_usuario()
            elif opcao == '3':
                remover_usuario()
            elif opcao == '4':
                editar_usuario()
            elif opcao == '5':
                procurar_usuario()
            elif opcao == '6':
                visualizar_estatisticas()
            elif opcao == '7':
                visualizar_informacoes_usuario()
            elif opcao == '8':
                formas_pagamento_usadas()
            elif opcao == '9':
                oq_foi_digitado()
            elif opcao == '10':
                print("Saindo do painel...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Não foi possível acessar o painel. Tente novamente.")

# Função principal que inicia o programa
def main():
    while True:
        opcao = menu_inicial()

        if opcao == '1':
            painel_administracao()  # Só entra no painel se a autenticação for bem-sucedida
        elif opcao == '2':
            iniciar_site()  # Chama a função para iniciar o site
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
if __name__ == "__main__":
    main()

import os
import subprocess

# Função para iniciar todos os arquivos dentro das pastas especificadas
def iniciar_arquivos_da_pasta(pasta_raiz):
    if not os.path.exists(pasta_raiz):
        print(f"A pasta '{pasta_raiz}' não foi encontrada.")
        return
    
    for root, dirs, files in os.walk(pasta_raiz):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            
            if file.endswith('.php'):
                print(f"Iniciando o arquivo PHP: {caminho_arquivo}")
                subprocess.run(['php', caminho_arquivo], check=True)
            elif file.endswith('.sql'):
                print(f"Iniciando o arquivo SQL: {caminho_arquivo}")
                subprocess.run(['mysql', '-u', 'usuario', '-p', 'senha', '<', caminho_arquivo], check=True)
            elif file.endswith('.html'):
                print(f"Abrindo o arquivo HTML: {caminho_arquivo}")
                subprocess.run(['start', caminho_arquivo], shell=True)  # No Windows
            elif file.endswith('.js'):
                print(f"Iniciando o arquivo JavaScript: {caminho_arquivo}")
                subprocess.run(['node', caminho_arquivo], check=True)
            else:
                print(f"Arquivo {caminho_arquivo} não pode ser executado automaticamente (somente .php, .sql, .html, .js).")

# Função para iniciar o carregamento do painel do site
def iniciar_carregamento_painel():
    print("\nIniciando o carregamento do painel do site...")
    
    # Coloque aqui a sequência de inicialização do painel do site
    # Por exemplo, iniciar um servidor web, carregar scripts, etc.
    
    # Exemplo fictício de carregamento do painel
    subprocess.run(['python', 'start_painel.py'], check=True)  # Supondo que tenha um arquivo 'start_painel.py' para iniciar o painel

# Função principal de menu
def menu_principal():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Iniciar o painel de administração")
        print("2 - Sair")
        print("3 - Iniciar carregamento do painel do site")
        
        opcao = input("Digite sua escolha (1/2/3): ")

        if opcao == "1":
            # Lógica do painel de administração (se já tiver)
            print("\nEntrando no painel de administração...")
            # Adicione aqui a sequência de código do painel de administração, se necessário
        elif opcao == "2":
            print("\nSaindo do painel de administração...")
            break  # Sair da sequência do painel de administração
        elif opcao == "3":
            iniciar_carregamento_painel()  # Inicia o carregamento do painel do site
        else:
            print("\nOpção inválida, por favor, tente novamente.")

import os
import subprocess
import webbrowser
import time

# Função para iniciar o servidor PHP local
def iniciar_servidor_php():
    print("Iniciando o servidor PHP local para o painel...")
    painel_pasta = 'C:/Users/Micro/Documents/codigos/ONLY/PHP/002/ESTRUTURA DO PROJETO'  # Altere para o caminho correto
    subprocess.Popen(['php', '-S', 'localhost:8000', '-t', painel_pasta])  # Inicia o servidor PHP
    time.sleep(2)  # Espera 2 segundos para garantir que o servidor está rodando
    print("Servidor PHP iniciado. O painel está acessível em http://localhost:8000")

# Função para exibir o menu principal no terminal
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

# Função para iniciar o start_painel.py a partir do Hello World.py
def iniciar_start_painel():
    try:
        print("Iniciando o arquivo start_painel.py...")

        # Caminho correto para o arquivo 'start_painel.py'
        caminho_arquivo = 'C:/Users/Micro/Documents/codigos/FR/start_painel.py'

        # Executar o arquivo start_painel.py
        subprocess.run(['python', caminho_arquivo], check=True)  # Ajuste o caminho se necessário
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar executar start_painel.py: {e}")
    except FileNotFoundError:
        print("Arquivo start_painel.py não encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função principal
def main():
    # Iniciar os arquivos da pasta
    pasta_raiz = 'FR'  # O caminho da pasta 002 dentro de ONLY/PHP
    iniciar_arquivos_da_pasta(pasta_raiz)  # Iniciar os arquivos que você tem na pasta ONLY/PHP/002
    
    # Iniciar o painel
    iniciar_painel()  

    # Se necessário, pode chamar a função para iniciar o painel diretamente
    # iniciar_start_painel()  

# Função para iniciar os arquivos da pasta
def iniciar_arquivos_da_pasta(pasta):
    # Aqui você pode incluir a lógica para iniciar os arquivos da pasta
    print(f"Iniciando os arquivos da pasta {pasta}...")

# Chama a função principal
if __name__ == "__main__":
    main()
    
import pyfiglet

# Texto que você quer exibir
texto = "DKISS ENGINEER®"

# Gerando o texto em estilo grande
resultado = pyfiglet.figlet_format(texto)

# Exibindo o resultado
print(resultado)

import subprocess
import time

def iniciar_servidor_php():
    print("Iniciando o servidor PHP local para o painel...")
    painel_pasta = 'C:/Users/Micro/Documents/codigos/ONLY/PHP/002/ESTRUTURA DO PROJETO'  # Ajuste o caminho
    subprocess.Popen(['php', '-S', 'localhost:8000', '-t', painel_pasta])  # Inicia o servidor PHP
    time.sleep(2)  # Espera 2 segundos para garantir que o servidor está rodando
    print("Servidor PHP iniciado. O painel está acessível em http://localhost:8000")

# Chama a função para iniciar o servidor
iniciar_servidor_php()

import webbrowser

def abrir_painel():
    url = "http://localhost:8000/painel"
    print(f"Abrindo o painel do site em: {url}")
    webbrowser.open(url)

# Chama a função para abrir o painel no navegador
abrir_painel()

import requests

def verificar_status_servidor():
    try:
        response = requests.get("http://localhost:8000")
        if response.status_code == 200:
            print("Servidor está ativo e funcionando!")
        else:
            print(f"Erro ao conectar com o servidor. Código de status: {response.status_code}")
    except requests.ConnectionError:
        print("Falha na conexão com o servidor.")

# Chama a função para verificar o status do servidor
verificar_status_servidor()

import os
import signal
import subprocess

def parar_servidor_php():
    print("Parando o servidor PHP...")
    # Obtenha o ID do processo do PHP e mate o processo (de forma simples)
    processo_php = subprocess.Popen(['taskkill', '/F', '/IM', 'php.exe'])
    processo_php.wait()
    print("Servidor PHP parado.")

# Chama a função para parar o servidor
parar_servidor_php()

def menu_principal():
    while True:
        print("\n--- Painel de Administração ---")
        print("1. Iniciar o painel do site")
        print("2. Ver status do servidor")
        print("3. Parar o servidor")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_servidor_php()  # Chama a função para iniciar o servidor
            abrir_painel()  # Abre o painel no navegador
        elif escolha == "2":
            verificar_status_servidor()  # Verifica o status do servidor
        elif escolha == "3":
            parar_servidor_php()  # Para o servidor PHP
        elif escolha == "4":
            print("Saindo do painel...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função do menu principal
menu_principal()

import logging

# Configura o logging para capturar erros
logging.basicConfig(filename='painel_log.txt', level=logging.DEBUG)

def registrar_erro_mensagem(mensagem):
    logging.error(mensagem)

def registrar_informacao_mensagem(mensagem):
    logging.info(mensagem)

# Exemplo de como registrar um erro
try:
    x = 1 / 0  # Provoca um erro de divisão por zero
except Exception as e:
    registrar_erro_mensagem(f"Ocorreu um erro: {e}")

# Exemplo de como registrar uma mensagem de informação
registrar_informacao_mensagem("Painel iniciado com sucesso.")

def adicionar_usuario(nome, email):
    print(f"Usuário {nome} com o email {email} foi adicionado ao sistema.")
    # Aqui você poderia adicionar os dados a um banco de dados ou arquivo

# Exemplo de uso
adicionar_usuario("João", "joao@exemplo.com")

import unittest

class TesteServidor(unittest.TestCase):
    def test_status_servidor(self):
        response = requests.get("http://localhost:8000")
        self.assertEqual(response.status_code, 200)

    def test_painel_respondendo(self):
        response = requests.get("http://localhost:8000/painel")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

import psutil

def monitorar_uso():
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    print(f"Uso da CPU: {cpu}%")
    print(f"Uso da Memória: {memoria}%")

# Chama a função para monitorar o uso
monitorar_uso()
import psutil

