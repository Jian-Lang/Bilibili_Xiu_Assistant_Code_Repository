<template>
	<view>
		<!-- <view>
			<text>姬霓太美</text>
		</view>
		<view>
			<text selectable>霓太美</text>
		</view>
		<view>
			<text selectable space="ensp">霓太    美</text>
		</view>
		<view>
			<text selectable space="emsp">霓太    美</text>
		</view>
		<view>
			<text selectable space="nbsp" style="font-size:30px">霓太          美</text>
		</view>
		<view>
			<text selectable space="nbsp" >&amp;霓太美</text>
		</view> -->
	<!-- 	<view class="box2" hover-class="box2-active">
			<view class="box" :hover-start-time="1000" :hover-stay-time="1000" hover-class="box-active" hover-stop-propagation="true">我是一个大盒子</view>
		</view>
		<button>按钮</button>
		<button size="mini">按钮</button>
		<button type="primary">按钮</button>
		<button plain="true">按钮</button>
		<button disabled>按钮</button>
		<button loading="true">按钮</button> -->
		<image src="../../static/friend.png" mode="aspectFit"></image>
		<image src="../../static/friend.png" mode="aspectFill"></image>
	</view>
</template>

<script>
</script>

<style>
	.box{
		width: 100px;
		height: 100px;
		background-color: green;
	}
	.box-active{
		background-color: pink;
	}
	.box2{
		width: 200px;
		height: 200px;
		background-color: blue;
	}
	.box2-active{
		background-color: pink;
	}
	
</style>
