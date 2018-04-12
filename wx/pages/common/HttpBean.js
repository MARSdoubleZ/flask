export function httpGet(url, data, sucCallback, failCallback) {
  wx.request({
    url: 'http://localhost:5000' + url,
    method: 'GET',
    data: data,
    success: function (res) {
      sucCallback(res)
    },
    fail: function (res) {
      failCallback(res)
    }
  })
}

export function httpPost(url, data, sucCallback, failCallback) {
  wx.request({
    url: 'http://localhost:5000' + url,
    method: 'POST',
    data: data,
    header: { 'content-type': 'application/json' },
    success: function (res) {
      sucCallback(res)
    },
    fail: function (res) {
      failCallback(res);
    }
  })
}