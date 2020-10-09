<a name="ZeAlN"></a>
# 1. 报告概述
<a name="u25E9"></a>
## 1.1 报告目的

<br />本文档旨在帮助用户快速的了解EVM超轻量物联网虚拟机对javascript语言的支持程度和虚拟机的性能，加深的EVM的理解和认识；
<a name="P3Wyh"></a>
## 1.2 报告范围

<br />本报告对社区免费开放，欢迎社区用户体验EVM并提供宝贵的意见。
<a name="Qooce"></a>
## 1.3 软件简介

<br />**`EVM`** 全称`Embedded Virtual Machine`，本质上是一款通用、精简的嵌入式虚拟机，由语法解析前端框架和字节码运行后端构成，可运行在资源受限制的单片机上。
<a name="XEvjA"></a>
## 1.4 软件版本和仓库



| 软件 | 版本 | 仓库地址 |
| --- | --- | --- |
| **EVM** | EVM内部最新版1.9 | [https://github.com/scriptiot/evm](https://github.com/scriptiot/evm) |
| **QuickJS** | QuickJS最新tag 20200705 版本 | [https://github.com/horhof/quickjs](https://github.com/horhof/quickjs) |
| **benchmark** | EVM测试仓库 1.0 | [https://github.com/scriptiot/benchmark](https://github.com/scriptiot/benchmark) |



<a name="ie7hL"></a>
# 2. 目录结构



| **文件** |  | **说明** |
| :---: | :---: | --- |
| **evm** | bin | windows和Linux的ejs二进制版本 |
|  | lib | windows和Linux的libejs.a 静态库 |
|  | src | ejs源码工程目录 |
| **quickjs** | bin | windows和Linux的quickjs二进制版本 |
|  | src | quickjs源码工程目录 |
| **test** | benchmark | 性能测试脚本集 |
|  | basic | 基础语法测试脚本集 |
|  | operater | 运算符测试脚本集 |
|  | statement | 语句测试脚本集 |
|  | object | 对象测试脚本集 |
|  | function | 函数测试脚本集 |
| readme.md |  | 仓库说明文件 |

<a name="5lltd"></a>
# 3. 功能测试


<a name="poJL1"></a>
## 3.1 测试目的

<br />验证EVM对javascript语法的支持程度
<a name="wMSRM"></a>
## 3.2 测试环境
<br />

| 测试环境 | 类型 | 生产商/来源 | 硬件配置 | 软件版本 |  |
| :---: | :---: | :---: | :---: | :---: | --- |
|  |  |  |  | os | gcc |
|  | 测试机-1 | 联想Air13 | 处理器：Intel i7 10710 12核<br />内存：16 GB<br />存储：1T<br />主频：1.61GHz | windows 10  | gcc version 7.3.0 (x86_64-posix-seh-rev0, Built by MinGW-W64 project) |

<a name="7GqkR"></a>
## 3.3 语法测试结果
测试脚本位于项目根目录/test下面

![evm_function](image/evm_function.png)


<a name="oJqcg"></a>
# 4. 性能测试


<a name="9M4RQ"></a>
## 4.1 测试目的

<br />对比EVM虚拟机和QuickJs虚拟机的运行性能，为EVM的性能优化提供性能基准参考。
<a name="xCaQn"></a>
## 4.2 测试环境


| 测试环境 | 类型 | 生产商/来源 | 硬件配置 | 软件版本 |  |
| :---: | :---: | :---: | :---: | :---: | --- |
|  |  |  |  | os | gcc |
|  | 测试机-1 | 联想Air13 | 处理器：Intel i7 10710 12核<br />内存：16 GB<br />存储：1T<br />主频：1.61GHz | windows 10  | gcc version 7.3.0 (x86_64-posix-seh-rev0, Built by MinGW-W64 project) |
|  | 测试机-2 | 组装台式机 | 处理器：Intel i5-9600K 6核<br />内存：32 GB<br />存储：1T<br />主频：3.70GHz | windows 10 WSL (ubuntu 20.04) | None |
|  | 测试机-3 |  | 处理器：Intel i7 10710<br />内存：16 GB<br />存储：1T<br />主频：1.1GHz |  |  |



<a name="dAIzO"></a>
## 4.3 测试脚本


- 本报告中所有的测试脚本来自于 [《JavaScript 基准测试套件 Octane》](https://github.com/chromium/octane)
| 测试脚本 | 描述 | 链接地址 |
| :---: | :---: | :---: |
| **NavierStokes** | <br />- Main focus: _reading and writing numeric arrays._<br />- Secondary focus: _floating point math._<br /> |  |
| **DeltaBlue** | <br />- Main focus: _polymorphism_<br />- Secondary focus: _OO-style programming_<br /> |  |
| **Richards** | <br />- Main focus: _property load/store, function/method calls_<br />- Secondary focus: _code optimization, elimination of redundant code_<br /> |  |

<a name="WD0Ad"></a>
## 4.4 测试机-1-性能测试结果

![evm_performance_1](image/evm_performance_1.png)



![image.png](https://cdn.nlark.com/yuque/0/2020/png/259002/1597200391155-c17e4eec-d142-49f0-bab2-84389811a922.png#align=left&display=inline&height=816&margin=%5Bobject%20Object%5D&name=image.png&originHeight=816&originWidth=1132&size=47232&status=done&style=none&width=1132)



![image.png](https://cdn.nlark.com/yuque/0/2020/png/259002/1597200530862-c2aefc61-b611-4d9d-8826-75d9c2f379b0.png#align=left&display=inline&height=816&margin=%5Bobject%20Object%5D&name=image.png&originHeight=816&originWidth=1132&size=49893&status=done&style=none&width=1132)


![image.png](https://cdn.nlark.com/yuque/0/2020/png/259002/1597200625489-c06df3b7-d952-4726-bb49-507551e93605.png#align=left&display=inline&height=767&margin=%5Bobject%20Object%5D&name=image.png&originHeight=767&originWidth=1132&size=46576&status=done&style=none&width=1132)

## 4.5 测试机-2-性能测试结果

![evm_performance_2](image/evm_performance_2.png)


![EVM与QuickJS 性能测试 -- NavierStokes.png](https://cdn.nlark.com/yuque/0/2020/png/443421/1597231890718-dc2389b0-e773-4022-bad9-de87fea36197.png#align=left&display=inline&height=890&margin=%5Bobject%20Object%5D&name=EVM%E4%B8%8EQuickJS%20%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95%20--%20NavierStokes.png&originHeight=890&originWidth=1209&size=64898&status=done&style=none&width=1209)

![EVM与QuickJS 性能测试 -- DeltaBlue.png](https://cdn.nlark.com/yuque/0/2020/png/443421/1597232292308-64495d7b-ff57-4c25-aeda-8b19f380b21c.png#align=left&display=inline&height=841&margin=%5Bobject%20Object%5D&name=EVM%E4%B8%8EQuickJS%20%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95%20--%20DeltaBlue.png&originHeight=841&originWidth=1209&size=67191&status=done&style=none&width=1209)

![EVM与QuickJS 性能测试 -- Richards.png](https://cdn.nlark.com/yuque/0/2020/png/443421/1597232522866-089197df-b9ab-4527-aaf0-56d9d7929065.png#align=left&display=inline&height=841&margin=%5Bobject%20Object%5D&name=EVM%E4%B8%8EQuickJS%20%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95%20--%20Richards.png&originHeight=841&originWidth=1209&size=63119&status=done&style=none&width=1209)


# 5. 测试结论

- EVM对es5的语法覆盖度达到90%以上，内置函数和扩展模块功能的覆盖度对应ECMA标准还有一定差距。
- 目前可支持的测试对象为Richards、Deltablue和NavierStokes。
- 基于当前测试结果，EVM虚拟机的整体性能略优于quickjs。部分测试依赖于外部扩展实现，与虚拟机本身性能相关不大。NavierStokes测试更偏向于计算和虚拟机性能的测试，EVM在该测试跑分项目表现较好。


# 6. 参考

- [https://developers.google.com/octane/benchmark#richards](https://developers.google.com/octane/benchmark#richards)
- ![image.png](https://cdn.nlark.com/yuque/0/2020/png/259002/1597213600154-9868e1a6-868f-4851-b592-894292091582.png#align=left&display=inline&height=2525&margin=%5Bobject%20Object%5D&name=image.png&originHeight=2525&originWidth=941&size=375066&status=done&style=none&width=941)



