## class RTC – 实时时钟

RTC是一个独立的时钟驱动，用于记录系统时间。

### 使用方法

```
var m = require('evm');
var rtc = new m.RTC();
rtc.datetime((2020, 4, 3, 5, 13, 0, 0, 0));
print(rtc.datetime());
```

### 构造函数

` class evm.RTC() `

 创建一个RTC对象：
    
    
### 对象函数

`RTC.datetime([year, month, day, week, hour, minute, second])`

获取或者设置系统时间。
如果没有参数，则该函数返回一个时间数组，数组格式为：[年, 月, 日, 星期, 时, 分, 秒]。
如果有参数，表示设置时钟。
