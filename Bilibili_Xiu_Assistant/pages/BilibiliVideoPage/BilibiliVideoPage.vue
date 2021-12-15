<template>
	<view>
		<web-view :src="url"></web-view>
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
</style>
