import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import firebase from 'firebase'
// import css from './assets/css/style.css'

Vue.config.productionTip = false

const config = {
  apiKey: "AIzaSyA1ftgElpwTJ3kltF4DrYyTwP96bXYwF0Q",
  authDomain: "isdl-kangaroo-48f90.firebaseapp.com",
  projectId: "isdl-kangaroo-48f90",
  storageBucket: "isdl-kangaroo-48f90.appspot.com",
  messagingSenderId: "364622417468",
  appId: "1:364622417468:web:ab92d9ecb5f503a51b7d39"
}

// console.log(config);
firebase.initializeApp(config);

new Vue({
  router,
  store,
  // css,
  render: h => h(App)
}).$mount('#app')
