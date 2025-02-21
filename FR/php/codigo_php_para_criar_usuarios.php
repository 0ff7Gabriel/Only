<?php
// Conex�o com o banco de dados
require_once '../includes/config.php';  // Ajuste o caminho conforme sua estrutura

// Dados do novo usu�rio
$nome = "Dkiss";
$email = "dkissartist@gmail.com";
$senha = "14082003";  // Senha fornecida
$is_admin = 1;  // Indicando que o usu�rio ser� um administrador

// Hash da senha
$hashedSenha = password_hash($senha, PASSWORD_DEFAULT);

// Preparando o SQL para inserir o usu�rio no banco
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
        "message" => "Usu�rio Dkiss registrado com sucesso como administrador!"
    ]);
} else {
    echo json_encode([
        "message" => "Erro ao registrar o usu�rio."
    ]);
}
?>
