该项目是一个用于《我的世界》(Minecraft) 枪械模组（TACZ）的指令生成工具，主要目的是帮助玩家快速生成特定武器的指令代码。以下是项目的 README 内容：

---

# MC-TACZ Arms CMD Picker

**MC-TACZ Arms CMD Picker** 是一个为 Minecraft TACZ 模组设计的指令生成工具，旨在帮助玩家快速生成特定武器的指令代码。

## 📌 项目简介

该项目基于 Python 编写，包含一个简单的命令行界面，用于选择武器并生成对应的 Minecraft 指令。适用于 TACZ 模组中武器调试、测试或服务器管理场景。

## 📁 文件结构说明

- `main.py`：程序主入口，负责武器选择和指令生成。
- `utils.py`：包含辅助函数，如输入验证。
- `data/gun_id.py`：武器 ID 列表，用于映射武器名称到对应 ID。
- `data/cmd_list.py`：指令模板列表，定义不同武器的指令格式。
- `data/__init__.py`：初始化模块，用于组织数据文件。

## 🛠️ 使用方法

1. 确保你已安装 Python 3.x。
2. 运行 `main.py` 文件：
   ```bash
   python main.py
   ```
3. 按照提示选择武器并生成指令。

## 📝 示例输出

选择武器后，程序将输出类似以下格式的指令：
```
/give @p tacz:weapon_<gun_id>
```

## 📎 依赖项

- 无第三方库依赖，仅使用标准库。

## 🤝 贡献指南

欢迎提交 PR 或 Issue 来改进项目。你可以添加更多武器支持、优化 UI 或完善文档。

## 📄 许可证

本项目采用 MIT 许可证。详见 `LICENSE` 文件。

---

如有问题或建议，请在项目页面提交 Issue。