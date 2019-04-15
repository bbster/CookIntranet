<template>
   <div>
    <Scaduler class="scaduler"/>
    <Feed class="feed"   :title-data="feed.titleData" :header-data="feed.headerData"/>
  </div>
</template>

<script>
import Scaduler from '@/components/scaduler/Scaduler'
import Feed from '@/components/feed/Feed'

export default {
  layout: 'default',
  components: {
    Scaduler,
    Feed
  },
  data: () => ({
    feed: {
      titleData: '공지',
      headerData: [
        { text: '작성자', value: 'manager' },
        { text: 'STAFF', value: 'staff' },
        { text: 'STATUS', value: 'status' },
        { text: '내용', value: 'memo' }
      ]
    }
  })
}
</script>

<style lang="stylus" scope="this api replaced by slot-scope in 2.5.0+">
.v-navigation-drawer
  z-index 9000
.v-overlay
  z-index 8000
</style>