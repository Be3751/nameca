<template>
    <div class="show">
        <el-table class="data-table" :data="tableData" stripe>
            <el-table-column prop="id" label="ID" width="180"></el-table-column>
            <el-table-column prop="imgname" label="画像" width="180"></el-table-column>
            <el-table-column prop="name" label="名前" width="180"></el-table-column>
            <el-table-column prop="furigana" label="フリガナ"></el-table-column>
            <el-table-column prop="birthday" label="誕生日"></el-table-column>
            <el-table-column prop="favorite" label="趣味"></el-table-column>
            <el-table-column prop="skills" label="スキル"></el-table-column>
        </el-table>
        <div v-for="url in urls">
          <img style="width: 100px; height: 100px" :src="url"></img>
        </div>
    </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/storage";
const axios = require('axios').create()
export default {
  name: 'show',
  data () {
    return {
      tableData: [],
      filename: '',
      urls: [],
      fit: 'fill'
    }
  },
  mounted () {
    this.bindData()
  },
  methods: {
    bindData: async function () {
      // Axios経由で取得したDB情報をテーブルにバインド
      const response = await axios.get('/api');
      this.tableData = response.data;
      this.filename = response.data[0]['imgname'];
      
      // Firebaseに保存した画像のダウンロードURLを取得
      console.log(this.filename);
      // const imgpath = "images/" + this.filename;
      // console.log(imgpath);
      const storageRef = await firebase.storage().ref("images");
      const fileList = await storageRef.listAll();
      console.log(fileList)
      fileList.items.forEach(itemRef => {
        itemRef.getDownloadURL().then(url => {
          console.log(url)
          this.urls.push(url)
        })
      });
    },
  },
  computed: {
  }
}
</script>

<style scoped>
.data-table {
  width: 80%;
  margin: auto;
}
</style>
