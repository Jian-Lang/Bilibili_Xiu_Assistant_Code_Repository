<template>
	<view>
		<web-view :src="url"></web-view>
<!-- 		<view class="title">
			视频链接如下，请点击后跳转！
		</view>
		<view class="url">
			<text user-select="true">{{url}}</text>	
		</view> -->
	</view>
</template>

<script>
	export default{
		data(){
			return{
				url:''
			}
		},
		onLoad() {
			this.url = uni.getStorageSync("video_url");
			this.$forceUpdate()
		}
	}
</script>

<style>
		
	.title{
		font-size: 45rpx;
		/* margin: 0 auto; */
		margin-top: 30rpx;
		width: 100%;
		text-align: center;
	}
		
	.url{
		text-align: center;
		margin: 0 auto;
		margin-top: 30rpx;
		font-size: 25rpx;
	}
</style>