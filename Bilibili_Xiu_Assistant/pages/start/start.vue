<template>
	<view>
		<view class="img-f">
			<image src="../../static/logo.png" mode="widthFix"></image>
		</view>
		<view class="slogan1">咻一下</view>
		<view class="slogan2">随时随地得到最新推送</view>
		<view class="btn-f">
			<button size="mini" plain="true" class="btn" @tap="goToNextPage()"><text>点击进入</text></button>
		</view>
		<view class="protocol" @click="goToProtocol()">《【哔哩哔哩_咻管家】微信小程序用户协议》</view>
	</view>
</template>

<script>
	export default{
		methods: {
			goToNextPage(){
				uni.showModal({
				    title: '用户须知',
					confirmText: '我同意',
					cancelText: '我拒绝',
				    content: '为使用【哔哩哔哩_咻管家】微信小程序服务(以下简称“本服务”或“小程序服务”)，'+
					'您应当阅读并遵守《【哔哩哔哩_咻管家】微信小程序用户协议》，请务必审慎阅读、充分理解各'+
					'条款内容，特别是免除或限制责任的相应条款，以及开通或使用某项服务的单独协议，并选择接受或不接受。' +
					'除非您已阅读并接受本条款所有条款，否则您无权使用【哔哩哔哩_咻管家】微信小程序服务。您对本'+
					'服务的登录、查看、发布信息等行为即视为己阅读并同意本条款的约束。'+
					'如果您未满18周岁，请在法定监护人的陪同下阅读本您协议，并特别注意未成年人使'+
					'用条款。',
				    success: function (res) {
				        if (res.confirm) {
				            uni.navigateTo({
				                        url: '../login/login',
				                    });
				        } else if (res.cancel) {
				            
				        }
				    }
				});
		},
		goToProtocol(){
			uni.navigateTo({
				url: "../user_protocol/user_protocol"
			})
		}
	},
	}
</script>

<style>
	page{
		background-color: #000;
	}
	.img-f{
		margin-top: 10%;
		text-align: center;
	}
	image {
	   width: 65%;
	   margin: auto;
	}
	.slogan1{
		margin-top: -20rpx;
		color: #FFFFFF;
		font-size: 32px;
		text-align: center;
	}
	.slogan2{
		margin-top: 30rpx;
		color: #FFFFFF;
		font-size: 16px;
		text-align: center;
	}
	.btn-f{
		margin-top: 100rpx;
		text-align: center;
	}
	.btn-f text{
		font-size: 14px;
		color: #FFFFFF
	}
	.protocol{
		margin-top: 100rpx;
		color: #FFFFFF;
		font-size: 12px;
		text-align: center;
	}
</style>