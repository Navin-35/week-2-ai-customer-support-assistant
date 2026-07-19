async function sendMessage(){

    const input=document.getElementById("message");
    const message=input.value.trim();

    if(message==="") return;

    const chat=document.getElementById("chat-box");

    const time=new Date().toLocaleTimeString();

    chat.innerHTML+=`
    <div class="user">
        <b>You</b> (${time})<br>
        ${message}
    </div>
    `;

    input.value="";

    chat.innerHTML+=`
    <div id="typing" class="bot">
        🤖 Typing...
    </div>
    `;

    chat.scrollTop=chat.scrollHeight;

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

    document.getElementById("typing").remove();

    if(data.success){

        chat.innerHTML+=`
        <div class="bot">
            <b>${data.category}</b><br><br>
            ${data.answer}
        </div>
        `;

    }else{

        chat.innerHTML+=`
        <div class="bot">
            ❌ ${data.error}
        </div>
        `;
    }

    chat.scrollTop=chat.scrollHeight;
}


document.getElementById("message").addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});


async function clearChat(){

    await fetch("/clear",{
        method:"POST"
    });

    document.getElementById("chat-box").innerHTML="";
}