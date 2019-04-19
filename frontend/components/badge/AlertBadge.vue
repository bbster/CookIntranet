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
                      <span>{{ item.avatar }}</span>
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
              avatar: '용국',
              title: '용궁횟집',
              subtitle: "<span class='text--primary'>배송</span> &mdash; 나는 헌법을 준수하고 국가를 보위하며 조국의 평화적 통일과 국민의 자유와 복리의 증진 및 민족문화의 창달에 노력하여 대통령으로서의 직책을 성실히 수행할 것을 국민 앞에 엄숙히 선서합니다."
            },
            {
              avatar: '용국',
              title: '밥통옆 밥뜨기전 자기이름 내리기',
              subtitle: "<span class='text--primary'>공지</span> &mdash; 나는 헌법을 준수하고 국가를 보위하며 조국의 평화적 통일과 국민의 자유와 복리의 증진 및 민족문화의 창달에 노력하여 대통령으로서의 직책을 성실히 수행할 것을 국민 앞에 엄숙히 선서합니다. "
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