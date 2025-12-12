//Javascript principal para todas as paginas//

window.addEventListener("scroll",function(){
    let transparente = document.querySelector(".cabecalho")
    transparente.classList.toggle("descer",window.scrollY > 0)
    let transparente2 = document.querySelector(".butao")
    transparente2.classList.toggle("descer2",window.scrollY > 0)
    let botaosubir = document.querySelector("#subir")
    botaosubir.classList.toggle("subida",this.window.scrollY > 0)
})