<template>
		<view>
			<view class = "slogan">
				<image src="../../static/Protrait.png" mode="widthFix"></image>
			</view>
			<form>
				<view class="cu-form-group">
					<view class="title">昵称:</view>
					<input type="text" placeholder="请输入文明昵称..." name="userName" 
					@input="userNameInput" confirm-type="done" confirm-hold="true" placeholder-style="color:#000000" v-model="inputName"></input>
				</view>
				<view class="cu-form-group">
					<view class="title">密码:</view>
					<input type="text" placeholder="请输入密码..." name="passWord" 
					confirm-type="done" confirm-hold="true" @input="userPasswordInput" placeholder-style="color:#000000" v-model="inputPwd"></input> 
				</view>
				<view class="cu-form-group">
					<view class="title">Uid:</view>
					<input type="text" placeholder="请输入B站Uid..." name="UID" 
					@input="UIDInput" confirm-type="done" confirm-hold="true" placeholder-style="color:#000000" v-model="inputUID"></input>
				</view>
			</form>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" size="mini" @click="subBtn_regis()" :disabled="hasPwd||isAble||hasUid" form-type="submit">
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>确认注册
			   </button>
			</view>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" @click="goToNextPage()"  size="mini" >
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>返回登录
				</button>
			</view>
		</view>
</template>

<script>
	export default{
		data(){
			return{
				// userPwdInp:  '',
				inputPwd:'',
				inputUID:'',
				inputName:'',
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
			//加载生命周期
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
			subBtn_regis(e){
				this.inputPwd = '',
				this.inputUID = '',
				this.inputName = '',
				this.loadFlag = true,
				this.isAble = true,
				this.hasPwd = true,
				this.hasUid = true
				var $this = this;
				setTimeout(function(){
					uni.showToast({
						title: "注册成功!"
					});
					$this.loadFlag = false
					$this.isAble = false
					$this.hasPwd = false
					$this.hasUid = false
				},500)
			},
			goToNextPage(){
				uni.navigateTo({
					url:'../login/login'
				})
		},
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
