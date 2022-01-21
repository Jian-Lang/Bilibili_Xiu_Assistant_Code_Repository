<template>
	<view>
		<view class="setting" @click="goToSettingDays">
			<span class="text">获取更新天数设置</span>
			<span class="icon-chevron-right icon_right"></span>
		</view>
		<view class="setting">
			<span class="text">其他设置1</span>
			<span class="icon-chevron-right icon_right"></span>
		</view>
		<view class="setting">
			<span class="text">其他设置2</span>
			<span class="icon-chevron-right icon_right"></span>
		</view>
		<view class="logout" @click="Logout">
			退出登录
		</view>
	</view>

</template>

<script>
	export default{
		methods:{
			goToSettingDays(){
				uni.navigateTo({
					url:"../RefreshDaySetting/RefreshDaySetting"
				})
			},
			Logout(){
				uni.navigateTo({
					url:"../start/start"
				})
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
	.setting,.logout{
		font-weight: 500;
		font-size: 40rpx;
		line-height: 100rpx;
		position: relative;
		height: 100rpx;
		background-color: #FFFFFF;
		width: 100%;
	}
	.icon_right{
		color: #a6abae;
		margin-left: 30rpx;
		margin-right: 35rpx;
		font-size: 45rpx;
		line-height: 100rpx;
		position: absolute;
		right: 0rpx;
	}
	.text{
		margin-left: 16rpx;
	}
	.logout{
		margin-top: 20rpx;
		text-align: center;
	}
</style>
