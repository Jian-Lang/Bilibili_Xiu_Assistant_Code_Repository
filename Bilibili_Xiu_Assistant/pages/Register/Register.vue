<template>
		<view>
			<view class = "slogan">
				<image src="../../static/Protrait.png" mode="widthFix"></image>
			</view>
			<form>
				<view class="cu-form-group">
					<view class="title">昵称:</view>
					<input type="text" placeholder="请输入16位以内的昵称..." name="userName" 
					@input="userNameInput" confirm-type="done" confirm-hold="true" placeholder-style="color:#000000" v-model="inputName"></input>
				</view>
				<view class="cu-form-group">
					<view class="title">密码:</view>
					<input type="text" placeholder="请输入8-12位的密码..." name="passWord" 
					confirm-type="done" confirm-hold="true" @input="userPasswordInput" placeholder-style="color:#000000" v-model="inputPwd"></input> 
				</view>
				<view class="cu-form-group">
					<view class="title">Uid:</view>
					<input type="text" placeholder="请输入B站Uid..." name="UID" 
					@input="UIDInput" confirm-type="done" confirm-hold="true" placeholder-style="color:#000000" v-model="inputUID"></input>
				</view>
			</form>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" size="mini" @click="subBtn_regis()" :disabled="hasPwd||hasName||hasUid" form-type="submit">
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
				//绑定表单内的数据，用于刷新表单输入框
				inputPwd:'',
				inputUID:'',
				inputName:'',
				//判定用户是否已经输入昵称、密码和UID
				UidLen:'',
				hasUid: true,
				userPwdLen: '',
				hasPwd: true,
				userNameLen : '',	
				hasName : true,
				loadFlag : false,
				//获取用户的账号、密码和UID信息，并传给后端
				username_res: '',
				password_res: '',
				uid_res: '',
				//向后端传递的用户名和密码
				Uname:'',
				Upassword:'',
				Uuid: '',
				//从后端获取的数据
				message:'',
				Code:'',
			}
		},
		onPullDownRefresh() {
			setTimeout(()=>{
				this.loadFlag = true
				this.hasName = true
				this.hasPwd = true
				this.hasUid = true
				this.inputName = '';
				this.inputPwd = '';
				this.inputUID = '';
				uni.stopPullDownRefresh()
			},300)
		},
		onLoad(){
			//加载生命周期
		},
		methods:{
			userNameInput(e){
				this.userNameLen = e.target.cursor;
				this.username_res = e.target.value;
				uni.setStorageSync('username_res',this.username_res);
				if(this.userNameLen > 0){
					this.hasName = false
				}else{
					this.hasName = true
				}
			},
			userPasswordInput(e){
				// this.userPwdInp = e.target.value;
				this.userPwdLen = e.target.cursor;
				this.password_res = e.target.value;
				uni.setStorageSync('password_res',this.password_res);
				if(this.userPwdLen >= 8){
					this.hasPwd = false;
				}
				else{
					this.hasPwd = true;
				}
			},
			UIDInput(e){
				// this.userPwdInp = e.target.value;
				this.UidLen = e.target.cursor;
				this.uid_res = e.target.value;
				uni.setStorageSync('uid_res',this.uid_res);
				if(this.UidLen > 0){
					this.hasUid = false;
				}
				else{
					this.hasUid = true;
				}
			},
			subBtn_regis(e){
				this.Uname = uni.getStorageSync('username_res'),
				this.Upassword = uni.getStorageSync('password_res'),
				this.Uuid = uni.getStorageSync('uid_res'),
				setTimeout(()=>{
					uni.request({
						url:'http://47.113.196.102:5000/register',
						method:'POST',	
						data:{username : this.Uname, password : this.Upassword, B_UID : this.Uuid},
						header: {
						  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
						 },

						success: (res) => {
							this.Code = JSON.stringify(res.data.status)
							if(this.Code == 200){
								this.inputPwd = '',
								this.inputUID = '',
								this.inputName = '',
								this.loadFlag = true,
								this.hasName = true,
								this.hasPwd = true,
								this.hasUid = true,
								uni.showToast({
									title: "注册成功!"
								});
							}
							if(this.Code == 400){
								uni.showToast({
									title: JSON.stringify(res.data.message)
								})
							}
						}
					})
				},1000)
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