<template>
	<view>
		<view :class="currentContentClass" v-for="(item,index) in videoList" :key="index">
				<view :class="currentUpperClass">
						<view :class="currentIconClass">
							<image :class = "currentImgClass" :src= "item.up_face"  mode="widthFix"></image>
						</view>
						<view :class="currentNickClass">
							{{item.up_name}}<br>
							<text class="time">{{item.update_time}} 投稿了视频</text>
						</view>
						<view class="clear"></view>
				</view>
				<view :class="currentVideoClass" :src = "item.url">
					<image @click="goToVideo(item.url)" :class = "currentVideoImgClass" :src= "item.video_pic" mode="widthFix"></image>
				</view>
				<view :class="currentVideoTitle">
					{{item.video_title}}
				</view>
		</view>
	</view>

</template>

<script>
	export default{
		data(){
			return{
				username:'none',
				currentContentClass:'none',
				currentUpperClass:'none',
				currentIconClass:'none',
				currentImgClass:'none',
				currentNickClass:'none',
				time:'none',
				currentVideoClass:'none',
				currentVideoImgClass:'none',
				currentVideoTitle:'none',
				videoList: []
			}
		},
		onLoad() {
			this.username = uni.getStorageSync("username_log"),
			uni.request({
				url:'https://www.zhangwenning.top:5000/getbvideo',
				method:'GET',	
				data:{username : this.username},
				header: {
				  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				 },
				 success: (res) => {
					if(res.data.status == "200"){
						this.currentContentClass = 'hasSpeContent',
						this.currentUpperClass = 'hasSpeUpper',
						this.currentIconClass = 'hasSpeIcon',
						this.currentImgClass = 'hasSpeImg',
						this.currentNickClass = 'hasSpeNick',
						this.time = 'time',
						this.currentVideoClass = 'hasSpeVideo',
						this.currentVideoImgClass = 'hasSpeVideoImage',
						this.currentVideoTitle = 'hasSpeVideoTitle',
						this.videoList = res.data.data
					}
				 }
			})
			uni.loadFontFace({
			  family: 'Huawen',
			  source: 'url("https://www.zhangwenning.top:8080/word/华文行楷.ttf")',
			  success() {
			      console.log('success')
			  }
			})	
		},
		methods:{
			goToVideo(e){
				uni.setStorageSync("video_url",e),
				console.log(e)
				console.log(uni.getStorageSync("video_url"))
				uni.navigateTo({
					url: "../BilibiliVideoPage/BilibiliVideoPage"
					
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
	.none{
		width: 0;
		height: 0;
	}
	.hasSpeContent{
		background-color: #FFFFFF;
		margin: 0 auto;
		width: 100%;
		padding-top: 20rpx;
		padding-bottom: 20rpx;
		margin-bottom: 30rpx;
	}
	.hasSpeUpper{
		margin: 0 auto;
		width: 94%;
		margin-bottom: 12rpx;
	}
	.hasSpeIcon{
		float: left;
	}
	.hasSpeImg{
		
		line-height: 100rpx;
		width: 94rpx;
		height: 94rpx;
		margin-top: 3rpx;
		border-radius: 50%;
	}
	.hasSpeNick{
		margin-top: 5rpx;
		font-weight: 700;
		font-size: 35rpx;
		margin-left: 20rpx;
		line-height: 50rpx;
		float: left;
	}
	.time{
		font-weight: 400;
		line-height: 50rpx;
		color: #999ca1;
		font-size: 25rpx;
	}
	.hasSpeVideo{
		margin: 0 auto;
		text-align: center;
		width: 94%;
		margin-bottom: 6rpx;
	}
	.clear{
		clear: both;
	}
	.hasSpeVideoImage{
		width: 100%;
		border-radius: 9rpx;
	}
	.hasSpeVideoTitle{
		margin: 0 auto;
		width: 94%;
		font-size: 30rpx;
		font-weight: 700;
	}
	
</style>
