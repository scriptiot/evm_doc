## 1. 什么是基于EVM的lib库

> EVM是一款通用性虚拟机，目前支持javascript、python、lua、qml、json和xml等多种语言；针对不同的语言EVM会发布针对不同平台的lib库，供社区免费使用。

---

## 2. lib库简介

> lib库发布在[evm](https://github.com/scriptiot/evm)项目目录**`lib`**目录中，根据不同的平台进行分类；

---

### 2.1 基于evm的libejs库

> libejs是基于evm支持javascript语言的静态库

| 文件      |    说明|
| :-------- | --------:|
| **lib/arm_windows_armcc/libejs.lib**|  windows平台libejs静态库(armcc, Keil)|
| **lib/x86_64_linux_gnu/linux/libejs.a**|  Linux平台libejs静态库 （gcc7 64位）|
| **lib/x86_64_windows_mingw/libejs.a**|  windows平台libejs静态库(MinGW-gcc 64位)|

---

### 2.2 基于evm的libqml库

> libqml是基于evm支持qml语言的静态库

| 文件      |    说明|
| :-------- | --------:|
| **lib/arm_windows_armcc/libqml.lib**|  windows平台libqml静态库(armcc, Keil)|
| **lib/x86_64_linux_gnu/linux/libqml.a**|  Linux平台libqml静态库 （gcc7 64位）|
| **lib/x86_64_windows_mingw/libqml.a**|  windows平台libqml静态库(MinGW-gcc 64位)|
