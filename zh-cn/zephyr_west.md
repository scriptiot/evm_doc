## 1. west是什么

**`west`**是zephyr官方提供的命令行工具，用于控制基于Zephyr应用环境搭建、升级、项目编译、调试、烧写；

## 2. west命令简介

| 子命令      |   含义 | 
| :-------- | :--------|
| init  | 初始化west工作空间 | 
| update  | 更新west.yml中的模块|
| list  | zephyr模块列表 |
| help  | 帮助 | 
| config  | 配置读取和设置 |
| topdir  | 显示west工作空间目录 |
| boards  | 支持的boards | 
| build  | 编译程序 |
| flash  | 烧录程序 |
| debug  | 调试程序 |
| zephyr-export  | 注册zephyr为cmake配置包 |

## 3. west 常用命令简介



+ 编译程序

    + 命令
```sh
    west build -b BOARD -d BUILD_DIR
```
    + 举例
```sh       
    west build -b bearpi_stm32l431 -d build/bearpi_stm32l431/bearpi_stm32l431 
```

+ 清空编译中间文件

    + 命令
```sh
    west build -b BOARD -d BUILD_DIR -t clean
```
    + 举例 
```sh
    west build -b bearpi_stm32l431 -d build/bearpi_stm32l431/bearpi_stm32l431 -t clean
```
+ 烧写程序

    + 命令
```sh
    west flash -d BUILD_DIR
```
    + 举例
```sh
    west flash -d build/bearpi_stm32l431/bearpi_stm32l431/ 
```

+ 调试程序
   + 命令
```sh
    west debug -d BUILD_DIR
```
   + 举例
```sh
    west debug -d build/bearpi_stm32l431/bearpi_stm32l431/
```
