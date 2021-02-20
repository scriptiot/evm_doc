## class Flash – Flash存储对象

Flash对象可以访问小熊派开发板上的SPI驱动的Flash闪存。

### 构造函数

` class evm.FLASH(label) `

 创建一个 Flash对象，并初始化Flash驱动。
    
    
### 对象函数

`Flash.readblocks(address, buf, size)`

读取闪存内容：
*  address， 起始地址
*  buf，字节数组
*  size，要读取的数据大小


`Flash.writeblocks(address, buf, size)`

写入闪存内容：
*  address， 起始地址
*  buf，字节数组
*  size，要写入的数据大小
