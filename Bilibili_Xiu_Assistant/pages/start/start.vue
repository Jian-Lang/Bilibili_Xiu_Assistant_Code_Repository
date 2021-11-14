<template>
	<view>
		<view class="img-f">
			<image src="../../static/logo.png" mode="widthFix"></image>
		</view>
		<view class="slogan1">咻一下</view>
		<view class="slogan2">随时随地得到最新推送</view>
		<view class="btn-f">
			<button size="mini" plain="true" class="btn" @tap="goToNextPage()"><text>登录进入</text></button>
		</view>
		
	</view>
</template>

<script>
	export default{
		methods: {
			goToNextPage(){
				uni.navigateTo({
			                url: '../login/login',
			            });
		}
	}
	}
</script>

<style>
	page{
		background-color: #000;
	}
	.img-f{
		margin-top: 50rpx;
		text-align: center;
	}
	image {
	   width: 65%;
	   margin: auto;
	}
	.slogan1{
		margin-top: -20rpx;
		color: #FFFFFF;
		font-size: 32px;
		text-align: center;
	}
	.slogan2{
		margin-top: 30rpx;
		color: #FFFFFF;
		font-size: 16px;
		text-align: center;
	}
	.btn-f{
		margin-top: 100rpx;
		text-align: center;
	}
	text{
		font-size: 14px;
		color: #FFFFFF
	}
</style>
