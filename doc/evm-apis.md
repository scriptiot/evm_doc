## EVM 虚拟机开发手册

本文档主要介绍EVM虚拟机相关的技术特性与API使用手册

### EVM虚拟机介绍

EVM虚拟机是一款轻量级的嵌入式虚拟机。它可以运行在资源受限的单片机设备上，最小RAM为2KB，最小Flash为50KB。

EVM目前主要特性有：
- 支持JavaScript、Python、Lua、QML、XML、JSON混合编程。
- 高效的垃圾回收机制，无内存碎片。
- 运行速度快。
- 交互式编程。
- 生成和加载字节码文件。


### EVM虚拟机设计简介

#### 常量

EVM虚拟机常量定义分为两种，一种是字符串常量，另外一种是数字常量。在虚拟机中，常量被分别保存在全局的常量池中：

```
evm_const_pool_t * string_pool; //字符串常量池
evm_const_pool_t * number_pool; //数字常量池
```

数字常量池是按添加顺序进行存储的，常量池中不会出现重复的数字。而字符串常量是按哈希表方式进行存储的，EVM虚拟机针对哈希表算法进行了优化，不仅提高的存取速度，同时满足了轻量化的哈希表扩容算法。

#### key值

EVM虚拟机访问字符串常量不是采用记录字符串在内存的地址值，而是通过获取key值而获取到字符串内容。所谓的key值是字符串在常量池中的值，为16位整型值。如果需要访问字符串内容，则需要通过下面的方法来获取：

```
char *evm_string_get(evm_t * e, uint16_t key);
```

如果要向常量池中增加字符串或者数字，可以使用下面的方法：

```
int evm_str_insert(evm_t *e, const char *str, int alloc);//添加字符串，返回key值
int evm_number_insert(evm_t *e, double num);//添加数字常量，返回key值
```

返回-1表示添加失败。

#### evm_val_t

EVM虚拟机通过evm_val_t来表示最基本的数据类型。evm_val_t相当于一个64位的整型数据，通常在单片机领域，大部分数据都是32位，包括指针地址。EVM将外部数据包装成evm_val_t，通过标记方式，对数据进行分类。EVM虚拟机目前支持的数据类型有：

```c
TYPE_NUMBER = 0, //数字类型
TYPE_HEAP_STRING,//堆字符串
TYPE_FOREIGN_STRING, //外部字符串
TYPE_BOOLEAN,//布尔
TYPE_FUNCTION,//函数
TYPE_NATIVE,//内置函数
TYPE_NULL,//空类
TYPE_UNDEFINED,//未定义类型
TYPE_NAN,//非法数字类型
TYPE_LIST,//数组类型
TYPE_BUFFER,//字节数组类型
TYPE_OBJECT,//对象类型
TYPE_CLASS,//类
TYPE_INT,//整数类型
TYPE_FRAME,//（虚拟机专用）
TYPE_FOREIGN,//（虚拟机专用）
```

同时，EVM虚拟机在这些基本类型之上，又对对象类型进行了扩展，其中：

```c
TYPE_HEAP_STRING,
TYPE_LIST,
TYPE_BUFFER,
TYPE_OBJECT,
TYPE_CLASS,
```

这几个基本类型均为对象类型，那么扩展的对象类型有：

```c
GC_NONE, 非法类型
GC_ROOT, 根作用域
GC_OBJECT, 对象
GC_NATIVE_OBJECT, 内置对象
GC_DICT, 字典
GC_CLASS, 类
GC_SET, 集合
GC_FUNC, 函数
GC_CLOSURE_FUNC, 闭包函数
GC_STATIC_FUNC, 静态函数
GC_LIST, 数组
GC_BUFFER, 字节数组
GC_BUFFER16, 16位数组
GC_BUFFER32, 32位数组
GC_BUFFER64, 64位数组
GC_BUFFER16_U, 无符号16位数组
GC_BUFFER32_U, 无符号32位数组
GC_BUFFER64_U, 无符号64位数组
GC_BUFFER_FLOAT, 浮点数组
GC_BUFFER_DOUBLE, 双精度浮点数组
GC_STRING, 堆字符串
GC_NUMBER, 数字
GC_BOOLEAN, 布尔
GC_TUPLE, 元组
GC_MODULE, 模块
GC_MEMBER, （虚拟机专用）
GC_MEMBER_KEYS, （虚拟机专用）
GC_MEMBER_VALS, （虚拟机专用）
```


### 虚拟机API介绍

#### 虚拟机对外实现接口

` extern char evm_repl_tty_read(evm_t * e)`
虚拟机交互式编程终端读取字符接口

#### 虚拟机注册接口

```
void evm_register_print(intptr_t fn); //注册接口
extern void (*evm_print)(const char *fmt, ...); //接口格式
```
注册一个打印接口

```
void evm_register_free(intptr_t fn); //注册接口
extern void (*evm_free)(void * mem); //接口格式
```
注册外部内存释放接口

```
void evm_register_file_load(intptr_t fn); //注册接口
const char * vm_load(evm_t * e, char * path, int type); //接口格式
```
注册虚拟机文件加载方式

```
void evm_register_malloc(intptr_t fn); //注册接口
extern void * (*evm_malloc)(int size); //接口格式
```
注册外部内存申请接口

#### 虚拟机启动相关函数

`evm_err_t evm_start(evm_t * e);`

启动虚拟机：
- e，虚拟机运行参数

```
evm_err_t evm_init(evm_t * e, 
				   int heap_size, 
				   int stack_size,
				   int module_size,
				   int var_name_len, 
				   int file_name_len);
```

虚拟机初始化：
- e，虚拟机运行参数
- heap_size，堆大小
- stack_size，栈大小
- module_size，支持模块数量大小
- var_name_len，变量名称最大长度
- file_name_len，文件名称最大长度

```
void evm_deinit(evm_t * e);
```

注销虚拟机：
- e，虚拟机运行参数

```
evm_err_t evm_boot(evm_t *e, char *path);
```

虚拟机加载：
- e，虚拟机运行参数
- path，文件路径

```
evm_err_t evm_executable_load(evm_t *e, uint8_t * buf);
```

虚拟机加载字节码二进制数据：
- e，虚拟机运行参数
- buf，数据内容

```
evm_err_t evm_executable_run(evm_t *e);
```

虚拟机运行字节码数据：
- e，虚拟机运行参数

```
evm_val_t evm_run_callback(evm_t * e, 
						   evm_val_t * scope, 
						   evm_val_t *p_this, 
						   evm_val_t *args, 
						   int argc);
```

虚拟机运行回调函数：
- e，虚拟机运行参数
- scope，函数或者作用域
- p_this，当前对象
- args，参数内容
- argc，参数个数

#### 虚拟机对象操作

```
evm_val_t *evm_object_create(evm_t * e, int type, int prop_len, int attr_len);
```

创建对象：
- e，虚拟机运行参数
- type，对象类型
- prop_len，成员数量长度
- attr_len，扩展属性长度

```
evm_val_t *evm_object_create_ext_data(evm_t * e, int type, intptr_t ext_data)；
```

创建带有外部数据的新对象：
- e，虚拟机运行参数
- type，对象类型
- ext_data，外部数据（用户自定义数据）

```
evm_val_t * evm_object_create_by_class(evm_t * e, int type, evm_val_t * o);
```

通过类来创建对象：
- e，虚拟机运行参数
- type，对象类型
- o，class对象值

```
evm_val_t *evm_native_function_create(evm_t *e, evm_native_fn fn, int attr_len);
```

创建内置函数对象：
- e，虚拟机运行参数
- fn，绑定的内置函数
- attr_len，扩展属性长度

```
evm_val_t * evm_list_create(evm_t * e, int type, uint16_t len);
```

创建数组、列表对象：
- e，虚拟机运行参数
- type，数组类型（可以是LIST，SET，TUPLE）
- len，数组长度

```
evm_val_t *evm_heap_string_create(evm_t *e, char *str, int len);
```

创建堆字符串对象：
- e，虚拟机运行参数
- str，复制到堆的字符串
- len，指定字符串长度

```
evm_val_t *evm_buffer_create(evm_t *e, int len);
```

创建字节数组对象：
- e，虚拟机运行参数
- len，指定数组长度



