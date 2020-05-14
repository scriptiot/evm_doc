## class LED – LED 对象

LED对象是用来控制开发板的LED灯（发光二极管）。

### 构造函数

` class evm.LED(id) `

 创建一个LED对象：
*  id为LED编号（小熊派开发板上有一个LED灯，id编号为0）。
    
    
### 对象函数
`LED.off()`

关闭LED灯。

`LED.on()`

打开LED灯。


### 使用方法

```javascript
var m = require('evm');
var led =new m.LED(0);
led.on();
led.off();

```
<video src="http://47.105.117.50:12306/djf/evm_doc_publish/raw/master/zh-cn/vedio/led.mp4?inline=false" 
controls="controls"></video> 



