document.getElementById('send-button').onclick = async function() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    // Hiển thị tin nhắn người dùng
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="message user-message">Bạn: ${message}</div>`;

    // Gửi tin nhắn đến backend
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    });
    const data = await response.json();

    // Hiển thị trả lời của bot
    chatBox.innerHTML += `<div class="message bot-message">Chatbot: ${data.reply}</div>`;
    input.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
};