// pages/bind/bind.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
     message:"数据绑定",
     name:"",
     dataList:["aa","bb","cc"],
     imageList:["/static/pic/R-C.JPG","/static/pic/R-C.JPG"]
  },
  changeData:function(){
    this.setData({
      message:"修改后的数据"
    })
  },
  getUserName:function(){
    var that = this;
    wx.getUserInfo({
       success:function(res){
         console.log("sdsd",res);
          that.setData({
             name:res.userInfo.nickName
          })
       },
       fail:function(res){
          console.log("失败",res);
       }
    })
  } , 
  bindGetUserInfo:function(){
      wx.openSetting({});
      console.log("aaaa");
      var that = this;
      wx.getUserInfo({
         success:function(res){
           console.log("sdsd",res);
            that.setData({
               name:res.userInfo.nickName
            })
         },
         fail:function(res){
            console.log("失败",res);
         }
      })
    },
    getUserLocal:function(){
       console.log("aaaa-----");
       wx.chooseLocation({
         success:function(res){
           console.log("sss",res);
         },
       })
    },
    uploadImage:function(){
         console.log("上传图片----");
         var that = this;
         wx.chooseMedia({
          count:9,
          mediaType:['image', 'video'],
          sourceType:['album', 'camera'],
          success:function(res){
            let  {tempFiles}  = res;
            console.log(tempFiles);
            var arr = []
             tempFiles.forEach(
              e=>{arr.push(e.tempFilePath)}
            )
            that.setData({
              imageList:arr
            })
            console.log("gggg");
          }
         })
    },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})