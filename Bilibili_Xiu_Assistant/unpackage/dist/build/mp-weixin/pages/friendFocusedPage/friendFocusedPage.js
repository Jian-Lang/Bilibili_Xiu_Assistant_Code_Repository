(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/friendFocusedPage/friendFocusedPage"],{"018b":function(n,e,t){"use strict";var u;t.d(e,"b",(function(){return r})),t.d(e,"c",(function(){return a})),t.d(e,"a",(function(){return u}));var r=function(){var n=this,e=n.$createElement;n._self._c},a=[]},"0367":function(n,e,t){"use strict";t.r(e);var u=t("018b"),r=t("43b7");for(var a in r)"default"!==a&&function(n){t.d(e,n,(function(){return r[n]}))}(a);t("8233");var c,s=t("f0c5"),o=Object(s["a"])(r["default"],u["b"],u["c"],!1,null,null,null,!1,u["a"],c);e["default"]=o.exports},"0cc6":function(n,e,t){},"43b7":function(n,e,t){"use strict";t.r(e);var u=t("f1ca"),r=t.n(u);for(var a in u)"default"!==a&&function(n){t.d(e,n,(function(){return u[n]}))}(a);e["default"]=r.a},8233:function(n,e,t){"use strict";var u=t("0cc6"),r=t.n(u);r.a},b6c6:function(n,e,t){"use strict";(function(n){t("035c");u(t("66fd"));var e=u(t("0367"));function u(n){return n&&n.__esModule?n:{default:n}}n(e.default)}).call(this,t("543d")["createPage"])},f1ca:function(n,e,t){"use strict";(function(n){Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var t={data:function(){return{currentUpperClass:"upperList_none",currentImgClass:"image_unsearched",currentIconClass:"icon_unsearched",currentNickClass:"nickname_unsearched",currentFontIconClass:"fonticon_unsearched",imgSrc:"https://www.zhangwenning.top:8080/icon/",upperList:[],upName:"",username:"",uid:"",friendname:"",currentFontIconColorClass:["un0","un1","un2","un3","un4","un5","un6","un7","un8","un9","un10","un11","un12","un13","un14","un15","un16","un17","un18","un19","un20","un21","un22","un23","un24","un25","un26","un27","un28","un29","un30","un31","un32","un33","un34","un35","un36","un37","un38","un39","un40","un41","un42","un43","un44","un45","un46","un47","un48","un49"]}},onLoad:function(){var e=this;this.username=n.getStorageSync("username_log"),this.friendname=n.getStorageSync("friend_name"),n.request({url:"https://www.zhangwenning.top:5000/showfriendBconcern",method:"GET",data:{username:this.username,friendname:this.friendname},header:{"content-type":"application/x-www-form-urlencoded"},success:function(n){if("400"==n.data.status)e.upperList=[],e.currentUpperClass="upperList_none",e.currentImgClass="image_unsearched",e.currentIconClass="icon_unsearched",e.currentNickClass="nickname_unsearched",e.currentFontIconClass="fonticon_unsearched";else if("200"==n.data.status){e.upperList=n.data.data,e.currentUpperClass="upperList_have",e.currentImgClass="image_searched",e.currentIconClass="icon_searched",e.currentNickClass="nickname_searched",e.currentFontIconClass="icon-heart";var t=0;for(t=0;t<50;t++)"TRUE"==e.upperList[t].has_special_concerned&&(e.currentFontIconColorClass[t]="Specilized",e.$forceUpdate())}}})},methods:{addSpecialList:function(e,t){this.uid=e,this.currentFontIconColorClass[t]=="un"+t.toString()?(n.request({url:"https://www.zhangwenning.top:5000/addfollowing",method:"GET",data:{username:this.username,uid:this.uid},header:{"content-type":"application/x-www-form-urlencoded"},success:function(e){"200"==e.data.status&&n.showToast({title:"已添加特别关心"})}}),this.currentFontIconColorClass[t]="Specilized",this.$forceUpdate()):(n.request({url:"https://www.zhangwenning.top:5000/deletefollowing",method:"GET",data:{username:this.username,uid:this.uid},header:{"content-type":"application/x-www-form-urlencoded"},success:function(e){n.showToast({title:"已取消特别关心"})}}),this.currentFontIconColorClass[t]="un"+t.toString(),this.$forceUpdate())}}};e.default=t}).call(this,t("543d")["default"])}},[["b6c6","common/runtime","common/vendor"]]]);