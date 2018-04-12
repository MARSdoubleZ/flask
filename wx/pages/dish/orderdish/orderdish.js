// pages/dish/orderdish/orderdish.js
import { httpGet } from '../../common/HttpBean.js'
let thisa;
Component({
  created() {
    thisa = this;
  },
  /**
   * 组件的属性列表
   */
  properties: {
    title: {            // 属性名
      type: String,     // 类型（必填），目前接受的类型包括：String, Number, Boolean, Object, Array, null（表示任意类型）
      value: '标题'     // 属性初始值（可选），如果未指定则会根据类型选择一个
    },
  },
  /**
   * 组件的初始数据
   */
  data: {
    shopname: '',
    navLeftItems: [],
    curNav: '',
    dishs: null,
    dishnum: {},
  },
  /**
   * 组件的方法列表
   */
  methods: {
    init: function (flowid) {
      thisa = this;
      // console.log('flowid:'+flowid);
      let url = '/wxenterRRt';
      let data = { flowid: flowid };
      function sucFun(res) {
        let data = res.data;
        let json = JSON.parse(data);
        let dishSorts = JSON.parse(json[1]);
        let dishs = JSON.parse(json[2]);
        // console.log(dishs);
        thisa.setData({
          shopname: json[0],
          navLeftItems: dishSorts,
          curNav: dishSorts[0]._id['$oid'],
          dishs: dishs,
        });
      }
      function failFun(res) {
        console.log('err:' + ':' + res);
      }
      httpGet(url, data, sucFun, failFun);
    },
    switchRightTab: function (e) {
      // 获取item项的id，和数组的下标值  
      let sortid = e.target.dataset.id;
      console.log(sortid)
      let url = '/getdishBySortid';
      let data = {sortid: sortid};
      function sucFun(res) {
        let data = res.data;
        let dishs = JSON.parse(data);
        console.log(dishs)
        dishs = JSON.parse(dishs);
        console.log(dishs)
        thisa.setData({
          dishs: dishs,
        });

      }
      function failFun(res) {
        console.log('err:' + ':' + res);
      }
      httpGet(url, data, sucFun, failFun);
      
    },
    addDish: function (e) {
      // console.log(e.currentTarget.id);
      console.log(e.currentTarget.dataset.dname);
      let target = e.currentTarget;
      let dishid = target.id;
      let dname = target.dataset.dname;
      let price = target.dataset.price;
      let dishnum = thisa.data.dishnum;
      if (typeof (dishnum[dishid]) == 'undefined') {
        dishnum[dishid] = 1;
      } else {
        dishnum[dishid] += 1;
      }
      let jsonStr = wx.getStorageSync('shoppingcar');
      let json = JSON.parse(jsonStr);

      json[dishid] = [dname,price,dishnum[dishid]];
      wx.setStorageSync('shoppingcar', JSON.stringify(json));
      thisa.setData({
        dishnum: dishnum
      })
      // console.log(wx.getStorageSync('shoppingcar'));
    },
    lessDish: function (e) {
      let target = e.currentTarget;
      let dishid = e.currentTarget.id;
      let dname = target.dataset.dname;
      let price = target.dataset.price;
      let dishnum = thisa.data.dishnum;
      let jsonStr = wx.getStorageSync('shoppingcar');
      let json = JSON.parse(jsonStr);
      if (typeof (dishnum[dishid]) != 'undefined') {
        if (dishnum[dishid] > 0) {
          dishnum[dishid] -= 1;
          json[dishid] = [dname, price, dishnum[dishid]];
          if (dishnum[dishid] == 0) {
            delete json[dishid];
          }
          wx.setStorageSync('shoppingcar', JSON.stringify(json));
          thisa.setData({
            dishnum: dishnum
          })
        }
      }
      console.log(wx.getStorageSync('shoppingcar'));
    }
  }
})
