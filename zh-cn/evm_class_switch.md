## class Switch –  按键

Switch对象对应的是开发板上的按键。小熊派开发板有两个用户按键 F1、F2， 分别对应的id为1和2.

### 使用方法

```
var m = require('evm');
var sw = new m.Switch(1);
print(sw.value());
function test(){ print('button');}
sw.callback(test);
```

### 构造函数

` class evm.Switch(id) `

 创建一个按键对象，并指定id编号。
    
    
### 对象函数

`Switch.value()`

获取按键状态，按键松开返回0； 按键按下返回1.


`Switch.callback(function)`

按键注册回调函数。当按键按下后，执行回调函数。如果function为null，则表示注销回调函数。




