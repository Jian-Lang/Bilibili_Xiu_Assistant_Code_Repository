<template>
	<view>
		<view class="header">
			<view class="portrait">
				<image :src = "imgSrc" mode="widthFix"></image>
			</view>
			<view class="personalData">
				<view class="username">{{username}}</view>
				<view class="uid">uid: {{uid}}</view>
				<view class="sign" @click="goToEditor">个人介绍：{{sign}}</view>
			</view>
		</view>
		<view class="content">
			<view class="perData">
				<span class="icon-user icon" style="color:#3ebf91"></span>
				<span class="text">个人信息</span>
				<span class="icon-chevron-right icon_right"></span>
			</view>
			<view class="speBro">
				<span class="icon-list2 icon" style="color:#3bb5db"></span>
				<span class="text">特别关心推送</span>
				<span class="icon-chevron-right icon_right"></span>
			</view>
			<view class="speBroList">
				<span class="icon-heart icon" style="color: #f66041"></span>
				<span class="text">up主特别关心列表</span>
				<span class="icon-chevron-right icon_right"></span>
			</view>
			<view class="focBro">
				<span class="icon-star-full icon" style="color:#eda02a;"></span>
				<span class="text">up主关注列表</span>
				<span class="icon-chevron-right icon_right"></span>
			</view>
			
			<view class="setting">
				<span class="icon-cog icon" style="color: #4bc9ee;"></span>
				<span class="text">设置</span>
				<span class="icon-chevron-right icon_right"></span>
			</view>
			<!--字体图标技术 在线平台：阿里云、Iconmoon，-->
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				imgSrc:'http://47.113.196.102:8080/icon/' + uni.getStorageSync("username_log"),
				username:'无用户',
				uid:'',
				sign:'',
				iniSign:'',
			}
		},
		onLoad() {
			this.username = uni.getStorageSync("username_log"),
			uni.setStorageSync("sign",""),
			uni.request({
				url:'http://47.113.196.102:5000/getuser',
				method:'GET',	
				data:{username : this.username},
				header: {
				  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				 },
				 success: (res) => {
					this.uid = this.getContent(JSON.stringify(res.data.B_UID));
				 	this.sign = this.getContent(JSON.stringify(res.data.Sign));
					//this.sign = this.sign.substring(1,this.sign.length-1);
				 }
			})
			uni.loadFontFace({
			  family: 'Huawen',
			  source: 'url("http://47.113.196.102:8080/word/华文行楷.ttf")',
			  success() {
			      console.log('success')
			  }
			})
			
		},
		onShow() {
			if(uni.getStorageSync("sign") != ""){
				this.sign = uni.getStorageSync("sign")
			}
			// console.log(this.sign)
		},
		methods:{
			goToEditor(){
				uni.navigateTo({
					url: "../userSign/userSign"
				})
			},
			getContent(e){
				return e.substring(1,e.length-1);
			}
		}

	}
</script>

<style>
	page{
		display: flex;
		flex-direction: column;
		background-color: #ededed;
	}
	.header{
		display: flex;
		background-color: #FFFFFF;
		overflow: hidden;
		width: 100%;
		height: 340rpx;
		/* background-color: #4CD964 */
		margin-bottom: 20rpx;
	}
	.portrait{
		float: left;
		margin-left: 35rpx;
		margin-top: 55rpx;
		overflow: hidden;
		width: 160rpx;
		height: 160rpx;
	}
	.portrait image{
		width: 158rpx;
		height: 158rpx;
		border-radius: 50%;
	}
	.personalData{
		float: left;
		margin-top: 55rpx;
		height: 300rpx;
		width: 450rpx;
		margin-left: 40rpx;
		/* background-color: #000000; */
	}
	.username{
		font-style: normal;
		/* color: #FFFFFF; */
		font-size: 50rpx;
		font-weight: 700;
	}
	.uid,.sign{
		color: #737373;
		margin-top: 20rpx;
	}
	.sign {
		margin-top: 25rpx;
		font-family: 'Huawen';
		/* src: url("http://47.113.196.102:8080/word/华文行楷.ttf"); */
	}
	.speBro,.perData,.speBroList,.focBro,.setting {
		position: relative;
		height: 100rpx;
		display: flex;
		background-color: #FFFFFF;
		width: 100%;
	}
	.speBro{
		margin-top: 20rpx;
	}
	.icon,.icon_right{
		color: #a6abae;
		margin-left: 30rpx;
		margin-right: 35rpx;
		font-size: 45rpx;
		line-height: 100rpx;
	}
	.text{
		font-weight: 500;
		font-size: 40rpx;
		line-height: 100rpx;
	}
	.icon_right{
		position: absolute;
		right: 0rpx;
	}
</style>
