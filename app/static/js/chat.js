/**
 * chat.js — Career Chat Page Logic
 * Handles sending messages to /career/ask and microphone recording.
 */

const chatMessages = document.getElementById("chat-messages");
const chatInput = document.getElementById("chat-input");

/**
 * Send the typed message to the backend and display the response.
 */
async function sendMessage() {
    const query = chatInput.value.trim();
    if (!query) return;

    // Show user message
    appendMessage(query, "user-message");
    chatInput.value = "";

    try {
        const res = await fetch("/career/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query }),
        });
        const data = await res.json();
        appendMessage(data.response || data.error, "ai-message");
    } catch (err) {
        appendMessage("⚠️ Network error. Please try again.", "ai-message");
    }
}

/**
 * Append a chat bubble to the message container.
 */
function appendMessage(text, className) {
    const div = document.createElement("div");
    div.className = `message ${className}`;
    div.innerHTML = `<p>${text}</p>`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Start browser speech recognition (Web Speech API).
 */
function startRecording() {
    if (!("webkitSpeechRecognition" in window || "SpeechRecognition" in window)) {
        alert("Speech recognition is not supported in this browser.");
        return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;

    recognition.onresult = (event) => {
        chatInput.value = event.results[0][0].transcript;
        sendMessage();
    };

    recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
    };

    recognition.start();
}

// Allow sending with Enter key
chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
});
