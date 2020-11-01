## 1. 安装zephyr-sdk编译工具链

+ 下载最新版本的zephyr-sdk:

    + github用户
        ```sh
        cd ~
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases\
        /download/v0.11.2/zephyr-sdk-0.11.2-setup.run
        ```
    + 国内用户可以使用百度云盘下载
        + 链接：`https://pan.baidu.com/s/1zMU0MhU03ZGqcVBUifsMWA`
        + 提取码：`nftx `

+ 运行installer, 安装 SDK 到 ~/zephyr-sdk-0.11.2:

```sh
chmod +x zephyr-sdk-0.11.2-setup.run
./zephyr-sdk-0.11.2-setup.run -- -d ~/zephyr-sdk-0.11.2
```

> ` 切记，一旦安装，禁止移动sdk安装目录.`


+ 设置 Zephyr SDK 需要使用的环境变量



```sh
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export ZEPHYR_SDK_INSTALL_DIR=~/zephyr-sdk-0.11.2
```

> `将上述代码写入~/.bashrc, 保证下次启动终端环境变量依然有效`

+ 安装 udev rules, 方便flash绝大多数Zephyr boards:

```sh
sudo cp ${ZEPHYR_SDK_INSTALL_DIR}/sysroots/x86_64-pokysdk-\
linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d

sudo udevadm control --reload
```

## 2. 一键安装EVM开发环境

+ evm.sh用法

```sh
cd tools
./evm.sh
```

+ 安装完成后，**重启Terminal终端，cd到evm目录**


## 3. 编译体验


+ 使用qemu_cortex_m3模拟构建EVM

```
west build -b qemu_cortex_m3 bsp/qemu_cortex_m3/ejs -d \
build/qemu_cortex_m3/ejs
```

+ 运行程序

```
west build -t run -d build/qemu_cortex_m3/ejs
```
