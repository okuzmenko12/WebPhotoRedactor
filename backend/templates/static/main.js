// static/main.js

console.log("Sanity check!");

// Get Stripe publishable key
fetch("/api/v1/payments/stripe/config/")
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

        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: "cs_test_a1reOgxfkM995QMsibO8oel6z1Mhnp4gyF9hp1UfYC0Z5XgvOlSqj6hun8"})

    });
  }
});



