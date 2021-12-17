<template>
	<view>
		<view class="header">
			添加咻友
		</view>
		<view class="searchInput">
			<input type="text" placeholder="请输入对方的昵称" v-model="friendName" @input="inputChanged"/>
		</view>
		<view class="searchbtn" @click="search">
			搜索             <span class="icon-search"></span>
		</view>
		<view :class = "currentclass">
			<view :class="currentIconClass"><image :class = "currentImgClass" :src="imgSrc" mode="widthFix"></image></view>
			<view :class="currentNickClass">
				<text>{{searchName}}</text>
			</view>
			<span @click="add" :class="currentFontIconClass"></span>
		</view>
	</view>
</template>
<script>
	export default{
		data(){
			return{
				userName:'',
				friendName:'',
				imgSrc:'',
				searchName:'',
				color:'#f27498',
				currentclass:'friend_unSearched',
				currentImgClass:'image_unsearched',
				currentIconClass:'icon_unsearched',
				currentNickClass:'nickname_unsearched',
				currentFontIconClass:"fonticon_unsearched"
			}
		},
		methods:{
			search(){
				this.userName = uni.getStorageSync("username_log"),
				uni.request({
					url:'https://www.zhangwenning.top:5000/searchfriend',
					method:'GET',	
					data:{username : this.userName, friendname : this.friendName},
					header: {
					  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
					 },
					 success: (res) => {
						if(this.friendName == "") return;
						this.searchName = res.data.username;
						if(this.searchName == null){
							this.searchName = "此用户不存在!"
							this.imgSrc = ""		
						}
						else if(this.searchName == uni.getStorageSync("username_log")){
							this.currentFontIconClass = "icon-user"
							this.currentNickClass = "nickname_searched",
							this.currentIconClass = "icon_searched",
							this.currentImgClass = "image_searched",
							this.currentclass = "friend",
							this.imgSrc = "https://www.zhangwenning.top:443/icon/" + this.searchName
						}
						else if(res.data.message == "1"){
							this.currentFontIconClass = "icon-user-check"
							this.currentNickClass = "nickname_searched",
							this.currentIconClass = "icon_searched",
							this.currentImgClass = "image_searched",
							this.currentclass = "friend",
							this.imgSrc = "https://www.zhangwenning.top:443/icon/" + this.searchName
						}
						else{
							this.currentFontIconClass = "icon-user-plus1"
							this.currentNickClass = "nickname_searched",
							this.currentIconClass = "icon_searched",
							this.currentImgClass = "image_searched",
							this.currentclass = "friend",
							this.imgSrc = "https://www.zhangwenning.top:443/icon/" + this.searchName	
						}
			
					 }
				})
				console.log(this.friendName)
			},
			inputChanged(e){
				if(e.target.value == ""){
					this.searchName = "",
					this.imgSrc = "",
					this.currentFontIconClass = "fonticon_unsearched"
					this.currentclass = "friend_unSearched",
					this.currentIconClass = "icon_unsearched",
					this.currentImgClass = "image_unsearched",
					this.currentNickClass = "nickname_unsearched"
				}
			},
			add(){
				this.userName = uni.getStorageSync("username_log");
				if(this.currentFontIconClass == "icon-user-plus1"){
					uni.request({
						url:'https://www.zhangwenning.top:5000/addfriend',
						method:'GET',	
						data:{username : this.userName, friendname: this.friendName},
						header: {
						  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
						 },
						 success: () => {
						 	uni.showToast({
						 		title: "添加成功"
						 	}),
							this.currentFontIconClass = "icon-user-check"
						 }
					})
				}
				else if(this.currentFontIconClass == "icon-user"){
					uni.showToast({
						title: "不能添加自己哦！",
						icon: "none"
					})
				}
				else if(this.currentFontIconClass == "icon-user-check")
					uni.showToast({
						title: "已有该好友！",
						icon: "none"
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
	.header{
		position: relative;
		margin-top: 25rpx;
		font-weight: 600;
		font-size: 40rpx;
		text-align: center;
		margin-bottom: 35rpx;
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
		margin-top: 40rpx;
		width: 35%;
		height: 65rpx;
		color: #FFFFFF;
	}
	.icon-search{
		margin-left: 5rpx;
	}
	.friend_unSearched{
		text-align: center;
		width: 100%;
		height: 110rpx;
	}
	.friend{
		margin-top: 45rpx;
		position: relative;
		background-color: #FFFFFF;
		width: 100%;
		height: 100rpx;
	}
	.icon_searched{
		height: 100rpx;
		width: 100rpx;
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
		margin-top: 3rpx;
		line-height: 94rpx;
		margin-left: 35rpx;
		width: 94rpx;
		height: 100rpx;
		border-radius: 50%;
	}
	.icon_searched,.nickname_searched{
		float: left;
	}
	.nickname_searched{
		margin-left: 55rpx;
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
	.icon-user-plus1,.icon-user,.icon-user-check{
		line-height: 110rpx;
		position: absolute;
		right: 35rpx;
		font-size: 40rpx;
	}
</style>