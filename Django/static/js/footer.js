/* footer */

class MyFooter extends HTMLElement{
    connectedCallback() {
        this.innerHTML = `
        <footer class="pie-de-pagina">
            <div class="parte-logo">
                <img id="logo" src="/images/logo.png">
                <p class="copyright">&copy Copyright CaRent - 2023</p>
            </div>
            <div class="dias-horarios">
                <p> Dias y horarios de atención: </p>
                <p> Lunes a Sábados de 9 a 21 hs </p>

                <p> Atención telefónica: </p>
                <p> 0800 - carent </p>
            </div>
            <div class="parte-enlaces">
                <p><a class="adesarrolladoras" href="desarrolladoras.html"> Desarrolladoras </a></p>
            </div>
        </footer>
        `
    }
}
customElements.define('my-footer', MyFooter)