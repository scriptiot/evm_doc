## class LED – LED 对象

LED对象是用来控制开发板的LED灯（发光二极管）。

### 构造函数

` class evm.LED(id) `

 创建一个LED对象：
*  id为LED编号（小熊派开发板上有一个LED灯，id编号为1）。
    
    
### 对象函数

`LED.intensity(value)`

获取或者设置LED灯的亮度，亮度范围是0-255,。0表示灯灭，255表示灯完全亮。如果函数没有参数设置，表示读取LED灯的亮度。STM32版本不支持该功能。

`LED.off()`

关闭LED灯。

`LED.on()`

打开LED灯至最大亮度。

`LED.toggle()`

LED灯在打开和关闭之前切换。

### 使用方法

```javascript
var m = require('evm');
var led =new m.LED(0);
led.on();
led.off();
led.toggle();
led.toggle();
```
<video src="http://47.105.117.50:12306/djf/evm_doc_publish/raw/master/zh-cn/vedio/led.mp4?inline=false" 
controls="controls"></video> 



