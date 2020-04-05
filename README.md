## 工具介绍
这是一个基于 `Ant Design Vue` 和 `Marked.js` 开发的文档模块，用于快速构建文档。

---

## 工具特点
- 纯静态，开箱即用，不依赖数据库
- 自动根据标题生成锚点链接，支持快速跳转

---

## 如何使用
将 markdown 文档放入 `doc` 目录，如：
```
doc/doc1.md
doc/doc2.md
doc/doc3.md
doc/doc4.md
doc/doc5.md
doc/doc6.md
```

在 `config.json` 中配置标题及菜单，如：
```
{
    "title": "文档模块", // 标题名称
    "menu": [
        {
            "title": "父级菜单 1", // 父级菜单名称
            "icon": "folder", // 父级菜单图标（图标地址：https://antdv.com/components/icon-cn/）
            "child": [
                {
                    "title": "子级菜单 1", // 子级菜单名称
                    "key": "doc1" // 子级菜单文档名称（doc/doc1.md）
                },
                {
                    "title": "子级菜单 2",
                    "key": "doc2"
                }
            ]
        },
        {
            "title": "父级菜单 2",
            "icon": "heart",
            "child": [
                {
                    "title": "子级菜单 3",
                    "key": "doc3"
                },
                {
                    "title": "子级菜单 4",
                    "key": "doc4"
                }
            ]
        },
        {
            "title": "父级菜单 3",
            "icon": "bulb",
            "child": [
                {
                    "title": "子级菜单 5",
                    "key": "doc5"
                },
                {
                    "title": "子级菜单 6",
                    "key": "doc6"
                }
            ]
        }
    ]
}

```

## 本地编辑预览


> 安装python3, 在当前目录执行如下命令，在浏览器输入`http://127.0.0.1:8000`即可实时预览

```

python3 -m http.server

```
