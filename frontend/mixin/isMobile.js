const IsMobile = {
  created: function () {
    // this.onResize()
  },
  data () {
    return {
      isMobile: false
    }
  },
  methods: {
    checkMobile () {
      if (window.innerWidth < 769) { this.isMobile = true } else { this.isMobile = false }
    }
  }
}
export default IsMobile

/**
 * import IsMobile from '@/mixin/isMobile'
 * mixins: [IsMobile]
 * v-resize="checkMobile"
 * :class="{xs7: !isMobile}">
 * v-if="!isMobile"
 */
