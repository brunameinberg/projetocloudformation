// Função para carregar as mensagens do servidor e exibi-las na página
function carregarMensagens() {
    fetch('/teste')  // Alterado para a rota correta (/teste) para carregar as mensagens
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
window.onload = function() {
    carregarMensagens();

    // Adiciona um event listener ao formulário
    const formMensagem = document.getElementById('formMensagem');
    if (formMensagem) {
        formMensagem.addEventListener('submit', function(event) {
            event.preventDefault(); // Impede o envio padrão do formulário

            // Recarrega as mensagens
            carregarMensagens();

            // Limpa o formulário
            formMensagem.reset();
        });
    }
};
