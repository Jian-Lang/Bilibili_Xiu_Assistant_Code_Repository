<template>
		<view>
			<view class = "slogan">
				<image src="../../static/logo_sm.png"></image>
			</view>
			<view class="cu-form-group">
				<view class="title">昵称</view>
				<input type="text" placeholder="请输入文明昵称..." name="userName" 
				@input="userNameInput" 
				confirm-type="done" confirm-hold="true"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">密码</view>
				<input type="text" placeholder="请输入密码..." name="passWord" 
				confirm-type="done" confirm-hold="true" @input="userPasswordInput"></input> 
			</view>
			<view class="cu-form-group">
				<view class="title">puid</view>
				<input type="text" placeholder="请输入UID..." name="UID" 
				@input="UIDInput" 
				confirm-type="done" confirm-hold="true"></input>
			</view>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" @click="subBtn_login()" :disabled="hasPwd||isAble" size="mini" >
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>登录咻管家
				</button>
			</view>
			<view class="padding"><button class="cu-btn block bg-blue margin-tb-sm lg" size="mini" @click="subBtn_regis()"   :disabled="hasPwd||isAble"><text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>新用户注册</button></view>
		
		</view>
</template>

<script>
	import BackgroundImage from "@/static/pic1.jpg"
	export default{
		data(){
			return{
				// userPwdInp:  '',
				BackgroundImage:BackgroundImage,
				userPwdLen: '',
				hasPwd: true,
				userNameInp : '',
				userNameLen : '',
				loadFlag : false,
				isAble : true,
			}
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
			subBtn_login(e){
				this.loadFlag = true,
				this.isAble = true,
				this.hasPwd = true
				var $this = this;
				setTimeout(function(){
					uni.showToast({
						title: "登录成功!"
					});
					$this.loadFlag = false
					$this.isAble = false
					$this.hasPwd = false
				},500)
			},
			subBtn_regis(e){
				this.loadFlag = true,
				this.isAble = true,
				this.hasPwd = true
				var $this = this;
				setTimeout(function(){
					uni.showToast({
						title: "注册成功!"
					});
					$this.loadFlag = false
					$this.isAble = false
					$this.hasPwd = false
				},500)
			}
		}
	}
</script>

<style lang="scss">
	page{
		width:100%;
		height: 100%;
		background-size: 100% 100%;
		background-image: url(https://pica.zhimg.com/80/v2-c6a4b8d39ce57889d166db005cafaae7_1440w.jpg?source=1940ef5c);
	}
	.slogan image{
		size: 50%;
	}
	.cu-form-group{
		margin-bottom: 50rpx;
		color: #FFFFFF;
		overflow: hidden;
		text-align: center;
	}
	.title{
		margin-right: 20rpx;
		margin-left: 35rpx;
		float: left;
		font-size: 50rpx;
	}
	.padding{
		text-align: center;
	}
	input{
		width: 550rpx;
		height: 70rpx;
		align-items: center;
		color: #000000;
		background-color: #FFFFFF;
	}
</style>
