// pages/apijieshao/apijieshao.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {

    id: Number

  },

  // 测试wx.request
  apiButton: function (res) {
    wx.request({
      url: 'https://api.douban.com/v2/movie/in_theaters', //仅为示例，并非真实的接口地址
      // 设置请求为ＧＥＴ方式，既显示传参，还有ＰＯＳＴ方式，一般是表单隐式传参
      method: 'GET',// OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT
      // 可用于设置请求参数，例如使用搜索功能时带参数请求后台
      // 也可以使用拼接url地址
      // 该请求的地址完整为：url?x=我是X&y=我是Y
      data: {
        movies: '后来的我们',
        // y: '我是Y'
      },
      header: {
        "Content-Type": "application/json"
      },
      success: function (res) {
        console.log(res.data)
        var list = res.data.list;
        if (list == null) {
          var toastText = '数据获取失败';
          wx.showToast({
            title: toastText,
            icon: '',
            duration: 2000
          });
        } else {
          that.setData({
            list: list
          })
        }
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      id: options.id
    })
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