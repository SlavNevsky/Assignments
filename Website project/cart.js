//cart 
let cartIcon =document.querySelector('cart-icon');
let cart = document.querySelector(".cart");
let CloseCart = document.querySelector("#close-cart");

//for open cart
jQuery(document).ready(function(){
    jQuery(".cart").addClass("active");
})

jQuery("#close-cart").ready(function(){
    jQuery(".cart").removeClass("active");
})


//Cart Working JS

if(document.readyState == "loading"){
    document.addEventListener("DOMContentLoaded", ready); 
}
else{
    ready();
}

//Making function
function ready(){
    var removeCartButtons = document.getElementsByClassName("cart-remove");
    console.log(removeCartButtons);
    for(var i=0; i<removeCartButtons.length; i++){
        var button= removeCartButtons[i];
        button.addEventListener("click",removeCartItem);
    }
    //Quantity Changes
    var quantityInputs = document.getElementsByClassName("cart-quantity");
    for(var u=0; i<quantityInputs.length; i++){
        var input = quantityInputs[i];
        button.addEventListener("click",quantityChanged)
    }

    //Add to Cart
    var quantityInputs = document.getElementsByClassName("add-cart");
    for(var u=0; i<quantityInputs.length; i++){
        var input = addCart[i];
        button.addEventListener("click",addCart)
    }

    document.getElementsByClassName("btn-buy")[0].addEventListener("click",buyButtonClicked)

}

//Buy Button
function buyButtonClicked(){
    alert("Your Order is Placed")
    var cartContent = document.getElementsByClassName("cart-conetnt")[0];
    while(cartContent.hasChildNodes()){
        cartContent.removeChild(cartContent.firstChild);
    }
    updatetotal();
}

//Remove Item from Cart

function removeCartItem(event){
    var buttonClicked = event.remove();
    buttonClicked.parentElement.remove();
    updatetotal();
}

//Quantity CHanges

function quantityChanged(event){
    var input = event.target;
    if(isNaN(input.value)|| input.value<=0){
        input.value=1;
    }
}

//Add to cart
function addCartClicked(event){
    var button = event.target;
    var shopProducts= buttonparentElement;
    var title = shopProducts.getElementsByClassName("product-title")[0].innerText;
    var price = shopProducts.getElementsByClassName("price")[0].innerText;
    var productImg =shopProducts.getElementsByClassName("product-img")[0].src;
    addProductToCart(title, price, productImg);
    updatetotal();
}

function addProductToCart(title, price, productImg){
    var cartShopBox = document.createElement("div");
    cartShopBox.classList.add("cart-box");
    var cartItem = document.getElementsByClassName("cart-content")[0];
    var cartItemNames = cartItems.getElementsByClassName("cart-product-title");
    for(var i=0; i<cartItemNames.length; i++){
        
        if(cartItemNames[i].innerText==title){
            alert("You already added to the cart. Increase the Quantity");
            return
        }
    }
    
    var cartBoxContent = <img src="${productImg}" class= "cart-img">
                            <div class="detail-box">
                            <div class="cart-product-title">${title}</div>
                            <div class="cart-price">${price}</div>
                            <input type="number" value="1" class="cart-quantity"></input> 
                            </div>
                            <i class="fa-solid fa-trash cart-remove"></i>;
                            
    cartShopBox.innerHTML=cartBoxContent;
    cartItems.append(cartShopBox);
    updatetotal();

    cartShopBox.getElementsByClassName("cart-remove")[0].addEventListener("click",removeCartItem);
    cartShopBox.getElementsByClassName("cart-quantity")[0].addEventListener("change",removeCartItem);
    cartShopBox.getElementsByClassName("cart-price")[0].addEventListener("change",removeCartItem);

}

//Update total
function updatetotal(){
    var cartContent = document.getElementsByClassName("cart-content")[0];
    var cartBoxes = document.getElementsByClassName("cart-content")[0];
    var total = 0;
    for (var i=0; i<cartBoxes.length; i++){
        var cartBox = cartBoxes[i];
        var priceElement = cartBox.getElementsByClassName("cart-price")[0];
        var quantityElement = cartBox.getElementsByClassName("cart-quantity")[0];
        var price = parseFloat(priceElement.innerText.replace("R ",""));
        var quantity = quantityElement.value;
        total = total+price*quantity;
    }
    //If price contains cents
    total = math.round(total*100)/100;
    document.getElementsByClassName("total-price")[0].innerText= "R"+total;

}