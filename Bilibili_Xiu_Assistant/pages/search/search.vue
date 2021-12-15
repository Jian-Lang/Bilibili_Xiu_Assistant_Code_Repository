<template>
	<view>
		<view class="logo">
			<image src="../../static/logo.png" mode="aspectFill"></image>
		</view>
		<view class="searchInput">
			<input type="text" placeholder="咻一下,发现有趣的up主!" v-model="upName"/>
		</view>
		<view class="searchbtn" @click="search">
			咻一下             <span class="icon-search"></span>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				upName:"",
			}
		},
		onLoad() {
				uni.setStorageSync("up_name","")
		},
		onShow() {
			uni.setStorageSync("up_name",""),
				this.upName = uni.getStorageSync("up_name")
		},
		methods:{
			search(){
				if(this.upName == ""){
					uni.showToast({
						icon: "none",
						title: "请输入内容后搜索"
					})
				}
				else{
					uni.setStorageSync("up_name",this.upName),
					uni.navigateTo({
						url: "../searchResults/searchResults"
					})
				}
			}
		}
	}
</script>

<style>
	page{
		display: flex;
		flex-direction: column;
	}
	.logo{
		position: relative;
		margin-top: 35rpx;
		
		text-align: center;
		margin-bottom: -5rpx;
	}
	.logo image{
		width: 65%;
	}
	.searchInput{
		width: 100%;
	}
	input{
		text-align: center;
		margin: 0 auto;
		border-radius: 10rpx;
		border: 2rpx solid #000000;
		width: 95%;
		height: 70rpx;
	}
	.searchbtn{
		border-radius: 10rpx;
		background-color: #f27498;
		font-size: 33rpx;
		line-height: 65rpx;
		text-align: center;
		margin: 0 auto;
		margin-top: 60rpx;
		width: 35%;
		height: 65rpx;
		color: #FFFFFF;
	}
	.icon-search{
		margin-left: 5rpx;
	}
</style>
