## class Pin – IO引脚控制

Pin对象用来控制芯片的IO引脚。通过Pin对象可以设置IO引脚的输入输出模式、 引脚的高低电平输出。如果要设置引脚的模拟输入模式，请参考ADC类。

### 构造函数

` class evm.Pin(port, pin, mode) `

 创建一个Pin对象：
*  port，引脚所在的端口。对于stm32芯片，可以使用如下几个默认的端口：
    *  Pin.GPIOA, Pin.GPIOB, Pin.GPIOC, Pin.GPIOD, Pin.GPIOE, Pin.GPIOF, Pin.GPIOG
*  pin，引脚号。对于stm32，引脚号通常为0 - 15.
*  mode，芯片输入输出模式。对于stm32芯片， 可以使用如下默认设置：
    *  Pin.AF_OD
    *  Pin.AF_PP
    *  Pin.ANALOG
    *  Pin.IN
    *  Pin.OUT_OD
    *  Pin.OUT_PP
    *  Pin.PULL_DOWN
    *  Pin.PULL_NONE
    *  Pin.PULL_UP

同时，也可以这样创建一个Pin对象：
    `pin = evm.Pin('GPIOB', 1, 'OUT_OD')`
    
    
### 对象函数

`Pin.value(value)`

获取或者设置引脚的电平：
*  没有参数时，返回引脚的电平值0或者1.
*  参数为0或者false时，引脚输出低电平。参数为大于0或者true时，输出高电平。


### 使用方法

```javascript
var m = require('evm');
var pin = new m.Pin(m.Pin.GPIOB, 5, m.Pin.OUT_PP);
pin.value(0);
print(pin.value());
```

