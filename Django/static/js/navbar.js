/* barra de navegacion */
class navBar extends HTMLElement{
    connectedCallback() {
      this.innerHTML =`
        <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
          <div class="container-xl">
              <a class="navbar-brand" href="index.html">
              <img src="/images/logo.png" alt="logo" width="40" height="35" class="d-inline-block align-text-top"> CaRent</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Vehiculos</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/nosotros.html">Acerca de nosotros</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/formulario_Carent.html">Contacto</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      ` 
    }
  }
  customElements.define('my-navbar', navBar)