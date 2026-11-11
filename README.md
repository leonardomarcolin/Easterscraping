# Easterscraping

## Sobre o projeto

Se você é fã dos chocolates da Stuttgart, este script é para você. Basta executar o arquivo para enviar a si mesmo (ou a qualquer pessoa cujo e-mail você tenha) um relatório com todos os chocolates disponíveis e seus respectivos preços na seção de bomboniere do site da Stuttgart.

O projeto foi feito em **Python** como linguagem principal e **MySQL** como banco de dados para armazenar as informações.

## Requisitos

Para que o script funcione corretamente, você precisará ter instalado:

- MySQL 8.0
- Python 3.13
- Um editor de código que suporte Python (eu recomendo o VSCode)
- Um e-mail para enviar os relatórios, com **senha de app** configurada
- Um e-mail para receber os relatórios

## Como usar

1. Baixe o arquivo `.py` e o `requirements.txt`.
2. Abra o `.py` no seu editor de código e altere, no final do código, o e-mail de envio, a senha de app e o e-mail de destino.
3. Confira as credenciais do MySQL no início do código (por padrão: host `localhost`, usuário `root` e senha `root`) e ajuste conforme a sua instalação.
4. Abra o terminal na pasta do projeto e instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute o script:

   ```bash
   python main.py
   ```

> **Observação:** o projeto vem originalmente com um e-mail de exemplo (tanto para envio quanto para recebimento) e uma senha de app de exemplo. Troque por seus dados antes de executar.

> **Atenção:** a cada execução, o script apaga e recria o banco de dados `CHOCOLATERIA`. Não utilize esse nome se você já tiver um banco com ele no seu MySQL.

## Gerando um executável (opcional)

Se quiser transformar o script em um arquivo executável, rode no terminal:

```bash
pyinstaller --onefile --noconsole main.py
```

Serão criadas novas pastas no diretório do script. Abra a pasta `dist` e, dentro dela, você encontrará o script como um arquivo `.exe`, que enviará o e-mail toda vez que for aberto.
