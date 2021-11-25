<template>
				<!-- vue JS + wechat-api + H5-CSS3 -->
		<view>
			<view class = "slogan">
				<image src="../../static/logo.png" mode="widthFix"></image>
			</view>
			<view class="cu-form-group">
				<view class="title"></view>
				<input type="text" placeholder="请输入昵称..."  name="userName" v-model="input_nickname"
				@input="userNameInput" confirm-type="done" confirm-hold="true"/>
			</view>
			<view class="cu-form-group">
				<view class="title"></view>
				<input type="text" placeholder="请输入密码..." name="passWord" v-model="input_password"
				confirm-type="done" confirm-hold="true" @input="userPasswordInput"></input> 
			</view>
			<view class="padding">
				<button @click="subBtn_login()" :disabled="hasPwd||hasName">
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>登录咻管家
				</button>
			</view>
			<view class="padding"><button @click="goToNextPage()"><text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>新用户注册</button></view>
		
		</view>
</template>
<script>
	export default{
		data(){
			return{
				//v-model绑定表单内的数据，用于刷新表单输入框
				input_nickname:'',
				input_password:'',
				//判定用户是否已经输入昵称和密码
				userPwdLen: '',
				hasPwd: true,
				userNameLen : '',
				hasName : true,
			    loadFlag : false,
				//获取用户的用户名和密码，并放置于本地缓存（后端比对）,
				//缓存的Key值是'username_log' 'password_log'
				username_log: '',
				password_log: '',
				//向后端传递的用户名和密码
				Uname:'',
				Upassword:'',
				//接收后端的数据
				Code:'',
				message:''
			}
		},
		onLoad(){
			//加载页面时调用，但在多个Tabbar中切换时，不会调用OnLoad()
		},
		onShow() {
			
		},
		onPullDownRefresh() {
			//JS 中定义匿名函数(箭头函数)类似于Java、c中的lambda表达式,无需完整格式定义函数
			setTimeout(()=>{
				this.loadFlag = true,
				this.hasName = true,
				this.hasPwd = true
				this.input_nickname = '';
				this.input_password = '';
				uni.stopPullDownRefresh()
			},300)
		},
		methods:{
			userNameInput(e){
				this.userNameLen = e.target.cursor;
				this.username_log = e.target.value;
				uni.setStorageSync('username_log',this.username_log);
				if(this.userNameLen > 0 && this.userNameLen < 16){
					this.hasName = false
				}else{
					this.hasName = true
				}
			},
			userPasswordInput(e){
				this.userPwdLen = e.target.cursor;
				this.password_log = e.target.value;
				uni.setStorageSync('password_log',this.password_log);
				if(this.userPwdLen >= 8 && this.userPwdLen <= 12){
					this.hasPwd = false;
				}
				else{
					this.hasPwd = true;
				}
			},
			subBtn_login(e){
				this.Uname = uni.getStorageSync('username_log')
				this.Upassword = uni.getStorageSync('password_log')
				uni.request({
					url: "http://47.113.196.102:5000/login",
					method:"POST",
					header: {
					  'content-type': 'application/x-www-form-urlencoded' //后端接收的是（表单）字符串类型，例如'id=1231454&sex=男'
					 },
					data:{username: this.Uname, password: this.Upassword},
					success: (res) => {	
						this.message = JSON.stringify(res.data.message)
						this.Code = JSON.stringify(res.data.status)
						if(this.Code == 200){
							uni.switchTab({
								url: "../search/search"
							})
						}
						if(this.Code == 400){
							uni.showToast({
									icon: "none",
									title: this.message
								});
							}
						}
					})
				},
				goToNextPage(){
						uni.navigateTo({
					            url: '../Register/Register',
								});
				}
			},
		}
	
</script>

<style lang="scss">
	page{
		width:100%;
		height: 100%;
		background-size: 100% 100%;
		// background-image: url(https://pica.zhimg.com/80/v2-8411510fe4d28ecf4c262e3b520bd6c7_720w.jpg?source=1940ef5c);
	}
	button{
		 font-size: 40rpx;
		 border-radius: 40rpx;
		 line-height: 80rpx;
		 width: 550rpx;
		 height: 80rpx;
		 font-weight: 700;
		 color: #FFFFFF;
		 background-color: #f27498;
		 // border-radius:  
	}
	.slogan{
		text-align: center;
	}
	.slogan image{
		width: 65%;
	}
	.cu-form-group{
		margin-bottom: 50rpx;
		color: #FFFFFF;
		overflow: hidden;
		text-align: center;
	}
	.title{
		color: #000000;
		margin-right: 20rpx;
		margin-left: 40rpx;
		float: left;
		font-size: 50rpx;
	}
	.padding{
		margin-bottom: 50rpx;
		text-align: center;
	}
	input{
		font-size: 35rpx;
		text-align: left;
		padding-left: 30rpx;
		border-radius: 40rpx;
		line-height: 80rpx;
		margin: 0 auto;
		border: 3rpx solid #f27498;
		width: 550rpx;
		height: 80rpx;
		color: #000000;
	}
</style>
