## 1. EVM标准化的API扩展接口

---

### 1.1 数据结构

+ `name`: 注册接口名称
+ `v`: 注册接口API实现

```c
typedef struct evm_builtin_t{
    const char * name;
    evm_val_t v;
}evm_builtin_t;

```

### 1.2 evm_module_create

> `evm_module_create`把`evm_builtin_t`列表中所有的API注册到命名为`name`的模块中

```c
/**
 * @brief 创建指定名称的模块
 * @param e，虚拟机
 * @param name，名称
 * @param n，内置成员列表
 * @return 内置对象
 */
evm_val_t evm_module_create(evm_t * e, const char* name, evm_builtin_t *n);
```

## 2. 扩展模块注册流程

```c
/**********定义用户API*****************/



/**********创建模块*****************/
int evm_module(evm_t * e){
	evm_builtin_t module[] = {
		{"Pin", evm_class_pin(e)},
		{"LCD", evm_class_lcd(e)},
		{"LED", evm_class_led(e)},
		{"LED", evm_class_flash(e)},
		{"ADC", evm_class_adc(e)},
		{"DAC", evm_class_dac(e)},
		{"RTC", evm_class_rtc(e)},
		{"Switch", evm_class_switch(e)},
        {NULL, NULL}
    };
    evm_module_create(e, "evm", module);
	return e->err;
}
```