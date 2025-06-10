function gerarQRCode() {
    const text = document.getElementById('qrInput').value;
    const qrImage = document.getElementById('qrImage');

    if (!text) {
        alert('Por favor, digite algum conteúdo.');
        return;
    }

    fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.qr_code) {
            qrImage.src = 'data:image/png;base64,' + data.qr_code;
        } else {
            alert('Erro ao gerar QR Code');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao conectar com o servidor.');
    });
}