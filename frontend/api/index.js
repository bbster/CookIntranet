// implement your own methods in here, if your data is coming from A rest API

import * as Product from './product'
import * as Scadule from './Scadule'
import * as Feeds from './Feeds'

export default {
  // order
  getProduct: Product.getProduct,
  getScadule: Scadule.getScadule,
  getFeeds: Feeds.getFeeds
}
