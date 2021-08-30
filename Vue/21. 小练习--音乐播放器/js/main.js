/*
  1:歌曲搜索接口
    请求地址:https://autumnfish.cn/search
    请求方法:get
    请求参数:keywords(查询关键字)
    响应内容:歌曲搜索结果

  2:歌曲url获取接口
    请求地址:https://autumnfish.cn/song/url
    请求方法:get
    请求参数:id(歌曲id)
    响应内容:歌曲url地址
  3.歌曲详情获取
    请求地址:https://autumnfish.cn/song/detail
    请求方法:get
    请求参数:ids(歌曲id)
    响应内容:歌曲详情(包括封面信息)
  4.热门评论获取
    请求地址:https://autumnfish.cn/comment/hot?type=0
    请求方法:get
    请求参数:id(歌曲id,地址中的type固定为0)
    响应内容:歌曲的热门评论
  5.mv地址获取
    请求地址:https://autumnfish.cn/mv/url
    请求方法:get
    请求参数:id(mvid,为0表示没有mv)
    响应内容:mv的地址
*/
var app = new Vue({
  el: '#player',
  data:{
    serchText:'',
    musicList: [],
    musicUrl:'',
    musicCover:'',
    hotComments:'',
    isPlaying: false,
    MVUrl:'',
    isShow:false,

  },
  methods:{
    // 回车搜索
    serchSong:function () {
      var that = this;
      axios.get('https://autumnfish.cn/search?keywords='+ that.serchText)
          .then(function (response) {
              that.musicList = response.data.result.songs;
              console.log(that.musicList)
          },
          function (err) {
              alert(err)
          });
    },
    // 搜索歌曲源URL
    playMusic:function (musicID) {
      var that = this;
      axios.get('https://autumnfish.cn/song/url?id=' + musicID)
          .then(
              function (response) {
                that.musicUrl = response.data.data[0].url;
                console.log('https://autumnfish.cn/song/url?id=' + musicID);
                console.log(that.musicUrl)
              }
          );
      // 搜索歌曲封面
      axios.get('https://autumnfish.cn/song/detail?ids=' + musicID )
          .then(
              function (response) {
                that.data = response.data.songs[0].al.picUrl;
                // console.log(response.data.songs[0].al.picUrl);
                that.musicCover = that.data;
              }
          );
      // 搜索歌曲评论
      axios.get("https://autumnfish.cn/comment/hot?type=0&id=" + musicID)
          .then(
              function (response) {
                  that.hotComments = response.data.hotComments,
                  console.log(that.hotComments)
              }
          )

    },
    // 歌曲播放
    play: function() {
      // console.log("play");
      this.isPlaying = true;
    },
    // 歌曲暂停
    pause: function() {
      // console.log("pause");
      this.isPlaying = false;
    },
    // 播放MV、
    playMV: function (mvID) {
      var that = this;
      axios.get('https://autumnfish.cn/mv/url?id=' + mvID )
          .then(function (response) {
              console.log(response.data.data.url);
              that.MVUrl = response.data.data.url;
              that.isShow = true;
          })
    },

    // 隐藏
    hide: function() {
      this.isShow = false;
    }

  }

    }




)