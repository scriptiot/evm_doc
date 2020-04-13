
## class E53ST1 – GPS定位采集控制模块

### 构造函数

` class evm.E53ST1()`
 创建一个E53ST1对象。

`E53ST1.location()`
获取经纬度值。返回list对象，长度2，分别为经度、纬度。

`E53ST1.lighton()`
开灯。

`E53ST1.lightoff()`
关灯。

`E53ST1.beepon()`
开启蜂鸣器。

`E53ST1.beepoff()`
关闭蜂鸣器。

### 使用方法
```javascript
var m = require('evm')
var st = new m.E53ST1()
st.loghton()
st.lightoff()
st.beepon()
st.beepoff()
st.location()
```
