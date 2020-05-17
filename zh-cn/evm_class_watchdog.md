## class Watchdog – 看门狗对象

看门狗对象可以。

### 构造函数

` class evm.Watchdog(label) `

 创建一个 Watchdog对象
 * label："IWDG"
    
    
### 对象函数

`Watchdog.install_timeout(min, max)`

设置看门狗作用时间：
*  min，最小时间
*  max，最大时间（毫秒）
*  返回Watchdog ID


`Watchdog.setup(opt)`

启动看门狗：
*  0: 睡眠状态不使能看门狗
*  1：debug 中断时不使能看门狗
*  调用setup函数前，需使用install_timeout设置作用时间

`Watchdog.feed(id)`
喂狗：用户在最大作用时间内喂狗
*  id: Watchdog ID

`Watchdog.disable()`
失能定时器



### 使用方法
```javascript
var m= require('evm')
var dog =new m.Watchdog("IWDG")
var id = dog.install_timeout(0,10000)
dog.setup(0)
dog.feed(id)
```