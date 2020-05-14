## 1. 基于EVM和Zephyr开发板适配指南

本章节主要内容是介绍如何基于EVM和Zephyr适配一块新的开发板，具体以**`bsp/stm32/bearpi_stm32l431`** 小熊派开发板为例进行讲解。

## 2. 目录结构介绍

| 文件      |    说明|
| :-------- | --------:|
| **boards**| boards目录 |
| **boards/bearpi_stm32l431_defconfig**| 小熊派board配置 |
| **boards/bearpi_stm32l431.dts**| 小熊派对应的devicetree描述文件 |
| **boards/bearpi_stm32l431.ymal**| 小熊派board描述信息 |
| **boards/board.cmake**|   烧写程序配置  | 
| **boards/Kconfig.board**|   board对应的Kconfig配置  | 
| **boards/Kconfig.defconfig**|   defconfig对于的Kconfig配置  |
| **soc**|  芯片配置目录  | 
| **CMakeLists.txt**|  cmake工程文件|
| **prj.conf**|   用户配置|


## 3. 关键文件解析


### 3.1 CMakeLists.txt

```sh
set(BOARD_ROOT ${CMAKE_CURRENT_LIST_DIR})

set(SOC_ROOT ${CMAKE_CURRENT_LIST_DIR})

set(BOARD bearpi_stm32l431)
```

+ BOARD_ROOT 指定board对应的目录
+ SOC_ROOT 指定soc对应的目录
+ BOARD 指定board对应的名称

### 3.2 prj.conf

```c
# nothing here
CONFIG_NEWLIB_LIBC=y
CONFIG_STDOUT_CONSOLE=y
CONFIG_CONSOLE_SUBSYS=y
CONFIG_CONSOLE_GETCHAR=y
CONFIG_GPIO=y
CONFIG_STDOUT_CONSOLE=y
CONFIG_PRINTK=y
CONFIG_MAIN_STACK_SIZE=4096

CONFIG_FLASH=y
CONFIG_DISPLAY=y
CONFIG_SPI=y
CONFIG_ST7789V=y
CONFIG_LOG=y
CONFIG_SPI_LOG_LEVEL_ERR=y
CONFIG_ADC=y
CONFIG_ADC_STM32=y

CONFIG_DAC=y
CONFIG_DAC_STM32=y

```

+ CONFIG_NEWLIB_LIBC 启动 NEWLIB_LIBC
+ ...

### 3.3 boards/bearpi_stm32l431_defconfig

