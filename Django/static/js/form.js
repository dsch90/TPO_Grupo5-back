const nombre = document.getElementById("nombre")
const email = document.getElementById("email")
const comentario = document.getElementById("comentario")
const parrafo = document.getElementById("warnings")
const form = document.getElementById("form")

form.addEventListener("submit", e=>{
	e.preventDefault()
	let warnings = ""
	let entrar = false
	//let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
	
	if(nombre.value.length < 2){
		warnings += 'El nombre no es valido <br>'
		entrar = true
	}
	if(comentario.value.length < 1){
		warnings += 'Comentario requerido <br>'
		entrar = true
	}
	if(entrar){
		parrafo.innerHTML = warnings
	}
	
})
///Envio de mail
const btn = document.getElementById('button')

           document.getElementById('form')
            .addEventListener('submit', function(event) {
              event.preventDefault()
           
              btn.value = 'Enviando...'
           
              const serviceID = 'default_service'
              const templateID = 'template_fyu01zl'
           
              emailjs.sendForm(serviceID, templateID, this)
               .then(() => {
                 btn.value = 'ENVIAR MENSAJE'
                 form.reset()
                 alert('Mensaje enviado!')
               }, (err) => {
                 btn.value = 'ENVIAR MENSAJE'
                 alert(JSON.stringify(err))
               })
           })