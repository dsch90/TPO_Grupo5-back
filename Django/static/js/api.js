const listaComentarios = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/comments");
    const comments = await response.json();

    let tableBody = ``;
    comments.forEach((comment, index) => {
        tableBody += `  <div class="comentarios_contenedor">
                            <div class="comentarios_caja">
                                <div class="caja-top">
                                    <div class="perfil">
                                        <div class="nombre-cliente">
                                            <strong>${comment.id}</strong></span>
                                            <span id="email">${comment.email}</span>
                                        </div>
                                    </div>                            
                                    <div class="reseñas">
                                        <p class="fas fa-star">"${comment.body}"</p>
                                    </div>
                                </div>
                            </div>
                        </div>`;
    });
    //document.getElementById("tableBody_Comments").innerHTML = tableBody;
    comentarios_json.innerHTML = tableBody;
};
window.addEventListener("load", function () {
    listaComentarios();
});

