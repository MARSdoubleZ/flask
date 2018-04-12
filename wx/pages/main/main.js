// pages/main/main.js
var thisa = null;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    navbar: ['餐饮', '体育', '户外'],
    currentTab: 0,
    mapHeight: "350px",
    longitude: 116.14294,
    latitude: 39.74788,
    maphideflag: true,
    linkaTxt: '显示地图'
  },
  navbarTap: function (e) {
    this.setData({
      currentTab: e.currentTarget.dataset.idx
    })
  },
  init: function () {
    wx.getSystemInfo({
      success: function (res) {
        console.log(res);
        // 可使用窗口宽度、高度
        // console.log('height=' + res.windowHeight);
        // console.log('width=' + res.windowWidth);
        // 计算主体部分高度,单位为px
        thisa.setData({
          // second部分高度 = 利用窗口可使用高度 - first部分高度（这里的高度单位为px，所有利用比例将300rpx转换为px）
          mapHeight: res.windowHeight - 192 + 'px'
        })
      }
    });
  },
  setMapCenter: function () {
    wx.getLocation({
      type: 'gcj02',
      success: function (res) {
        // console.log(res);
        thisa.setData({
          longitude: res.longitude,
          latitude: res.latitude
        });
        // callback(res);
      },
    });
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    thisa = this;
    thisa.init();
    // thisa.setMapCenter();
  },
  enterRestaurant: function (e) {
    let restaurantCode = e.detail.value.restaurantCode;
    wx.navigateTo({
      url: '../dish/dish?restaurantCode=' + restaurantCode,
    });
  },
  showmap: function () {
    if (thisa.data.linkaTxt == '显示地图') {
      thisa.setData({
        maphideflag: false,
        linkaTxt: '收起地图'
      });
    } else {
      thisa.setData({
        maphideflag: true,
        linkaTxt: '显示地图',
      });
    }

  },
  showLogin: function (e) {

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