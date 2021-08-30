var app = new Vue({
    el:'#app',
    data:{
        city:'',
        weather:[],
    },
    methods:{
        // 点击搜索按钮，根据输入内容查询成功
        serch:function () {
            var that = this;
            axios.get('http://wthrcdn.etouch.cn/weather_mini?city='+this.city)
                .then(
                    function (response) {
                        that.weather = response.data.data.forecast;
                        console.log(that.weather)
                    },
                    function (err) {
                        alert(err);
                    }
                )
        },
        // 输入城市，敲击回车键搜索,因为调用同一个接口，因此函数直接通过this调用
        enterSerch:function () {
            this.serch()
        },
        // 点击输入框下方城市，直接展示在输入框内，并且搜索
        clickSerch:function (city) {
            this.city = city;
            this.serch()

        }
    }
})