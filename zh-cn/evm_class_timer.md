## class Timer – 硬件定时器

### 构造函数

` class evm.Timer(id, prescaler，period)`
 创建一个Timer对象。
 - `id` 定时器编号，目前仅支持TIM2，即默认id=2;
 - `prescaler` 指定要加载到定时器的PSC中的值。定时器时钟源除以（ prescaler + 1 ）以得出定时器时钟;
 - `period`用于定时器1、3、4、6-15。[0-0x3fffffff]用于定时器2和5。指定要加载到定时器的ARR中的值。该值决定定时器的周期（即当计数器循环时）。定时器将在 period + 1 定时器时钟循环后滚动。

`Timer.init(*, prescaler, period)`
定时器初始化函数，参数内容同上；

`Timer.deinit()`
反初始化定时器。
禁用回调（以及关联的中断请求）。
禁用任何通道回调（以及关联的中断请求）。停用定时器，并禁用定时器外围设备。

`Timer.callback(fun)`
设置定时器触发时所调用的函数。 fun 是被传递的1参数，即定时器对象。若 fun 为 None ，则禁用回调。

### 使用方法
```javascript
var m= require('evm')
function tt(){print('timer');}
var timer =new m.Timer(0,7999,999)
timer.callback(tt)
```
