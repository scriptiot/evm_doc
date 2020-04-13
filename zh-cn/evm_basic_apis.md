## 1. 虚拟机类型判断API

### 1.1 判断evm_val_t对象是否为数字

```c
int evm_is_number(evm_val_t *v)

```

### 1.2 判断evm_val_t对象是否为整数

```c
int evm_is_integer(evm_val_t *v)

```

### 1.3 判断evm_val_t对象是否为堆字符串

```c
int evm_is_heap_string(evm_val_t *v)

```

### 1.4 判断evm_val_t对象是否为外部字符串

```c
int evm_is_foreign_string(evm_val_t *v)

```

### 1.5 判断evm_val_t对象是否为字符串

```c
int evm_is_string(evm_val_t *v)

```

### 1.6 判断evm_val_t对象是否为布尔值

```c
int evm_is_boolean(evm_val_t *v)

```

### 1.7 判断evm_val_t对象是否为字符数组

```c
int evm_is_buffer(evm_val_t *v)

```

### 1.8 判断evm_val_t对象是否为脚本函数

```c
int evm_is_script(evm_val_t *v)

```

### 1.9 判断evm_val_t对象是否为内置函数

```c
int evm_is_native(evm_val_t *v)

```

### 1.10 判断evm_val_t对象是否为数组、列表

```c
int evm_is_list(evm_val_t *v)

```

### 1.11 判断evm_val_t对象是否为外部指针

```c
int evm_is_foreign(evm_val_t *v)

```


### 1.12 判断evm_val_t对象是否为函数

```c
int evm_is_function(evm_val_t *v)

```

### 1.13 判断evm_val_t对象是否为undefined

```c
int evm_is_undefined(evm_val_t *v)

```

### 1.14 判断evm_val_t对象是否为空

```c
int evm_is_null(evm_val_t *v)

```

### 1.15 判断evm_val_t对象是否为NaN

```c
int evm_is_nan(evm_val_t *v)

```

### 1.16 判断evm_val_t对象是否为对象

```c
int evm_is_object(evm_val_t *v)

```

### 1.17 判断evm_val_t对象是否为类

```c
int evm_is_class(evm_val_t *v)

```

## 2.虚拟机类型转换API

### 2.1 evm_val_t数字对象是转浮点

```c
double evm_2_double(evm_val_t *v)

```

### 2.2 evm_val_t数字对象是转整数

```c
double evm_2_integer(evm_val_t *v)

```

### 2.3 evm_val_t对象是转布尔

```c
int evm_2_boolean(evm_val_t *v)

```

### 2.3 evm_val_t对象是转字符串

```c
const char *evm_2_string(evm_val_t *v);

```

### 2.4 evm_val_t数字对象是转指针

```c
intptr_t evm_2_intptr(evm_val_t *v)

```

## 3. 虚拟机对象创建API

### 3.1 创建浮点型evm_val_t对象

```c
evm_val_t evm_mk_number(double d)

```

### 3.2 创建整形evm_val_t对象

```c
evm_val_t evm_mk_integer(int v, int type)

```

### 3.3 创建外部字符串evm_val_t对象

```c
evm_val_t evm_mk_foreign_string(intptr_t s)

```

### 3.4 创建堆字符串evm_val_t对象

```c
evm_val_t evm_mk_heap_string(intptr_t s)

```

### 3.5 创建布尔evm_val_t对象

```c
evm_val_t evm_mk_boolean(int v)

```

### 3.6 创建脚本函数evm_val_t对象

```c
evm_val_t evm_mk_script(intptr_t s)

```

### 3.7 创建内置函数evm_val_t对象

```c
evm_val_t evm_mk_native(intptr_t s)

```

### 3.8 创建null空值evm_val_t对象

```c
evm_val_t evm_mk_null(void)

```

### 3.9 创建undefined值evm_val_t对象

```c
evm_val_t evm_mk_undefined(void)

```

### 3.10 创建obejct值evm_val_t对象

```c
evm_val_t evm_mk_object(void *ptr)

```

### 3.11 创建字节数组值evm_val_t对象

```c
evm_val_t evm_mk_buffer(void *ptr)

```

### 3.12 创建数组或列表值evm_val_t对象

```c
evm_val_t evm_mk_list(void *ptr)

```

### 3.13 创建数组或列表值evm_val_t对象

```c
evm_val_t evm_mk_list(void *ptr)

```

### 3.13 创建true值evm_val_t对象

```c
evm_val_t evm_mk_true(void)

```

### 3.14 创建false值evm_val_t对象

```c
evm_val_t evm_mk_false(void)

```

### 3.15 创建NaN值evm_val_t对象

```c
evm_val_t evm_mk_nan(void)

```
