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
    el:'#player',
    data:{
        // 搜索文案
        serchText:'',
        // 歌曲信息列表
        musicList:[],
        // 歌曲音频地址
        musicURL:'',
        // 歌曲评价列表
        musicCommentslist:[],
        // 歌曲封面地址
        musicAlbum:'',
        // 是否在播放
        isplay:false,
        // 视频播放地址
        videoURL:'',
        // 是否展示视频
        showVideo: false,
    },
    methods:{
        // 搜索歌曲
        serchMusic: function () {
            that = this;
            axios.get('https://autumnfish.cn/search?keywords='+ that.serchText)
                .then(
                    function (response) {
                        // console.log(response.data.result.songs);
                        that.musicList = response.data.result.songs
                    }
                )
        },
        // 点击播放音乐：获取音乐地址、封面地址、评论内容
        playMusic:function (musicID) {
            that = this;
            axios.get('https://autumnfish.cn/song/url?id='+ musicID )
                .then(
                    function (response) {
                        that.musicURL = response.data.data[0].url
                        // console.log(response.data.data[0].url)
                    }
                );
            axios.get("https://autumnfish.cn/comment/hot?type=0&id=" + musicID)
                .then(function (response) {
                    // console.log(response.data.hotComments);
                    that.musicCommentslist = response.data.hotComments;
                });
            axios.get("https://autumnfish.cn/song/detail?ids=" + musicID)
                .then(function (response) {
                    // console.log(response.data.songs[0].al.picUrl)
                    that.musicAlbum = response.data.songs[0].al.picUrl
                });
        },
        play:function () {
            this.isplay = true;
            console.log(this.isplay)
        },
        pause:function () {
            this.isplay = false;
            console.log(this.isplay)
        },
        // 播放视频
        playMV: function (MVId) {
            that = this;
            this.showVideo = true;
            axios.get('https://autumnfish.cn/mv/url?id=' + MVId)
                .then(function (response) {
                    that.videoURL = response.data.data.url;
                    console.log(response.data.data.url)
                })
        },
        closeMV:function () {
            this.showVideo = false;
        }

    }


})