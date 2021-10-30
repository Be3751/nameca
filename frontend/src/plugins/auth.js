export function upload (file, serviceID) {
    const imageURL = `tmp/${serviceID}`
    return  firebase.storage().ref().child(imageURL).put(file,
      function(error) {
        if (error) {
          // The write failed...
          alert('画像のアップロードに失敗しました');
          console.log(error);
        } else {
          console.log("Image file saved successfully!")
        }
      })
}

export function download (title) {
    const imageURL = `tmp/${title}`
    return firebase.storage().ref().child(imageURL).getDownloadURL(
      function(error) {
        if (!error) {
          alert('画像のダウンロードに失敗しました');
          console.log(error)
        } else {
          console.log("Download URL successfully!")
        }
      }
    )
  }