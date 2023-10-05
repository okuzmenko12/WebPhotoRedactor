// static/main.js

console.log("Sanity check!");

// Get Stripe publishable key
fetch("/api/v1/subscriptions/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  console.log(data)
  const stripe = Stripe(data.public_key);

  // new
  // Event handler
  let submitBtn = document.querySelector("#submitBtn");
  if (submitBtn !== null) {
    submitBtn.addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/api/v1/subscriptions/create-checkout-session/")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.checkout_session_id})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});



