// pages/dish/dish.js
let thisa;
let od;
Page({
  /**
   * 页面的初始数据
   */
  data: {
    shopname: '',
    navbar: ['点菜', '购物车', '评论'],
    currentTab: 0,
    buycarShow: true,
    goodsList:{}
  },

  initShoppingCar() {
    wx.setStorageSync('shoppingcar', '{}');
    // console.log(wx.getStorageSync('shoppingcar'));
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    thisa = this;
    let flowid = options.restaurantCode;
    od = this.selectComponent("#od");
    od.init(flowid);
    thisa.initShoppingCar();
  },
  navbarTap: function (e) {
    // let od = this.selectComponent("#od");
    // od.fun1();
    this.setData({
      currentTab: e.currentTarget.dataset.idx
    })
  },
  showBuyCar: function (e) {
    console.log(wx.getStorageSync('shoppingcar'))
    let str = wx.getStorageSync('shoppingcar')
    let json = JSON.parse(str)
    thisa.setData({
      buycarShow: false,
      goodsList:json
    });
  },
  hidBuyCar: function (e) {
    thisa.setData({
      buycarShow: true
    });
  },
  dian: function (e) {

  },
  addInCar: function (e) {
    let target = e.currentTarget;
    let dishid = target.id;
    let dishnum = od.data.dishnum;
    dishnum[dishid]+=1;
    od.setData({
      dishnum: dishnum
    });
    let jsonStr = wx.getStorageSync('shoppingcar');
    let json = JSON.parse(jsonStr);
    console.log(json)
  
    // console.log(json[dishid])
    json[dishid][2] += 1;
    // console.log(json);
    wx.setStorageSync('shoppingcar', JSON.stringify(json));
    thisa.showBuyCar();
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
