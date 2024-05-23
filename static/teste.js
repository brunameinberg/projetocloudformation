// Função para carregar as mensagens do servidor e exibi-las na página
function carregarMensagens() {
    fetch('/teste')  // Alterado para a rota correta (/teste) para carregar as mensagens
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, 'text/html');
        const mensagens = doc.querySelectorAll('#mensagens li');
        const ul = document.getElementById('mensagens');
        ul.innerHTML = ''; // Limpa a lista atual de mensagens
        mensagens.forEach(mensagem => {
            const li = document.createElement('li');
            li.textContent = mensagem.textContent;
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

            const formData = new FormData(formMensagem);
            const data = new URLSearchParams(formData);

            // Envia a requisição POST via AJAX
            fetch('/salvar_dados', {
                method: 'POST',
                body: data,
            })
            .then(response => {
                if (response.ok) {
                    carregarMensagens();
                } else {
                    console.error('Erro ao enviar a mensagem.');
                }
            })
            .catch(error => console.error('Erro:', error));

            // Limpa o formulário
            formMensagem.reset();
        });
    }
};
