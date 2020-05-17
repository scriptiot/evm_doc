## EVM函数与支持外设列表

` delay_ms(ms) `
毫秒延时
*  ms:毫秒
```javascript
var m = require("evm")
m.delay_ms(100) 
```

` delay_us(us) `
微秒延时
*  us:微秒
```javascript
var m = require("evm")
m.delay_us(100) 
```

## 目前EVM模块支持的驱动外设
*   ` ADC `：模数转换器
*   ` DAC `：数模转换器
*   ` Flash `：存储器
*   ` Pin `：引脚
*   ` LED `：灯
*   ` Switch `：开关/按键
*   ` Timer `：定时器
*   ` Watchdog `：看门狗
*   ` UART `：串口

EVM后续将持续集成多种外设驱动以及通用模块……

