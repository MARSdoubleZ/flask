// pages/users/login/login.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  onlogin: function (e) {
    console.log(e.detail.value.email);
    wx.request({
      url: 'http://localhost:5000/wxuser', //接口地址
      // method: 'GET',
      method: 'POST',
      data: {
        email: e.detail.value.email,
        pwd: e.detail.value.pwd
      },
      // header: { 'content-type': 'application/json' },
      success: function (res) {
        console.log(res.data);

      },
      fail: function (res) {
        console.log('cuowu' + ':' + res)
      }
    })
  },

  cancel: function (e) {
    wx.navigateBack()
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
