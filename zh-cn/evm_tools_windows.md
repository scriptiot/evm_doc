## 1. evm-tools是什么

**`evm-tools`** 是EVM官方团队针对windows平台提供的编译工具链，用于编译、调试和烧写程序；

| 工具      |   描述 |  版本 |
| :-------- | :--------| :--------|
| cmake  | cmake工程工具 | cmake version 3.13.2 |
| gcc-arm-none-eabi | 嵌入式arm编译工具 | gcc-arm-none-eabi-9-2019-q4-major-win32 |
| ninja  | 构建工具 | 1.10.0 |
| openocd  | 开源片上调试器 | Open On-Chip Debugger 0.10.0 (2020-04-08)  |
| qemu  | 虚拟化模拟器 | QEMU releases 0.12 |

## 2. 安装Git终端

+ [下载安装windows git终端](https://github.com/git-for-windows/git/releases/download/v2.26.2.windows.1/Git-2.26.2-64-bit.exe)

> 如果已经安装，请跳过！

## 3. 安装python3

+ 下载 [Python3](https://www.python.org/downloads/release/python-370/)

> 如果python3已经安装，跳过!

## 4. 下载evm-tools

+ 解压到任意目录

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
