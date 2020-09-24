const path = require('path')

module.exports = {
  productionSourceMap: false,
  css: {
    loaderOptions: {
      stylus: {
        import: [path.join(__dirname, './public/setting/color.styl')]
      }
    }
  }
}
