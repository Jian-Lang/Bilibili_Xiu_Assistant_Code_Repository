<template>
	<view>
		<view>
			<view class="head" @click="change">关注列表</view>
		</view>
		<view class="content" v-for="(item,index) in upperList" :key="index">
			<view :class = "currentUpperClass">
				<view :class="currentIconClass"><image :class = "currentImgClass" :src= "item.face"  mode="widthFix"></image>
				</view>
				<view :class="currentNickClass">
					<text>{{item.name}}</text>
				</view>
				<span :class="currentFontIconColorClass[index]">
					<span @click = "addSpecialList(item.uid,index)" :class="currentFontIconClass" ></span>
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
				currentFontIconColorClass : ["un0","un1","un2","un3","un4","un5",
				"un6","un7","un8","un9","un10","un11","un12","un13","un14","un15",
				"un16","un17","un18","un19","un20","un21","un22","un23","un24","un25",
				"un26","un27","un28","un29","un30","un31","un32","un33","un34","un35",
				"un36","un37","un38","un39","un40","un41","un42","un43","un44","un45",
				"un46","un47","un48","un49"]
			}
		},
		onLoad(){
			//this.upperList = res.data.friend_information,
			this.username = uni.getStorageSync("username_log")
			uni.request({
				url:'https://www.zhangwenning.top:5000/showBfollowing',
				method:'GET',	
				data:{username : this.username},
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
						this.upperList = res.data.data;
						this.currentUpperClass = "upperList_have",
						this.currentImgClass = 'image_searched',
						this.currentIconClass = 'icon_searched',
						this.currentNickClass = 'nickname_searched',
						this.currentFontIconClass = "icon-heart";
						let i = 0;
						for(i = 0;i < 50;i++){
							if(this.upperList[i].has_special_concerned == "TRUE"){
								this.currentFontIconColorClass[i] = "Specilized";
								this.$forceUpdate()
							}
						}
					}	
				 }
			})
		},
		methods:{
			addSpecialList(e,f){
				this.uid = e;
					if(this.currentFontIconColorClass[f] == "un" + f.toString()){
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
						this.currentFontIconColorClass[f] = "Specilized";
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
						this.currentFontIconColorClass[f] = "un" + f.toString();
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
	.head{
		position: relative;
		margin-top: 30rpx;
		font-weight: 600;
		font-size: 40rpx;
		text-align: center;
		margin-bottom: 30rpx;
	},
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
	.un11,.un12,.un13,.un14,.un15,.un16,.un17,.un18,.un19,
	.un20,.un21,.un22,.un23,.un24,.un25,.un26,.un27,.un28,.un29,
	.un30,.un31,.un32,.un33,.un34,.un35,.un36,.un37,.un38,.un39,
	.un40,.un41,.un42,.un43,.un44,.un45,.un46,.un47,.un48,.un49
	{
		color: #828282
	}
	.Specilized{
		color: #f66041
	}
</style>