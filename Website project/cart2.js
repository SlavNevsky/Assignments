// Get necessary elements from the DOM
const cartTable = document.querySelector('#cart tbody');
const cartTotalElement = document.querySelector('#subtotal .total');
const checkoutButton = document.querySelector('.btn-buy');

let cartItems = [];
let cartTotal = 0;

// Function to calculate and update the cart total
function updateCartTotal() {
  let total = 0;
  for (let i = 0; i < cartItems.length; i++) {
    const item = cartItems[i];
    const subtotal = item.price * item.quantity;
    total += subtotal;
  }

  cartTotal = total;
  cartTotalElement.textContent = 'R ' + cartTotal.toFixed(2);
}

// Function to handle item removal from the cart
function removeCartItem(index) {
  cartItems.splice(index, 1);
  renderCartItems();
  updateCartTotal();
}

// Function to render cart items
function renderCartItems() {
  cartTable.innerHTML = '';
  for (let i = 0; i < cartItems.length; i++) {
    const item = cartItems[i];
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
      <td><a href="#"><i class="far fa-times-circle cart-remove" data-index="${i}"></i></a></td>
      <td><img src="${item.imageSrc}" alt="" class="product-img"></td>
      <td class="produc-title">${item.name}</td>
      <td class="price">R ${item.price.toFixed(2)}</td>
      <td><input type="number" min="1" value="${item.quantity}" data-index="${i}"></td>
      <td class="total">R ${(item.price * item.quantity).toFixed(2)}</td>
    `;

    const removeButton = newRow.querySelector('.cart-remove');
    removeButton.addEventListener('click', function () {
      const index = parseInt(this.dataset.index);
      removeCartItem(index);
    });

    const quantityInput = newRow.querySelector('input[type="number"]');
    quantityInput.addEventListener('change', function () {
      const index = parseInt(this.dataset.index);
      const newQuantity = parseInt(this.value);
      cartItems[index].quantity = newQuantity;
      updateCartTotal();
    });

    cartTable.appendChild(newRow);
  }
}

// Function to handle adding a new item to the cart
function addItemToCart(name, price, imageSrc) {
  const newItem = {
    name: name,
    price: price,
    imageSrc: imageSrc,
    quantity: 1,
  };

  cartItems.push(newItem);
  renderCartItems();
  updateCartTotal();
}

// Add event listener to the checkout button
checkoutButton.addEventListener('click', function () {
  alert('Redirecting to checkout page...');
});

// Example usage:
// Add some sample items to the cart
addItemToCart('Mens T-shirt', 300, '/images/s1.jpg');
addItemToCart('Womens Dress', 500, '/images/s2.jpg');
