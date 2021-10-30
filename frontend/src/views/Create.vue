<template>
  <div class="create">
    <el-form :model="createForm" :rules="rules">
        <input @change="selectedFile" type="file" name="file">
        <el-form-item label="名前" prop="name">
            <el-input type="text" v-model="createForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="フリガナ" prop="furigana">
            <el-input type="text" v-model="createForm.furigana" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="誕生日" prop="birthday">
            <el-input type="date" v-model="createForm.birthday" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="趣味" prop="favorite">
            <el-input type="text" v-model="createForm.favorite" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="スキル" prop="skills">
            <el-input type="text" v-model="createForm.skills" autocomplete="off"></el-input>
        </el-form-item>
        <el-button type="primary" @click="create">作成</el-button>
    </el-form>
  </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
import "firebase/storage";
const axios = require('axios').create()
export default {
    name: 'home',
    data () {
        return {
            imgname: '',
            uploadFile: null,
            createForm: {
                name: '',
                furigana: '',
                birthday: '',
                favorite: '',
                skills: '',
            },
            rules: {
                name: [
                    { required: true, message: '名前を入力してください。' },
                    { max: 15, message: '15文字以内で入力してください。' }
                ],
                furigana: [
                    { required: true, message: 'フリガナを入力してください' },
                    { max: 30, message: '30文字以内で入力してください。' }
                ],
                favorite: [
                    { required: true, message: '趣味を入力してください。' },
                    { max: 50, message: '50文字以内で入力してください。' }
                ],
                skills: [
                    { required: true, message: 'スキルを入力してください。' },
                    { max: 50, message: '50文字以内で入力してください。' }
                ],
            },
        }
    },
    methods: {
        create() {
            // RESTAPI経由で開発用DBにテキストデータのみPOST
            let formData = new FormData();
            formData.append('imgname', this.imgname);
            formData.append('name', this.createForm.name);
            formData.append('furigana', this.createForm.furigana);
            formData.append('birthday', this.createForm.birthday);
            formData.append('favorite', this.createForm.favorite);
            formData.append('skills', this.createForm.skills);

            axios.post('/api/info', formData).then(function (response){
                console.log(response)
            })
            
            // Firebase上のストレージに保存
            const imgpath = 'images/' + this.imgname
            const storageRef = firebase.storage().ref(imgpath);
            storageRef.put(this.uploadFile).then(() => {
                console.log('uploaded ' + this.imgname)
            });

            this.$router.push({name: '/show'})
        },
        selectedFile: function(e) {
            e.preventDefault();
            this.uploadFile = e.target.files[0]
            this.imgname = e.target.files[0].name
            console.log(e.target.files[0])
            console.log(this.imgname)
        },
    }
}
</script>
