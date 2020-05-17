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

> 注册 `evm_builtin_t`列表中所有的API注册到命名为`name`的模块中

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
	evm_runtime = e;
	number_of_callbacks = CONFIG_EVM_CALLBACK_SIZE;
	callback_list = evm_list_create(e, GC_LIST, number_of_callbacks);
	if( !callback_list ) return e->err;

	for(uint32_t i = 0; i < number_of_callbacks; i++){
		evm_list_set(e, callback_list, i, EVM_VAL_UNDEFINED);
	}

	
	args_list = evm_list_create(e, GC_LIST, number_of_callbacks);
	if( !args_list ) return e->err;

	evm_builtin_t module[] = {
		{"delay_ms", evm_mk_native((intptr_t)evm_module_delay_ms)},
		{"delay_us", evm_mk_native((intptr_t)evm_module_delay_us)},
#ifdef CONFIG_EVM_GPIO
		{"Pin", evm_class_pin(e)},
#endif
#ifdef CONFIG_EVM_LCD
		{"LCD", evm_class_lcd(e)},
#endif
#ifdef CONFIG_EVM_LED
		{"LED", evm_class_led(e)},
#endif
#ifdef CONFIG_EVM_FLASH
		{"Flash", evm_class_flash(e)},
#endif
#ifdef CONFIG_EVM_ADC
		{"ADC", evm_class_adc(e)},
#endif
#ifdef CONFIG_EVM_DAC
		{"DAC", evm_class_dac(e)},
#endif
#ifdef CONFIG_EVM_RTC
		{"RTC", evm_class_rtc(e)},
#endif
#ifdef CONFIG_EVM_SWITCH
		{"Switch", evm_class_switch(e)},
#endif
#ifdef CONFIG_EVM_WATCHDOG
		{"Watchdog", evm_class_watchdog(e)},
#endif
#ifdef CONFIG_EVM_TIMER
		{"Timer", evm_class_timer(e)},
#endif
#ifdef CONFIG_EVM_UART
		{"UART", evm_class_uart(e)},
#endif
        {NULL, NULL}
    };
    evm_module_create(e, "evm", module);
	return e->err;
}
```