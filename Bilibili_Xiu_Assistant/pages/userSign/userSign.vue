<template>
    <view class="container">
        <editor id="editor" class="ql-container" :placeholder="placeholder" @blur="blur" @focus="focus" @ready="onEditorReady"></editor>
        <button type="warn" @click="goBack" :disabled="disable">确定修改</button>
    </view>
</template>

<script>
    export default {
        data() {
            return {
				content: '',
                placeholder: '请输入30位以内的个人介绍哦(超过30位将无法"确认修改"),完成输入后并收起手机软键盘后可点击"确认修改"按钮...',
				disable: 'true',
				username:''
            }
        },
        methods: {
			focus(){
				this.disable = true
			},
			blur(){
				this.editorCtx.getContents({
					success: (res) => {	
						this.content = res.html,
						console.log(this.content),
						this.content = this.content.substring(3,this.content.length-4);
						if(this.content.length < 30){
							this.disable = false
						}
						else{
							this.disable = true
						}
						console.log(this.content);
					}
				})
			},
			onEditorReady(){    
			    uni.createSelectorQuery().select('#editor').context((res) =>{    
			    this.editorCtx = res.context    
			     this.editorCtx.setContents({    
			            html:this.EditGoodsDetail.content    
			        })    
			    }).exec()    
			},
			goBack(){
				if(this.content != "<br>"){
					uni.setStorageSync("sign",this.content)
				}
				else{
					uni.setStorageSync("sign","")
				};
				this.content = uni.getStorageSync("sign"),
				this.username = uni.getStorageSync("username_log"),
				uni.request({
					url:'https://www.zhangwenning.top:5000/uploadsign',
					method:'GET',	
					data:{username : this.username, sign : this.content},
					header: {
					  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
					 },
					 success: (res) => {
					 	uni.showToast({
					 		title: res.data.message
					 	})
					 }
				})
				uni.switchTab({
					url: "../mine/mine"
				})
			}
     
        }
    }
</script>
<style>
    .container {
        padding: 10px;
    }
    #editor {
        width: 100%;
        height: 300px;
        background-color: #CCCCCC;
    }

    button {
        margin-top: 10px;
    }
</style>