## class Timer – 定时器

### 构造函数

` class evm.Timer()`
 创建一个Timer对象。


`Timer.setInterval(callback, period)`
设置回调函数及定时周期；
*  callback: 回调函数
*  period:   定时周期


### 使用方法
```javascript
var m= require('evm')
function tt(){print('timer');}
var timer =new m.Timer()
timer.setInterval(tt,1000)
```
