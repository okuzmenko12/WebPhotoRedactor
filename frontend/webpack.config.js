const Dotenv = require('dotenv-webpack');

module.exports = {
  resolve: {
    fallback: {
      "crypto": require.resolve("crypto-browserify"),
      'crypto-browserify': require.resolve("crypto-browserify")
    },
  },
  plugins: [
    new Dotenv({
      path: '.env.development'
    })
  ],
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
    ],
  },
};