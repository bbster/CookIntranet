  <template>
    <v-menu
    :close-on-content-click="true"
    transition="scale-transition"
    origin="top right"
    >
      <template v-slot:activator="{ on }">
        <v-badge
        overlap
        color="orange"
        >
          <template v-slot:badge >
              <span >{{countBadge}}</span>
          </template>
        <v-icon
          medium
          color="grey darken-1"
          v-on="on"
        >
            notifications
        </v-icon>
      </v-badge>
    </template>
    <v-list two-line >
          <template v-for="(item, index) in items">
                <v-list-tile
                  :key="index"
                  avatar
                  @click="toFeed"
                >
                  <v-list-tile-avatar>
                    <img :src="item.avatar">
                  </v-list-tile-avatar>

                  <v-list-tile-content>
                    <v-list-tile-title v-html="item.title"></v-list-tile-title>
                    <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
                  </v-list-tile-content>
                </v-list-tile>
          </template>
        </v-list>
    </v-menu>
  </template>
    
  <script>
    export default {
      data () {
        return {
          items: [
            {
              avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
              title: 'Brunch this weekend?',
              subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
            },
            {
              avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
              title: 'Brunch this weekend?',
              subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
            }
          ]
        }
      },
      computed: {
        countBadge () {
          return this.items.length
        }
      },
      methods: {
        toFeed () {
        }
      }
    }
  </script>