## class ADC – 模拟转数字信号



### 构造函数

` class evm.ADC(id) `

 创建一个ADC对象，并指定id编号。小熊派开发板支持1个ADC引脚（ADC0_IN12）,默认编号为1。
 在创建对象时如果不指定id，则默认使用编号1.

    
    
### 对象函数

`ADC.read()`

读取adc转换值，值的范围是0到4095。


### 使用方法

```javascript
var m = require('evm');
var adc = new m.ADC();
print(adc.read())
```

