
## class E53SF1 – 烟雾采集控制器模块

### 构造函数

` class evm.E53SF1()`
 创建一个烟雾采集控制器模块。

`E53SF1.smog()`
获取烟雾浓度。

`E53SF1.lighton()`
开灯。

`E53SF1.lightoff()`
关灯。

`E53SF1.beepon()`
开启蜂鸣器。

`E53ST1.beepoff()`
关闭蜂鸣器。

### 使用方法
```javascript
var m = require('evm')
var sf = new m.E53SF1()
sf.smog()
sf.beepon()
sf.beepoff()
sf.lighton()
sf.lightoff()
```
