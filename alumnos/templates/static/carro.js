const shopContent = document.getElementById("shopContent");
const verCarrito = document.getElementById("btnCarro");
const modalContainer = document.getElementById("modal-container");

const productos =[
    {
        id: 1,
        nombre:"planta1",
        precio: 4000,
        img:"../src/GrupoHijuelas.jpg"
    },
    {
        id: 2,
        nombre:"planta2",
        precio:5000,
        img:"../src/plantainterior2.jpg"
    }
]
let carrito = [];

productos.forEach((product)=>{
    let content = document.createElement("div");
    content.className ="card"
    content.innerHTML = `
    <img src="${product.img}">
    <h3>${product.nombre}</h3>
    <p class="price">${product.precio}$</p>
    `;

    shopContent.append(content);

    let comprar = document.createElement("button")
    comprar.innerText = "comprar";
    comprar.className = "comprar";
    content.append(comprar);

    comprar.addEventListener("click", ()=>{
        carrito.push({
            id : product.id,
            img : product.img,
            nombre: product.nombre,
            precio:product.precio
        });
        console.log(carrito);
    });

});

verCarrito.addEventListener("click", () =>{
    modalContainer.innerHTML = "";
    modalContainer.style.display ="flex"
    
    const modalHeader = document.createElement("div");
    modalHeader.className = "modal-header"
    modalHeader.innerHTML = `
     <h1 class="modal-header-title">Carrito.</h1>
    `;
    modalContainer.append(modalHeader);

    const modalbutton = document.createElement("h1");
    modalbutton.innerText = "X";
    modalbutton.className = "modal-header-button";

    
    modalbutton.addEventListener("click", () => {
        modalContainer.style.display="none";
    });

    modalHeader.append(modalbutton);

    carrito.forEach((product) => {
        let carritoContent = document.createElement("div");
        carrito.className = "modal-content";
        carritoContent.innerHTML = `
            <img src="${product.img}">
            <h3>${product.nombre}</h3>
            <p>${product.precio} $ </p>
            <a href="../html/compraDatos.html" class="btn btn-primary">Comprar</a>
        `;
        modalContainer.append(carritoContent);
    });

    const total = carrito.reduce((acc, producto) => acc + producto.precio, 0);

    const totalBuying = document.createElement("div");
    totalBuying.className = "total-content";
    totalBuying.innerHTML = `total a pagar:${total}  $`;
    modalContainer.append(totalBuying);

});


