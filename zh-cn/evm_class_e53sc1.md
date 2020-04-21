
## class E53SC1 – 路灯照明模块

### 构造函数

` class evm.E53SC1()`
 创建一个E53SC1对象。

`E53SC1.lux()`
获取光强传感器值。

`E53SC1.lighton()`
开灯。

`E53SC1.lightoff()`
关灯。

### 使用方法
```javascript
var m = require('evm')
var el = new m.E53SC1()
el.lighton()
el.lux()
el.lightoff()
```