<template>
  <v-layout justify-space-between wrap>
    <v-flex xs12 sm4 md4 class="my-2 px-1">
      <v-date-picker
        ref="picker"
        v-model="date"
        full-width
        show-current
        first-day-of-week="1"
        locale="ko-kr"
      ></v-date-picker>
    </v-flex>

    <v-flex xs12 sm4 md4 class="my-2 px-1 scheduler_wrap">
      <div class="scheduler">
       <div class="scaduleTitle">{{ date || '날짜를 선택해주세요' }}</div>
        <no-ssr>
        <v-list  two-line>
            <v-list-tile
            v-for="(note, index) in notes"
            :key="note.content"
            @click="selectDate(index)"
            >
              <v-list-tile-content>
                <v-list-tile-title>{{note.title}}</v-list-tile-title>
                <v-list-tile-sub-title>{{note.author}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
        </v-list>
        </no-ssr>
        </div>
    <Modal v-bind:date="date"/>

    </v-flex>

    <v-flex xs12 sm4 md4 class="my-2 px-1">
      <v-subheader>{{ notes[noteidx].title + ' ' + notes[noteidx].time || '일정을 선택해주세요' }}</v-subheader>
      <ul class="ma-3">
        <li>일정 상세내용<br/>{{ notes[noteidx].content }}</li>
        <li>주소<br/><a :href="'https://www.google.co.kr/maps/search/'+notes[noteidx].address">{{ notes[noteidx].address }}</a></li>
        <li>전화<br/><a :href="'tel:'+notes[noteidx].tel">{{ notes[noteidx].tel }}</a></li>
        <li>대금<br/>{{ notes[noteidx].price }}원</li>

      </ul>
    </v-flex>
  </v-layout>
  
</template>

<script>
  import API from '@/api'
  import ScadulModal from '@/components/scaduler/ScadulModal'

  export default {
    components: {
      'Modal': ScadulModal
    },
    data: () => ({
      dialog: false,
      date: null,
      noteidx: 0,
      notes: [{
        title: null,
        author: null,
        content: null,
        product: null,
        price: null,
        address: null,
        tel: null,
        time: null,
        type: null
      }]
    }),
    methods: {
      selectDate (index) {
        this.noteidx = index
      }
    },
    computed: {
      // getScadule () {
      //   return API.getScadule()
      // }
    },
    watch: {
      date (date) {
        /* 해당날짜 일정리스트 가져오기 */
        console.log(date)
        this.notes = API.getScadule()
      }
    },
    created () {
    // can use Data(this.title, this.titleComputed ...), events(vm.$on, vm.$once, vm.$off, vm.$emit)
      this.date = new Date().toISOString().substr(0, 10)
      this.notes = API.getScadule()
    }
  }
</script>

<style lang="stylus" scope="this api replaced by slot-scope in 2.5.0+">
@require '~assets/style/variables'
.v-date-picker-title__date
  font-size 25px
.scheduler_wrap
  position relative
  .scheduler
    position relative
    height 365px
    overflow-y scroll
    -ms-overflow-style none
    box-shadow default
    .scaduleTitle
      position sticky
      top 0
      background #303030
      z-index 1
    .scaduler_fab
      z-index 9999
::-webkit-scrollbar
  display none;
</style>
