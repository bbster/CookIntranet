<template>
  <v-layout>
    <v-flex text-xs-center></v-flex>
  </v-layout>
</template>

<script>
  import API from '@/api'

  export default {
    layout: 'default',
    data: () => ({

    }),
    computed: {
      getProductData () {
        return API.getProduct()
      }
    }
  }
</script>