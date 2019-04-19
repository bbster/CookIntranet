<template>
  <v-app dark v-resize="checkMobile">
    <v-navigation-drawer
      :mini-variant.sync="miniVariant"
      :clipped="clipped"
      v-model="drawer"
      fixed
      app
    >
      <v-list>
        <v-list-tile
          router
          :to="item.to"
          :key="i"
          v-for="(item, i) in items"
          exact
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar fixed app :clipped-left="clipped" class="nav">
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-btn
        v-if="!isMobile"
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
      </v-btn>
      <v-btn
        v-if="!isMobile"
        icon
        @click.stop="clipped = !clipped"
      >
        <v-icon>web</v-icon>
      </v-btn>
      <!-- <v-btn
        icon
        @click.stop="fixed = !fixed"
      >
      </v-btn> -->
      <v-toolbar-title  v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <AlertBadge/>
      <v-btn
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>

        <nuxt />

    </v-content>
    
    <v-navigation-drawer
      temporary
      :right="right"
      v-model="rightDrawer"
      fixed
    >
      <v-list>
        <v-list-tile
          router
          :to="item.to"
          :key="i"
          v-for="(item, i) in itemsRight"
          exact
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>
    <v-footer :fixed="fixed" app>
      <span>&copy; The Cook {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import IsMobile from '@/mixin/isMobile'
import AlertBadge from '@/components/badge/AlertBadge'

export default {
  components: {
    AlertBadge
  },
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [
        { icon: 'apps', title: 'Main', to: '/' },
        { icon: 'bubble_chart', title: 'Product', to: '/product' },
        { icon: 'bubble_chart', title: '임시', to: '/login' },
        { icon: 'bubble_chart', title: '임시', to: '/' }
      ],
      itemsRight: [
        { icon: 'apps', title: '임시', to: '/' },
        { icon: 'bubble_chart', title: '임시', to: '/' },
        { icon: 'bubble_chart', title: '임시', to: '/' },
        { icon: 'bubble_chart', title: '임시', to: '/' }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Admin'
    }
  },
  mixins: [IsMobile]
}
</script>

<style lang="stylus" scope="this api replaced by slot-scope in 2.5.0+">
.v-navigation-drawer
.v-overlay
  z-index 8000
</style>