## class ADC – 模拟转数字信号



### 构造函数

` class evm.ADC(label,channel) `

 创建一个ADC对象，并指定编号,通道。
 小熊派开发板支持1个ADC引脚（ADC1_IN3）,默认编号为label = "ADC_1",channel = 3。

    
    
### 对象函数

`ADC.read()`

读取adc转换值，值的范围是0到4095。


### 使用方法

```javascript
var m = require('evm');
var adc = new m.ADC("ADC_1",3);
print(adc.read())
```

