## class Pin – IO引脚控制

Pin对象用来控制芯片的IO引脚。通过Pin对象可以设置IO引脚的输入输出模式、 引脚的高低电平输出。如果要设置引脚的模拟输入模式，请参考ADC类。

### 构造函数

` class evm.Pin(label, pin, flags) `

 创建一个Pin对象：
*  label GPIOX，例如：
    *  GPIOA, GPIOB, GPIOC, GPIOD, GPIOE, GPIOF, GPIOG
    *  由于芯片引脚数的差异，并非所有端口名称都能使用。具体可参考芯片手册说明。
*  pin，引脚号。引脚号通常为0 - 15.
*  flags，引脚配置参数，可以通过 xxx|xxx 方式进行组合配置：
    *  Pin.IN, 输入
    *  Pin.OUT，输出
    *  Pin.DISCONNECTED，取消配置、引脚悬空
    *  Pin.INT_ENABLE，使能外部中断
    *  Pin.INT_DISABLE，关闭外部中断
    *  Pin.INT_EDGE_RISING，外部中断边缘上升触发
    *  Pin.INT_EDGE_FALLING，外部中断边缘下降触发
    *  Pin.INT_EDGE_BOTH，外部中断边缘上升、下降均触发
    *  Pin.PULL_UP，上拉模式
    *  Pin.PULL_DOWN，下拉模式
    *  Pin.OPEN_SOURCE，开源极模式
    *  Pin.OPEN_DRAIN，开漏极模式

### 对象函数

`Pin.value(value)`
获取或者设置引脚的状态，亮度范围是0-255。0表示低电平，其它表示高电平。
如果函数没有参数设置，表示读取引脚电平。

创建对象例子：
    
```javascript
var m = require('evm')
var pin = new m.Pin('GPIOC', 13, m.Pin.OUT)
pin.value(1)
pin.value()
```
