<template>
	<view>
		<view class="searchInput">
				<input type="text" placeholder="咻一下,发现有趣的up主!" v-model="upName"
				@focus="inputChanged()"/>
		</view>
		<view class="content" v-for="(item,index) in upperList" :key="index">
			<view :class = "currentUpperClass">
				<view :class="currentIconClass"><image :class = "currentImgClass" :src= "item.rface"  mode="widthFix"></image>
				</view>
				<view :class="currentNickClass">
					<text>{{item.rname}}</text>
				</view>
				<span :class="iconColor[index]">
					<span @click = "addSpecialList(item.uid,index)" :class="currentFontIconClass"></span>
				</span>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				currentUpperClass:'upperList_none',
				currentImgClass:'image_unsearched',
				currentIconClass:'icon_unsearched',
				currentNickClass:'nickname_unsearched',
				currentFontIconClass:"fonticon_unsearched",
				imgSrc:'https://www.zhangwenning.top:8080/icon/',
				upperList:[],
				upName:'',
				username:'',
				uid:'',
				iconColor:["un0","un1","un2","un3","un4","un5","un6","un7","un8","un9","un10","un11","un12","un13","un14","un15","un16","un17","un18","un19"]
			}
		},
		onLoad(){
			//this.upperList = res.data.friend_information
			this.username = uni.getStorageSync("username_log")
			this.upName = uni.getStorageSync("up_name")
			uni.request({
				url:'https://www.zhangwenning.top:5000/search',
				method:'GET',	
				data:{username : this.username, content : this.upName},
				header: {
				  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				},
				 success: (res) => {
					if(res.data.status == "400"){
						this.upperList = [],
						this.currentUpperClass = 'upperList_none',
						this.currentImgClass = 'image_unsearched',
						this.currentIconClass = 'icon_unsearched',
						this.currentNickClass = 'nickname_unsearched',
						this.currentFontIconClass = "fonticon_unsearched"
					}
					else if(res.data.status == "200"){
						this.upperList = res.data.user;
						this.currentUpperClass = "upperList_have",
						this.currentImgClass = 'image_searched',
						this.currentIconClass = 'icon_searched',
						this.currentNickClass = 'nickname_searched',
						this.currentFontIconClass = "icon-heart";
						let i = 0;
						for(i = 0;i < 20;i++){
							if(this.upperList[i].hasfollowed == "TRUE"){
								this.iconColor[i] = "Specilized";
								this.$forceUpdate()
							}
						}
					}
				 }
			})
		},
		methods:{
			inputChanged(e){
				uni.setStorageSync("up_name",this.upName)
				uni.switchTab({
					url: "../search/search"
				})
			},
			addSpecialList(e,f){
				this.uid = e;
					if(this.iconColor[f] == "un" + f.toString()){
						uni.request({
							url:'https://www.zhangwenning.top:5000/addfollowing',
							method:'GET',	
							data:{username : this.username, uid: this.uid},
							header: {
							  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
							 },
							 success: (res) => {
									if(res.data.status == "200"){
										uni.showToast({
											title: "已添加特别关心"
										})
									}
							 }
						})
						this.iconColor[f] = "Specilized";
						this.$forceUpdate();
					}
					else{
						uni.request({
							url:'https://www.zhangwenning.top:5000/deletefollowing',
							method:'GET',	
							data:{username: this.username,uid: this.uid},
							header: {
							  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
							 },
							 success: (res) => {
							 	uni.showToast({
							 		title: "已取消特别关心",
							 	})
								// this.friendList = res.data
							 }
						})
						this.iconColor[f] = "un" + f.toString();
						this.$forceUpdate();
					}
			}
		}
	}
</script>
<style>
	page{
		display: flex;
		flex-direction: column;
		background-color: #ededed;
	},
	input{
		width: 92%;
		margin: 0 auto;
		text-align: center;
		border-radius: 10rpx;
		border: 2rpx solid #000000;
		height: 70rpx;
		margin-bottom: 30rpx;
	}
	.upperList_have{
		margin-top: 5rpx;
		position: relative;
		background-color: #FFFFFF;
		width: 100%;
		height: 100rpx;
		margin-bottom: 10rpx;
	}
	.upperList_none{
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
	.icon-heart{
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
	.un0,.un1,.un2,.un3,.un4,.un5,.un6,.un7,.un8,.un9,.un10,
	.un11,.un12,.un13,.un14,.un15,.un16,.un17,.un18,.un19{
		color: #828282
	}
	.Specilized{
		color: #f66041
	}
</style>