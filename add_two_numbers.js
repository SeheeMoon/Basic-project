function doSomething(){
    let a = document.getElementById('inputA').value;
    let b = document.getElementById('inputB').value;
    document.getElementById("ValueA").innerHTML = a;
    document.getElementById("ValueB").innerHTML = b;
    document.getElementById("ValueC").innerHTML = Number(a) + Number(b);
}