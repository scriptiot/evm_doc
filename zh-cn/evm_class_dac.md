## class DAC – 数字转模拟电压

使用DAC可以使引脚输出指定的模拟电压值，电压值范围是0到3.3V。小熊派开发板使用PA4引脚作为DAC的输出引脚。

### 构造函数

` class evm.DAC(label,channel)`

 创建一个DAC对象，并指定编号,通道。
 小熊派开发板支持1个DAC引脚（DAC1_OUT2）,默认编号为label = "DAC_1",channel = 2。

    
    
### 对象函数

`DAC.write(value)`

 设置DAC引脚的电压值，value的范围是0到4095，对应电压范围是0到3.3V。


### 使用方法

```javascript
var m = require('evm');
var dac new m.DAC("DAC_1",2);
dac.write(1000);
```

