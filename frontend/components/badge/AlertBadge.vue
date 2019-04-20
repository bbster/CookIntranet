    <template>
            <v-badge
      overlap
      color="orange"
    >
      <template v-slot:badge>
        <span>{{countBadge}}</span>
      </template>
      <v-icon
        medium
        color="grey darken-1"
      >
        notifications
      </v-icon>
    </v-badge>
    </template>
    
    <script>
    export default {
      data () {
        return {
          countBadge: '5'
        }
      }
    }
    </script>