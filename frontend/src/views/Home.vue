<template>
  <div class="home">
    <h1>Create your unique name card!</h1>
    <router-link to="/create">
      <el-button>作成</el-button>
    </router-link>
    <router-link to="/gallery">
      <el-button>表示</el-button>
    </router-link>
  </div>
</template>

<script>
import {upload, download} from "@/plugins/auth"
export default {
  name: 'home',
  data () {
    return {
      uploadImageUrl: '',
    }
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style scoped>
.data-table {
  width: 80%;
  margin: auto;
}
</style>
