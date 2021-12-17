<template>
    <view>
<!--        <view class="uni-padding-wrap">
            <view class="uni-title">日期：{{year}}年{{month}}月{{day}}日</view>
        </view> -->
		<view class="title">
			当前最大获取天数: {{oldDay}}
		</view>
        <picker-view v-if="visible" :indicator-style="indicatorStyle" :value="value[0]" @change="dayChange" class="picker-view">
            <picker-view-column>
                <view class="item" v-for="(item,index) in days" :key="index">{{item}}天</view>
            </picker-view-column>
        </picker-view>
		<view class="btn_confirm" @click="confirm">
			确定             
		</view>
    </view>
</template>
<script>
    export default {
		data(){
			return{
				oldDay:'',
				username:'',
				value : [2],
				days:['1','2','3','4','5'],
				select:[],
				indicatorStyle: `height: 50px;`,
				determinedDays:'',
				visible: true
			}
		},
		onShow(){
			this.username = uni.getStorageSync("username_log");
			uni.setStorageSync("day",""),
			uni.request({
				url:'https://www.zhangwenning.top:5000/getuser',
				method:'GET',	
				data:{username : this.username},
				header: {
				  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				 },
				 success: (res) => {
					uni.setStorageSync("oldDay",res.data.Day);
					this.oldDay = res.data.Day;
					this.$forceUpdate();
				 }
			})
		},
        methods: {
           dayChange(e){
			   this.select = e.detail.value,
			   this.determinedDays = this.select[0]+1,
			   uni.setStorageSync("day",this.determinedDays.toString())
		   },
		   confirm(){
			   if(uni.getStorageSync("day") != ""){
				    this.determinedDays = uni.getStorageSync("day");
			   }
			   else if(uni.getStorageSync("day")  == ""){
				    this.determinedDays = '1';
			   }
			   this.username = uni.getStorageSync("username_log");
			   if(this.determinedDays != uni.getStorageSync("oldDay")){
				   uni.request({
				   	url:'https://www.zhangwenning.top:5000/changeday',
				   	method:'GET',	
				   	data:{username : this.username, day : this.determinedDays},
				   	header: {
				   	  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
				   	 },
				   	 success: (res) => {
								this.oldDay = this.determinedDays,
				   				uni.showToast({
				   					title:"天数修改成功",
				   				})
				   				// setTimeout(function() {
				   				// 	uni.switchTab({
				   				// 		url: "../mine/mine"
				   				// 	})
				   				// }, 800);
				   	 }
				   })
			   }
			   else{
				   uni.showToast({
						title:"您未作出修改",
						icon: "none"
				   })
				   // setTimeout(function() {
				   // 	uni.switchTab({
				   // 		url: "../mine/mine"
				   // 	})
				   // }, 800);
			   }
				   
		   }
        }
    }
</script>
<style>
	.title{
		margin-top: 50rpx;
		text-align: center;
		width: 100%;
		font-size: 45rpx;
		font-weight: 700;
	}
    .picker-view {
	
        width: 750rpx;
        height: 600rpx;
    }
    .item {
		font-size: 35rpx;
		line-height: 50px;
        height: 50px;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
	.btn_confirm{
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
</style>