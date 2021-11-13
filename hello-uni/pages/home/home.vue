<template>
	<view>
		<view>数据绑定</view>
		<view>{{msg}}</view>
		<view>{{1+'nihao'}}</view>
		<view>{{1+1}}</view>
		<view>{{flag?'A':'B'}}</view>
		<image v-bind:src="imgUrl"></image>
		<view v-for="(item,index) in arr" v-bind:key="item.id">
			序号：{{index}}，名字：{{item.name}}，年龄：{{item.age}}
		</view>
		<button type="primary" @click="clickHandle(20,$event)">按钮</button>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				msg:'hello',
				flag: false,
				imgUrl:'../../static/user.png',
				arr: [
					{
						name:'用户1',
						age:20,
						id:1
					},
					{
						name:'用户2',
						age:20,
						id:2
					},
					{
						name:'用户3',
						age:30,
						id:3
					},
					{
						name:'小沈阳',
						age:22,
						id:4
					}
				]
			}
		},
	methods: {
		clickHandle(num,e){
			console.log(num,e)
		}
	}
	}
	
</script>

<style>
</style>
