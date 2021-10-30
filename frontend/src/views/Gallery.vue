<template>
    <div class="gallery">
        <div class="wrapper grid">
          <div v-for="url in urls" class="item">
            <img style="width: 100px; height: 100px" :src="url"></img>
            <p><a href="">{{ url }}</a></p>
          </div>
        </div>
        
    </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/storage";
const axios = require('axios').create()
export default {
  name: 'gallery',
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
      // const response = await axios.get('/api');
      // this.tableData = response.data;
      // this.filename = response.data[0]['imgname'];
      
      // Firebaseに保存した画像のダウンロードURLを取得
      // console.log(this.filename);
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

.wrapper{
	max-width: 1100px;
	margin: 0 auto;
	padding: 0 4%;
}

.grid {
	display: grid;
	gap: 26px;
	grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
	margin-top: 6%;
	margin-bottom: 50px;
	text-align: center;
}
.grid p {
	text-align: center;
	color: #312F2F;
}


</style>
