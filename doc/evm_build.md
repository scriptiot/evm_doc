## 如何在x86平台快速编译构建ejs


### 1. gcc命令编译

> windows平台基于mingw730_64构建的libejs.a静态库，请使用gcc7.3版本以上的gcc构建项目


```c
/c/Qt/Qt5.14.1/Tools/mingw730_64/bin/gcc.exe -std=c99 main.c ../thirds/cjson/cJSON.c -DQMAKE_TARGET=\"ejs\" -DQMAKE_VERSION=\"1.0\" -L ../lib/x86_64-windows-mingw -l:libejs.a -I ../include/ -I ../thirds/cjson/ -o ejs.exe
```

![evm_build_1](./image/evm_build_1.gif)

### 2. Qt工程编译

+ 建议编译环境使用 **Qt 最新版**  http://download.qt.io/archive/qt/5.14/5.14.1/  Qt Creater打开 `ejs.pro` 直接进行编译即可

![evm_build_qt](./image/evm_build_qt.gif)