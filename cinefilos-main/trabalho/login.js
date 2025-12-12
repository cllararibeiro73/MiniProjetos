import dicionarioteste from "./cadastro";

const senhainput = document.getElementById('senha');
const usuarioinput = document.getElementById('usuario');
let i = 0;
let teste = false

function logar(){
    while (teste != true){
        if (dicionarioteste[i].usuario == usuarioinput){
            if (dicionarioteste[i].senha == senhainput){
                alert("deu tudo certo")
                teste = true
            }
        } else{
            if (dicionarioteste.length == i){
                alert("usuario nao cadastrado")
                break
            }
            else{
                i++
            }
        }
    }
    
}