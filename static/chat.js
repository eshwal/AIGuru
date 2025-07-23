  const chatBody = document.getElementById("chat-body");
  const input = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");

  function formatTime(num) {
    return num.toString().padStart(2, "0");
  }

  function scrollToBottom(el) {
    el.scrollTop = el.scrollHeight;
  }

  async function sendMessage() {
    const userText = input.value.trim();
    if (userText === "") return;

    sendBtn.disabled = true;
    const now = new Date();
    const timeStr = `${formatTime(now.getHours())}:${formatTime(now.getMinutes())}`;

    // User message
    const userRow = document.createElement("div");
    userRow.className = "chat-row user";

    const userAvatar = document.createElement("img");
    userAvatar.className = "avatar";
    //userAvatar.src = "https://i.pravatar.cc/40?u=user"; 
    userAvatar.src = "/static/user.jpg";// User avatar

    const userMsg = document.createElement("div");
    userMsg.className = "chat-message user-message";
    userMsg.innerHTML = `${userText}<span class="timestamp">${timeStr}</span>`;

    userRow.appendChild(userMsg);
    userRow.appendChild(userAvatar);
    chatBody.appendChild(userRow);
    scrollToBottom(chatBody);

    input.value = "";

    // Typing indicator
    const typingRow = document.createElement("div");
    typingRow.className = "chat-row bot";
    typingRow.id = "typing";

    const botAvatar = document.createElement("img");
    botAvatar.className = "avatar";
    //botAvatar.src = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png";
    botAvatar.src = "/static/assistant.jpg"; // Bot avatar

    const typingMsg = document.createElement("div");
    typingMsg.className = "chat-message bot-message";
    typingMsg.textContent = "Typing...";

    typingRow.appendChild(botAvatar);
    typingRow.appendChild(typingMsg);
    chatBody.appendChild(typingRow);
    scrollToBottom(chatBody);

    try {
      const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
      });

      const data = await response.json();
      const botText = data?.reply || "Sorry, I couldn't understand that.";
      const botTimeStr = `${formatTime(new Date().getHours())}:${formatTime(new Date().getMinutes())}`;

      document.getElementById("typing").remove();

      const botRow = document.createElement("div");
      botRow.className = "chat-row bot";

      const botMsg = document.createElement("div");
      botMsg.className = "chat-message bot-message";
      botMsg.innerHTML = `${botText}<span class="timestamp">${botTimeStr}</span>`;

      botRow.appendChild(botAvatar.cloneNode());
      botRow.appendChild(botMsg);
      chatBody.appendChild(botRow);
    } catch (error) {
      document.getElementById("typing").remove();

      const errorRow = document.createElement("div");
      errorRow.className = "chat-row bot";

      const errorMsg = document.createElement("div");
      errorMsg.className = "chat-message bot-message text-danger";
      errorMsg.textContent = "⚠️ Error: " + error.message;

      errorRow.appendChild(botAvatar.cloneNode());
      errorRow.appendChild(errorMsg);
      chatBody.appendChild(errorRow);
    }

    sendBtn.disabled = false;
    scrollToBottom(chatBody);
  }

  sendBtn.addEventListener("click", sendMessage);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
  });