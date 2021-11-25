<template>
	<view>
		<view>
			<view class="head" @click="change">咻友录<span class="icon-user-plus" @click="searchFriends"></span></view>
		</view>
		<view class="content" @click="goToFriendPage">
			<view :class = "currentfriendclass" v-for="(item,index) in friendList" :key="index">
				<view :class="currentIconClass"><image :class = "currentImgClass" :src= "imgSrc+item.username"  mode="widthFix"></image></view>
				<view :class="currentNickClass">
					<text>{{item.username}}</text>
				</view>
				<span  @click.stop ="deletefriend(item.username)" :class="currentFontIconClass"></span>
			</view>
		</view>
	</view>

</template>

<script>
	var _self;
	export default{
		data(){
			return{
				friendList:[],
				currentfriendclass:'friendList_none',
				currentImgClass:'image_unsearched',
				currentIconClass:'icon_unsearched',
				currentNickClass:'nickname_unsearched',
				currentFontIconClass:"fonticon_unsearched",
				// currentfriendclass : "friendList_have",
				// currentImgClass : 'image_searched',
				// currentIconClass : 'icon_searched',
				// currentNickClass : 'nickname_searched',
				// currentFontIconClass : "icon-user-minus",
				imgSrc:'http://47.113.196.102:8080/icon/',
				username: ''

			}
		},
		onShow() {
			this.username = uni.getStorageSync("username_log")
			uni.request({
				url:'http://47.113.196.102:5000/getfriend',
				method:'GET',	
				data:{username : this.username},
				header: {
				  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				 },
				 success: (res) => {
					if(res.data.status == "400"){
						this.friendList = [],
						this.currentfriendclass = 'friendList_none',
						this.currentImgClass = 'image_unsearched',
						this.currentIconClass = 'icon_unsearched',
						this.currentNickClass = 'nickname_unsearched',
						this.currentFontIconClass = "fonticon_unsearched"
					}
					else if(res.data.status == "200"){
						this.friendList = res.data.friend_information,
						this.currentfriendclass = "friendList_have",
						this.currentImgClass = 'image_searched',
						this.currentIconClass = 'icon_searched',
						this.currentNickClass = 'nickname_searched',
						this.currentFontIconClass = "icon-user-minus"
					}	
				 }
			})
		},
		methods:{
			searchFriends(){
				uni.navigateTo({
					url: "../searchFriends/searchFriends"
				})
			},
			refresh(e){
				this.username = uni.getStorageSync("username_log"),
				uni.request({
					url:'http://47.113.196.102:5000/getfriend',
					method:'GET',	
					data:{username : this.username},
					header: {
					  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
					 },
					 success: (res) => {
					 	uni.showToast({
					 		title: "删除成功",
					 	}),
						this.friendList = res.data.friend_information
					 }
				})
			},
			deletefriend(e){
				let _this = this;
				let name = uni.getStorageSync("username_log")
				uni.showModal({
					title: "确定删除" + e + "吗？",
					confirmText: '确定',
					cancelText: '取消',
					success: function (res) {
					    if (res.confirm) {	
							uni.request({
								url:'http://47.113.196.102:5000/deletefriend',
								method:'GET',	
								data:{username : name,friendname:e},
								header: {
								  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
								 },
								 success: (res) => {
								 	uni.showToast({
								 		title: "删除成功",
								 	})
									// this.friendList = res.data
								 }
							})
							_this.refresh(e)
					    } else if (res.cancel) {
					        
					    }
					}
				})
			},
			goToFriendPage(){
				uni.navigateTo({
					url: "../xiu_friendPage/xiu_friendPage"
				})
			},
			testFn (e) {
			
			　　e.preventDefault();
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
	.head{
		position: relative;
		margin-top: 20rpx;
		font-weight: 600;
		font-size: 40rpx;
		text-align: center;
		margin-bottom: 60rpx;
	}
	.icon-user-plus{
		position: absolute;
		right: 20rpx;
		top: 12rpx;
		font-size: 45rpx;
	}
	.friendList_have{
		margin-top: 5rpx;
		position: relative;
		background-color: #FFFFFF;
		width: 100%;
		height: 100rpx;
		margin-bottom: 10rpx;
	}
	.friendList_none{
		width: 0rpx;
		height: 0rpx;
	}
	.nickname_searched{
		margin-left: 25rpx;
		line-height: 100rpx;
	}
	.nickname_unsearched{
		line-height: 100rpx;
		margin: 0 auto;
		text-align: center;
	}
	.fonticon_unsearched{
		height: 0rpx;
		width: 0rpx;
	}
	.icon-user-minus{
		line-height: 110rpx;
		position: absolute;
		right: 35rpx;
		font-size: 40rpx;
	}
	.icon_searched,.nickname_searched{
		float: left;
	}
	.icon_unsearched{
		width: 0rpx;
		height: 0rpx;
	}
	.image_unsearched{
		width: 0rpx;
		height: 0rpx;
	}
	.image_searched{
		line-height: 100rpx;
		margin-left: 35rpx;
		width: 94rpx;
		height: 94rpx;
		margin-top: 3rpx;
		border-radius: 50%;
	}
</style>
