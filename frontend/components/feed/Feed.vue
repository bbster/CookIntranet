<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title>{{titleData}}</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table
      :headers="headerData"
      :items="feeds"
      :expand="expand"
      item-key="id"
    >
      <template v-slot:items="props">
        <tr @click="props.expanded = !props.expanded">
          <td class="text-xs-right">{{ props.item.manager }}</td>
          <td class="text-xs-right">{{ props.item.staff }}</td>
          <td class="text-xs-right">{{ props.item.status }}</td>
          <td class="text-xs-right">{{ props.item.memo }}</td>
        </tr>
      </template>
      <template v-slot:expand="props">
        <v-card flat>
          <v-card-text>{{ props.item.memo }}</v-card-text>
        </v-card>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import API from '@/api'

export default {
  props: ['titleData', 'headerData'],
  data () {
    return {
      expand: false,
      feeds: [
        {}
      ]
    }
  },
  created () {
    this.feeds = API.getFeeds()
  }
}
</script>

<style lang="stylus" scope="this api replaced by slot-scope in 2.5.0+">

</style>
