async function sendMessage(){

    const input=document.getElementById("message");

    const message=input.value;

    if(message==="") return;

    const chat=document.getElementById("chat-box");

    chat.innerHTML+=`
    <div class="user">
        <b>You:</b> ${message}
    </div>
    `;

    input.value="";

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data=await response.json();

    chat.innerHTML+=`
    <div class="bot">
        <b>Category:</b> ${data.category}<br><br>

        <b>AI:</b> ${data.answer}
    </div>
    `;

    chat.scrollTop=chat.scrollHeight;

}