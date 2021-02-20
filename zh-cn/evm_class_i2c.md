## class UART – 串口

### 构造函数

` class evm.UART(label, baudrate, databits, parity, stopbits, rxBufSize)`
 创建一个UART对象,并执行初始化操作。
*  label:     串口号   
    *   UART_1
    *   UART_2
    *   UART_3
*  baudrate:  波特率
*  databits:  数据位
    *   DATA5
    *   DATA6
    *   DATA7
    *   DATA8
    *   DATA9

*  parity:    极性
    *   NONE
    *   ODD
    *   EVEN
*  stopbits:  停止位
    *   STOP05
    *   STOP1
    *   STOP15
    *   STOP2

*  rxBufSize: 缓存区大小（默认 256）

`UART.any()`
返回缓存区中数据大小

`UART.read(buf, offset, size)`
读取串口数据
*   buf: 数据存储
*   offset: 偏移量
*   size: 读取数据大小

`UART.write(buf, offset, size)`
发送串口数据
*   buf: 数据存储
*   offset: 偏移量
*   size: 读取数据大小

`UART.write(str)`
发送串口字符串
*   str: 字符串数据

### 使用方法
```javascript
var m = require('evm')
var u = new m.UART("UART_1")
u.write("evm")

```
