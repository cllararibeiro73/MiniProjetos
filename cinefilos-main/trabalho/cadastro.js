const form = document.querySelector('#butaooo')
const emailinput = document.getElementById('email')
const senhainput = document.getElementById('senha')
const usuarioinput = document.getElementById('usuario')

let dicionarioteste = [
    {usuario: "admin",
    senha: "admin"},
    {usuario: "teo",
    senha: "teo"},
    {usuario: "romerito",
    senha: "romerito"},
    {usuario: "ifrn",
    senha: "ifrn"},
    {usuario: "lourranny",
    senha: "lourranny"},
]


function funcao() {
// verificar se o nome está vazio
    if(usuarioinput.value ===""){
        alert("por favor, preencha o usuário com seu nome");
        return;
    } 
//verificar se o e-mail está preenchido e se é válido
    if(emailinput.value === "" || !isEmailValid(emailinput.value)){
        alert("por favor,preencha o seu e-mail");
        return;
    }
// se toods os campos estiverem corretamente preenchidos,envie o form
    dicionarioteste.push( {usuario: usuarioinput.value, senha: senhainput.value} )
    location.href = "./login.html"
}

// função que válida e-mail
function isEmailValid(email){
    //criar uma regex para validar email
    const emailRegex = new RegExp(
        /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$/
    );
    if(emailRegex.test(email)){
        return true
    }
    return false;
}

const senhainput2 = document.getElementById('senha2');
const usuarioinput2 = document.getElementById('usuario2');
let i = 0;
let teste = false

function logar(){
    while (teste != true){
        if (dicionarioteste[i].usuario == usuarioinput2.value){
            if (dicionarioteste[i].senha == senhainput2.value){
                alert("deu tudo certo")
                teste = true
            }
        } else{
            if (i == dicionarioteste.length){
                alert("usuario nao cadastrado")
            }
            else{
                i++
            }
        }
    }
    
}