## 1. evm-tools是什么



## 2. 下载evm-tools

+ 解压到任意目录
+ 下载Python3 ，如果python3已经安装，跳过。


## 3. 一键安装EVM开发环境

+ evm.sh用法

```sh
USAGE: ./evm.sh [path of evm-tools]
e.g.: ./evm.sh /c/evm-tools

```
+ 举例

```sh
cd tools
./evm.sh /c/evm-tools
```

+ 安装完成后，**重启Git终端，cd到evm目录**


## 4. 编译体验

+ 根据指定的board芯片类型进行编译

```
west build -b bearpi_stm32l431 bsp/stm32/bearpi_stm32l431
```

+ 烧写程序

```
west build -t run
```
