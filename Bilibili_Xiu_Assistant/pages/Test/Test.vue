<template>
	<view>
	
			<view :class="className[index]" v-for="(item,index) in list" :key="index" @click="TriggerEvent(index)">
				{{item.name}}
			</view>
			<view class="icon-user-plus">
				
			</view>
			
	</view>
</template>

<script>
	export default{
		data(){
			return{
				className:["no1","no2","no3","no4","no5","no6","no7","no8","no9","no10"],
				list:[{"name":"张一","age":"13"},
				{"name":"张二","age":"13"},
				{"name":"张三","age":"13"},{"name":"李四","age":"13"},
				{"name":"张五","age":"13"},{"name":"张六","age":"13"},
				{"name":"张七","age":"13"},{"name":"张八","age":"13"},
				{"name":"张九","age":"13"},{"name":"张十","age":"13"}]
			}
		},
		onLoad() {
				
		},
		methods:{
			TriggerEvent(e){
				this.testLoop()
				if(this.className[e] == "no" + (e+1).toString()){
					console.log(this.className[e])
					this.className[e] = "change" + (e+1).toString()
					this.$forceUpdate();
				}
				
				else{
						console.log(this.className[e])
						this.className[e] = "no" + (e+1).toString()
						this.$forceUpdate();
						
				}
			
			},
			testLoop(){
				let j = 0;
				for(j = 0; j< 10; j++){
					console.log(this.className[j])
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
	.no1,.no2,.no3,.no4,.no5,.no6,.no7,.no8,.no9,.no10{
		width: 100rpx;
		height: 100rpx;
		margin: 50rpx auto ;
		background-color: #4CD964;
	}
	.change1,.change2,.change3,.change4,.change5,.change6,.change7,.change8,.change9,.change10{
		width: 100rpx;
		height: 100rpx;
		margin: 50rpx auto ;
		background-color: #007AFF;
	}
	.icon-user-plus:before {
	  content: "\e902";
	}
</style>
