<template>
    <div id="modal-window-cont">
        <div id="success" class="white">
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="checkmark" width="40" zoomAndPan="magnify" viewBox="0 0 30 30.000001" height="40" preserveAspectRatio="xMidYMid meet" version="1.0"><defs><clipPath id="id1"><path d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656 " clip-rule="nonzero"/></clipPath></defs><g clip-path="url(#id1)"><path d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125 " fill-opacity="1" fill-rule="nonzero"/></g></svg>
            You have bought a tarrif!
        </div>
        <div id="payment-block">
            <div id="paypal-button-container"> </div>
        </div>
    </div>
</template>

<script>
export default {
  mounted() {
    this.loadPayPalSDK().then(() => {
      this.setupPayPalButtons();
    });
  },
  methods: {
    loadPayPalSDK() {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = `https://www.paypal.com/sdk/js?client-id=${this.clientId}&vault=true&intent=subscription`;
        script.async = true;
        script.onload = resolve;
        script.onerror = reject;
        document.body.appendChild(script);
      });
    },
    setupPayPalButtons() {
      const vm = this
      paypal.Buttons({
        createSubscription: function(data, actions) {
          return actions.subscription.create({
            'plan_id': 'P-50D947788Y1605602MULQ3ZA'
          });
        },
        onApprove: function(data, actions) {
          const success_window = document.getElementById('success')
          const payment_block = document.getElementById('payment-block')
          success_window.classList.add('visible')
          payment_block.classList.add('hide')
          console.log(data)
          setTimeout(() => {
            success_window.classList.remove('visible')
            payment_block.classList.remove('hide')
            vm.changeState()
          }, 10000)
        }
      }).render('#paypal-button-container');
    },
    changeState() {
        this.$emit('update:modelValue', false);
    }
  }
};
</script>

<style>
#modal-window-cont {
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
    z-index: 110;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: .3s;
}

#payment-block {
    width: 20%;
    height: auto;
    padding: 20px 50px;
    background-color: var(--first_color);
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

#success {
    position: fixed;
    width: 20%;
    height: auto;
    background-color: rgb(125, 252, 121);
    border-radius: 20px;
    padding: 50px 20px;
    justify-content: center;
    align-items: center;
    display: none;
    transition: .3s;
    z-index: 112;
    gap: 10px;
}

.checkmark {
    fill: #fff;
}
</style>