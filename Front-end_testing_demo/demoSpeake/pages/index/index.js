//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    imageSrc:'../imgs/background.jpg',

    text1:'',
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  get1 : function(e){
    var that = this;
    wx.request({
      // url: "https://developers.weixin.qq.com/miniprogram/dev/component/view.html",
      success: function (res) {
        console.log(res.data),
        that.setData({ text1: res.data});
        wx.navigateTo({
          url: '../jieshao/jieshao',
          success: function(res) {},
          fail: function(res) {},
          complete: function(res) {},
        })
      }
    })
  
  },
  get2: function (e){
    wx.navigateTo({
      url: '../zujian/zujian',
      success: function(res) {},
      fail: function(res) {},
      complete: function(res) {},
    })
  },
  get3: function (e) {
    wx.navigateTo({
      url: '../api/api',
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    })
  },
  get4: function (e) {
    wx.navigateTo({
      url: '../houduan/houduan',
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    })
  }
})
