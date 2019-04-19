<template>
  <v-layout v-resize="checkMobile" column style="padding-top:56px">
    <v-toolbar card dense color="transparent"  flat>

      <v-flex xs8>
        <v-layout>
          <v-flex xs4 v-if="!isMobile">
            <v-toolbar-title class="hidden-xs-only"><h4>{{titleData}}</h4></v-toolbar-title>
          </v-flex>

          <v-flex :class="{xs7: !isMobile}">
            <v-text-field
            v-model="search"
            append-icon="search"
            label="검색"
            single-line
            ></v-text-field>
          </v-flex>
        </v-layout>
      </v-flex>

        <v-flex xs4>
        <v-menu
          ref="menu1"
          v-model="menu1"
          :close-on-content-click="false"
          :nudge-right="40"
          lazy
          transition="scale-transition"
          offset-y
          full-width
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="dateFormatted"
              label="Date"
              persistent-hint
              @blur="date = parseDate(dateFormatted)"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="date" no-title @input="menu1 = false" locale="ko-kr"></v-date-picker>
        </v-menu>
      </v-flex>   
    </v-toolbar>
            <v-data-table item-key="id" :headers="headers" :items="feeds" :search="search" :pagination.sync="pagination" :hide-headers="isMobile" :class="{mobile: isMobile}" :expand="expand">
              <template slot="items" slot-scope="props">
                <tr v-if="!isMobile"  @click="props.expanded = !props.expanded"
                :style="getColorByStatus(props.item.status)">
                  <td>{{ props.item.manager }}</td>
                  <td class="text-xs-right" ><span class="px-1" :key="staff" v-for="staff in props.item.staff">{{staff}}</span></td>
                  <td class="text-xs-right">{{ props.item.status }}</td>
                  <td class="text-xs-right">{{ props.item.title }}</td>
                </tr>
                <tr v-else  @click="props.expanded = !props.expanded"
                 :style="getColorByStatus(props.item.status)">
                  <td>
                    <ul class="flex-content" >
                      <li class="flex-item" data-label="Manager">{{ props.item.manager }}</li>
                      <li class="flex-item" data-label="Staff"><span class="px-1" :key="staff" v-for="staff in props.item.staff">{{staff}}</span></li>
                      <li class="flex-item" data-label="Status">{{ props.item.status }}</li>
                      <li class="flex-item" data-label="Title">{{ props.item.title }}</li>
                    </ul>
                  </td>
                </tr>
              </template>
              <template v-slot:expand="props">
                <div>{{ props.item.memo }}</div>
              </template>
              <v-alert slot="no-results" :value="true" color="error" icon="warning">
                "{{ search }}"를 포함한 결과를 찾을 수 없습니다 
              </v-alert>
            </v-data-table>
          </v-layout>
</template>


<script>
import { getFeeds } from '@/api'
import IsMobile from '@/mixin/isMobile'

export default {
  props: ['titleData'],
  data: vm => ({
    menu1: false,
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    expand: false,
    pagination: {
      sortBy: 'manager'
    },
    selected: [],
    search: '',
    headers: [{
      text: '작성자',
      align: 'left',
      value: 'manager'
    },
    {
      text: 'STAFF',
      align: 'right',
      value: 'staff'
    },
    {
      text: 'STATUS',
      align: 'right',
      value: 'status'
    },
    {
      text: 'TITLE',
      align: 'right',
      value: 'title'
    }
    ],
    feeds: [{
      value: false,
      manager: null,
      staff: [],
      status: null,
      title: null,
      memo: null
    }],
    colors: {
      '긴급': 'red',
      '중요': 'yellow',
      '보통': 'green'
    }
  }),
  mixins: [IsMobile],
  methods: {
    toggleAll () {
      if (this.selected.length) this.selected = []
      else this.selected = this.feeds.slice()
    },
    changeSort (column) {
      console.log(column)
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending
      } else {
        this.pagination.sortBy = column
        this.pagination.descending = false
      }
    },
    formatDate (date) {
      if (!date) return null

      const [year, month, day] = date.split('-')
      return `${month}/${day}/${year}`
    },
    parseDate (date) {
      if (!date) return null

      const [month, day, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    },
    getColorByStatus (status) {
      return { borderLeft: `6px solid ${this.colors[status]}` }
    }
  },
  created () {
    this.feeds = getFeeds()
  },
  watch: {
    date (val) {
      this.dateFormatted = this.formatDate(this.date)
      // 해당일 데이터 요청
    }
  }
}
</script>

<style lang="stylus" scope="this api replaced by slot-scope in 2.5.0+">
.mobile
    color: #333

@media screen and (max-width: 768px)
    .mobile table.v-table tr 
        max-width: 100%
        position: relative
        display: block

    .mobile table.v-table tr td:not(.v-datatable__expand-col)
        display: flex
        width: 100%
        border-bottom: 1px solid #f5f5f5
        height: auto
        padding: 20px 0
    .v-datatable__expand-row
        padding 2px 5px
    .mobile table.v-table tr td ul li:before
        content: attr(data-label)
        padding-right: .5em
        text-align: left
        display: block
        color: #999

    .v-datatable__actions__select
        width: 50%
        margin: 0px
        justify-content: flex-start

    .mobile .theme--light.v-table tbody tr:hover:not(.v-datatable__expand-row)
        background: transparent

.flex-content
    padding: 0
    margin: 0
    list-style: none
    display: flex
    flex-wrap: wrap
    width: 100%

.flex-item 
    padding: 5px
    width: 50%
    height: auto
    font-weight: bold

.v-datatable__expand-row
    padding 0 10px
    text-align justify
    border-bottom 2px solid black
</style>
