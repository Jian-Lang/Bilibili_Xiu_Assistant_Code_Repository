<template>
		<view>
			<view class="cu-form-group">
				<view class="title">账号</view>
				<input type="text" placeholder="请输入账号..." name="userName" 
				@input="userNameInput" 
				confirm-type="done" confirm-hold="true"></input>
			</view>
			<view class="cu-form-group">
				<view class="title">密码</view>
				<input type="text" placeholder="请输入密码..." name="passWord" 
				confirm-type="done" confirm-hold="true"></input> 
			</view>
			<view class="padding">
				<button class="cu-btn block bg-blue margin-tb-sm lg" @click="subBtn" type="" :disabled="isAble" >
					<text v-if="loadFlag" class="cuIcon-loading2 cuIconfont-spin"></text>提交
				</button>
			</view>
		</view>
</template>

<script>
	export default{
		data(){
			return{
				userNameInp : '',
				userNameLen : '',
				loadFlag : false,
				isAble : true
			}
		},
		methods:{
			userNameInput(e){
				// console.log(e);
				this.userNameInp = e.target.value;
				this.userNameLen = e.target.cursor;
				if(this.userNameLen>0){
					this.isAble = false
				}else{
					this.isAble = true
				}
			},
			subBtn(e){
				this.loadFlag = true,
				this.isAble = true
				var $this = this;
				setTimeout(function(){
					// uni.hideLoading()
					uni.showToast({
						title: "提交成功!"
					});
					$this.loadFlag = false
					$this.isAble = false
				},500)
			}
		}
		
	}

</script>

<style>
</style>
