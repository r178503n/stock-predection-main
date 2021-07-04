const BundleTracker = require("webpack-bundle-tracker");
// const baseHost = "http://localhost:8000";
const baseProdHost = "https://docking-victoriabookings.herokuapp.com";
const staticPath = "/static/dist/";
//const baseLocalHost = "http://localhost:8000";
module.exports = {
  context: __dirname,
  output: {
    path: require("path").resolve("./distro/dist/"),
    filename: "[name]-[hash].js",
    publicPath: staticPath, //baseLocalHost + "/static/dist/",
  },

  plugins: [
    new BundleTracker({
      // path: __dirname,
      path: require("path").resolve("./"),
      filename: "webpack-stats-angular.json",
    }),
  ],
  devServer: {
        // for assets not handled by webpack
        contentBase:  require("path").resolve("./distro/dist/"),
        // port should be different from the one you use to run Django
        port: 9000,
        headers: {
          'Access-Control-Allow-Origin': '*'
        },
        // gzip everything served by dev server, could speed things up a bit
        compress: true,
        // HMR
        hot: true
    },
};

