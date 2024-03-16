async function contarTags(url) {
    try {
        const response = await fetch(url);
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const tags = doc.getElementsByTagName('*');
        console.log("Total de tags:", tags.length);
    } catch (error) {
        console.error('Erro ao fazer a requisição para a página:', error);
    }
}

async function buscarDados() {
    const inputURL = document.getElementById('inputURL').value;
    const serverURL = await fetch ('http://localhost:3000/scraping', {
        method: 'POST',
        headers: {
            'content-type' : 'application/json',
        },
        body: JSON.stringify({ url }),

    })
        
    
    try {
        const contarTags = await response.JSON();
        contarTags(contarTags);
    } catch (error) {
        console.error('Erro ao fazer a requisição ao servidor intermediário:', error);
    }
}
