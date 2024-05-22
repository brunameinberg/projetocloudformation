// Função para carregar as mensagens do servidor e exibi-las na página
function carregarMensagens() {
    fetch('/mensagens')
    .then(response => response.json())
    .then(data => {
        const ul = document.getElementById('mensagens');
        ul.innerHTML = ''; // Limpa a lista atual de mensagens
        data.forEach(mensagem => {
            const li = document.createElement('li');
            li.textContent = mensagem;
            ul.appendChild(li);
        });
    });
}

// Chama a função para carregar as mensagens ao carregar a página
window.onload = carregarMensagens;

// Adiciona um evento para recarregar as mensagens quando um novo envio for feito
document.getElementById('formMensagem').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    carregarMensagens(); // Recarrega as mensagens
    this.reset(); // Limpa o formulário
});
