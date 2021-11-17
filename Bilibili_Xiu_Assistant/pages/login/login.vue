<template>
		<view>
			<view class = "slogan">
				<image src="../../static/logo.png" mode="widthFix"></image>
			</view>
			<view class="cu-form-group">
				<view class="title">昵称:</view>
				<input type="text" placeholder="请输入文明昵称..." name="userName" v-model="user_nickname"
				@input="userNameInput" confirm-type="done" confirm-hold="true" placeholder-style="color:#000000"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">密码:</view>
				<input type="text" placeholder="请输入密码..." name="passWord" v-model="user_password"
				confirm-type="done" confirm-hold="true" @input="userPasswordInput" placeholder-style="color:#000000"></input> 
			</view>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" @click="subBtn_login()" :disabled="hasPwd||isAble" size="mini" >
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>登录咻管家
				</button>
			</view>
			<view class="padding"><button class="cu-btn block bg-blue margin-tb-sm lg" size="mini" @click="goToNextPage()"><text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>新用户注册</button></view>
		
		</view>
</template>

<script>
	import BackgroundImage from "@/static/pic1.jpg"
	export default{
		data(){
			return{
				// userPwdInp:  '',
				user_nickname:'',
				user_password:'',
				UidLen:'',
				hasUid: true,
				userPwdLen: '',
				hasPwd: true,
				userNameInp : '',
				userNameLen : '',
				loadFlag : false,
				isAble : true,
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
				this.isAble = true,
				this.hasPwd = true
				this.user_nickname = '';
				this.user_password = '';
				uni.stopPullDownRefresh()
			},300)
		},
		methods:{
			userNameInput(e){
				this.userNameInp = e.target.value;
				this.userNameLen = e.target.cursor;
				if(this.userNameLen > 0){
					this.isAble = false
				}else{
					this.isAble = true
				}
			},
			userPasswordInput(e){
				// this.userPwdInp = e.target.value;
				this.userPwdLen = e.target.cursor;
				if(this.userPwdLen > 0){
					this.hasPwd = false;
				}
				else{
					this.hasPwd = true;
				}
			},
			UIDInput(e){
				// this.userPwdInp = e.target.value;
				this.UidLen = e.target.cursor;
				if(this.UidLen > 0){
					this.hasUid = false;
				}
				else{
					this.hasUid = true;
				}
			},
			subBtn_login(e){
				this.loadFlag = true,
				this.isAble = true,
				this.hasPwd = true
				setTimeout(function(){
					uni.showToast({
						title: "登录成功!"
					});
					this.loadFlag = true
					this.isAble = true
					this.hasPwd = true
				},500)
			},
			goToNextPage(){
				uni.navigateTo({
			            url: '../Register/Register',
						});
		}
		}
	}
</script>

<style lang="scss">
	page{
		width:100%;
		height: 100%;
		background-size: 100% 100%;
		background-image: url(https://pica.zhimg.com/80/v2-8411510fe4d28ecf4c262e3b520bd6c7_720w.jpg?source=1940ef5c);
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
		margin-bottom: 30rpx;
		text-align: center;
	}
	input{
		width: 550rpx;
		height: 70rpx;
		align-items: center;
		color: #000000;
		border-color: #000000;
	}
</style>
