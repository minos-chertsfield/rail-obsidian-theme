---
title: Rail 主题测试
tags:
  - rail/test
author: minos
status: open
cssclasses:
  - wide-page
created: 2026-11-04
---

# Rail 主题测试

一套主题的完整渲染测试：覆盖标题、格式、链接、列表、代码、表格、callout 与调色板展示。

## 标题层级 Heading Levels

### 三级标题 H3 — 深浅色都应清晰

#### 四级标题 H4

##### 五级标题 H5

###### 六级标题 H6

## 文本格式 Text Styles

**粗体**、*斜体*、***粗斜体***、~~删除线~~、==高亮文本==、`行内代码`、普通文本混排效果。维基链接：[Rail 主题测试](Rail 主题测试.md)，未解析链接：[[不存在的页面]]，外部链接：[Obsidian 官网](https://obsidian.md)。

脚注引用[^1]，行内公式 $E = mc^2$。

[^1]: 脚注内容。

## 列表 Lists

- 无序列表项
    - 嵌套项
1. 有序列表
2. 第二项
- [ ] 未完成任务
- [x] 已完成任务

## 代码块 Code Blocks

```text
纯文本代码块：背景应与正文明确区分。
第二行文本。
```

```ts
// TypeScript：语法高亮逐色核对
interface Palette {
  accent: string;
  onAccent: string;
}
const RAIL = { accent: "#8dff4f" };   // keyword, string, number
export function mix(a: Palette, pct: number): string {
  const hex = a.accent.slice(1);      // comment 灰
  return `rgba(${pct})`;              // template string
}
```

```python
# Python：语法高亮
from typing import Optional

class Renderer:
    """Docstring comment."""
    def __init__(self, width: int = 800):
        self.width = width

    @property
    def area(self) -> int:
        return self.width ** 2
```

```css
.theme-dark {
  --code-keyword: #ff7b72;
  --code-string: #a5d6ff;
}
```

## 表格 Table

| 变量 | 深色值 | 浅色值 | 说明 |
| --- | --- | --- | --- |
| `--color-accent` | `#8dff4f` | `#2a7314` | 强调色 |
| `--text-normal` | `#f4f4f5` | `#27272a` | 正文 |
| `--code-string` | `#a5d6ff` | `#0a3069` | 字符串 |

## Callout 全类型 Callouts

> [!note] Note — info 蓝
> 使用 `--callout-info`。

> [!abstract] Abstract — 摘要
> 使用 `--callout-summary`。

> [!info] Info — 信息
> 使用 `--callout-info`。

> [!tip] Tip — 绿色系
> 使用 `--callout-tip`。

> [!success] Success — 成功
> 使用 `--callout-success`。

> [!question] Question — 问题
> 使用 `--callout-question`。

> [!warning] Warning — 黄色系
> 使用 `--callout-warning`。

> [!failure] Failure — 失败
> 使用 `--callout-fail`。

> [!danger] Danger — 红色系
> 使用 `--callout-error`。

> [!bug] Bug — 缺陷
> 使用 `--callout-bug`。

> [!example] Example — 紫色系
> 使用 `--callout-example`。

> [!quote] Quote — 引用
> 使用 `--callout-quote`。

## 引用块 Blockquote

> 引用块背景应与正文区分，左侧强调色边框。
> 支持多行。

## 调色板 Palette

**Rail Dark**

| 色板 | 色值 | 用途 |
| --- | --- | --- |
| 🟩 `#8dff4f` | accent | 强调、标题、光标、列表标记 |
| 🔵 `#6ac8ff` | info | 链接、信息类 callout |
| 🟥 `#ff4b75` | danger | 错误、危险 callout |
| 🟨 `#ffd54b` | warning | 警告 callout、高亮 |
| 🟪 `#d2a8ff` | function | 函数、注解、紫色系 callout |
| ⬜ `#18181b` | content | 代码块、引用块背景 |

**Rail Light**

| 色板 | 色值 | 用途 |
| --- | --- | --- |
| 🟩 `#2a7314` | accent | 强调、标题 |
| 🔵 `#2265cf` | info | 链接 |
| 🟥 `#d02533` | danger | 错误 |
| 🟨 `#946300` | warning | 警告 |
| 🟪 `#8250df` | function | 函数 |

## 标签与属性 Tags

#测试标签 #rail/theme

---

水平线以上完成全部渲染测试。
