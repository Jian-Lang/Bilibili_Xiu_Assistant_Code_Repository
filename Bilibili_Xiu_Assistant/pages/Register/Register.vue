<template>
		<view>
			<view class = "slogan">
				<image :src="imgSrc" mode="widthFix" @click="uploadImg"></image>
			</view>
			<form>
				<view class="cu-form-group">
					<input type="text" placeholder="请输入15位以内的昵称..." name="userName" 
					@input="userNameInput" confirm-type="done" confirm-hold="true" v-model="inputName"></input>
				</view>
				<view class="cu-form-group">
					<input type="text" placeholder="请输入8-12位的密码..." name="passWord" 
					confirm-type="done" confirm-hold="true" @input="userPasswordInput" v-model="inputPwd"></input> 
				</view>
				<view class="cu-form-group">
					<input type="text" placeholder="请输入B站UID(不可换绑)..." name="UID" 
					@input="UIDInput" confirm-type="done" confirm-hold="true" v-model="inputUID"></input>
				</view>
			</form>
			<view class="padding">
				<button @click="subBtn_regis()" :disabled="hasPwd||hasName||hasUid||hasImg" form-type="submit">
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>确认注册
			   </button>
			</view>
			<view class="padding">
				<button @click="goToNextPage()">
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
				//头像上传参数
				imgSrc:'../../static/Protrait.png',
				hasImg: true
			}
		},
		onPullDownRefresh() {
			setTimeout(()=>{
				this.loadFlag = true
				this.hasName = true
				this.hasPwd = true
				this.hasUid = true
				this.hasImg = true
				this.inputName = '';
				this.inputPwd = '';
				this.inputUID = '';
				this.imgSrc = '../../static/Protrait.png';
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
				if(this.userNameLen > 0 && this.userNameLen < 16){
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
				if(this.userPwdLen >= 8 && this.userPwdLen <= 12){
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
				if(this.UidLen > 0 && this.UidLen < 21){
					this.hasUid = false;
				}
				else{
					this.hasUid = true;
				}
			},
			subBtn_regis(e){
				this.Uname = uni.getStorageSync('username_res'),
				this.Upassword = uni.getStorageSync('password_res'),
				this.Uuid = uni.getStorageSync('uid_res')
				setTimeout(()=>{
					uni.request({
						url:'https://www.zhangwenning.top:5000/register',
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
								this.hasImg = true
								uni.uploadFile({
								    url: 'https://www.zhangwenning.top:5000/uploadpic', //仅为示例，非真实的接口地址
								    filePath: this.imgSrc,
								    name: 'icon',
									formData: {
									 'username': this.Uname		
									            },
								});
								this.imgSrc = '../../static/Protrait.png',
								uni.showToast({
									title: "注册成功!"
								})
							}
							if(this.Code == 400){
								uni.showToast({
									icon: "none",
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
			uploadImg(){
				uni.chooseImage({
					count: 1,
					success: (res) => {
						const tempFilePaths = res.tempFilePaths;
						this.imgSrc = tempFilePaths[0];
						this.hasImg = false
					}
				})
			}
		}
	}
</script>

<style lang="scss">
	page{
		width:100%;
		height: 100%;
	}
	.slogan{
		text-align: center;
		overflow: hidden;
		margin: 0 auto;
		margin-top: 10%;
		margin-bottom: 8%;
	}
	.slogan image{
		// width: 145px;
		// height: 145px;
		width: 44%;
		border-radius: 50%;
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
</style>