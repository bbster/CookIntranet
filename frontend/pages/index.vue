<template>
   <div>
    <Scaduler class="scaduler"/>
    <Feed class="feed" :title-data="feed.titleData" :header-data="feed.headerData"/>
  </div>
</template>

<script>
import Scaduler from '@/components/scaduler/Scaduler'
import Feed from '@/components/feed/Feed'
import NewFeed from '@/components/feed/NewFeed'

export default {
  layout: 'default',
  components: {
    Scaduler,
    Feed,
    NewFeed
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
